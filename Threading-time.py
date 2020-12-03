import time
import threading
from GNUDormitoryCrawl import noticePageCrawler

def thread_run():
    print('=====', time.ctime(), '=====')
    for i in range(1,2):
        #크롤링 코드
        a = noticePageCrawler()
        if a == 0:
            print('새로 올라온 공지가 없습니다.')
        print('Thread running - ', i)
    threading.Timer(5, thread_run).start() #5초마다 반복

thread_run()

def test_answer():
    return thread_run()