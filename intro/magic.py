import requests
import threading
from concurrent.futures import Future

class FetchFuture(Future):
    def __init__(self, url):
        super().__init__()
        thread = threading.Thread(target=self._fetch, args=(url,))
        thread.start()

    def _fetch(self, url):
        response = requests.get(url)
        self.set_result(response.json())


def gen(url):
    data = yield FetchFuture(url)
    print(data)
    yield


url = "https://api.nbp.pl/api/exchangerates/rates/a/eur"
g = gen(url)
future = next(g)

future.add_done_callback(lambda f: g.send(f.result()))




# class CM:
#     def __enter__(self):
#         pass
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#
# class ACM:
#     async def __aenter__(self):
#         pass
#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         pass
