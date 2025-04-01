from asyncio import Future

my_future: Future = Future()

print(f'Is my_future done? {my_future.done()}')

my_future.set_result(42)

print(f'Is my_future done? {my_future.done()}')
print(f'What is the result of my_future? {my_future.result()}')



class Kebab(Future):
    #custom logic
    def get_kebab(self):
        self.set_result('big rollo')