import time
import threading

def thread_run():
    print('=====', time.ctime(), '=====')
    for i in range(1,3):
        #크롤링 코드
        print('Tread running - ', i)
    threading.Timer(5, thread_run).start() #5초마다 반복

thread_run()
