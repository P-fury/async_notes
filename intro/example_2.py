import os
import threading


def hello() -> None:
    print(f'hello from {threading.current_thread()}')


t1 = threading.Thread(target=hello)

t1.start()



print(f'python process running with id: {os.getpid()}')
total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'current thread name: {thread_name}')
print(f'total threads: {total_threads}')


t1.join()