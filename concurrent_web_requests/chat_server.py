import asyncio
import logging


class ChatServer:
    def __init__(self) -> None:
        self._usernames: dict = {

        }

    async def start_chat_server(self, host: str, port: int) -> None:
        server = await asyncio.start_server(self.client_connected, host, port)


        async with server:
            print('Starting Chat Server')
            await server.serve_forever()

    async def client_connected(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        command = await reader.readline()
        command, args = command.split(b' ')

        if command == b'CONNECT':
            username = args.decode().strip()
            self._add_user(username, reader, writer)
            await self._on_connect(username, writer)


        else:
            logging.error(f"Got invalid command from client, disconnection.")
            writer.close()
            await writer.wait_closed()

    def _add_user(self, username: str, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        self._usernames[username] = writer
        asyncio.create_task(self._listen_for_messages(username, reader))

    async def _listen_for_messages(self, username: str, reader: asyncio.StreamReader):
        try:
            while (data := await asyncio.wait_for(reader.readline(), 600)) != b'':
                await self._notify_all(username, f'{data.decode()}')
        except Exception as e:
            logging.error('Error reading from clinet', exc_info=e)
            await self._notify_all(username, f'has left the chat.\n')
            await self._remove_users(username)

    async def _on_connect(self, username: str, writer: asyncio.StreamWriter) -> None:
        writer.write(f"Welcome ! {len(self._usernames)} user(s) are online!\n".encode())
        await writer.drain()
        await self._notify_all(username, f'has joined the chat!\n')

    async def _notify_all(self,username:str, message: str) -> None:
        inactive_users = []
        for username_, writer in self._usernames.items():
            if username_ == username:
                continue
            try:
                writer.write(f'{username}: {message}'.encode())
                await writer.drain()
            except ConnectionError as e:
                logging.exception('Could not send to client.', exc_info=e)
                inactive_users.append(username_)

        [await self._remove_users(username) for username in inactive_users]

    async def _remove_users(self, username: str):
        writer = self._usernames[username]
        del self._usernames[username]

        try:
            writer.close()
            await writer.wait_closed()
        except Exception as e:
            logging.exception('Could not send to client.', exc_info=e)



async def main() -> None:
    server = ChatServer()
    await server.start_chat_server('localhost', 8085)



asyncio.run(main())
