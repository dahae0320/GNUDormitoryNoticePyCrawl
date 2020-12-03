import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("mykey.json")
firebase_admin.initialize_app(cred, {
    # 'databaseURL' : '데이터 베이스 URL'
    'databaseURL' : 'https://gnudormitorynotice.firebaseio.com/'
})

# 공지사항 페이지별로 데이터
def noticePageCrawler():
    number = 1
    for i in range(15):
        num = i+1
        data = requests.get('http://dorm.gnu.ac.kr/program/multipleboard/BoardList.jsp?groupNo=11171&searchType=&searchString=&category=&type=&cpage='+str(number))
        data.encoding = "UTF-8"
        parser = BeautifulSoup(data.text, 'html.parser')    #, from_encoding='utf-8'
        notice_num = parser.select("#body_content > form > div > div.board > table > tbody > tr.row"+ str(num) +"> td.first")[0].text

        ref = db.reference(notice_num.strip())
        print(ref.get()['notice_num'])
        if notice_num.strip() == ref.get()['notice_num']:
            return
        # print(num)
        # print(notice_num.strip())

        detail_data = requests.get('http://dorm.gnu.ac.kr/program/multipleboard/BoardView.jsp?groupNo=11171&boardNo='+str(notice_num.strip()))
        parser1 = BeautifulSoup(detail_data.text, 'html.parser')
        title = parser1.select("#body_content > form > div.board > div.view > div.title > h3:not(span)")[0].text
        description = parser1.select("#body_content > form > div.board > div.view > div.substance")[0].text
        author = parser1.select("#body_content > form > div.board > div.view > div.info > dl.col4 > dd:nth-child(4)")[0].text
        date = parser1.select("#body_content > form > div.board > div.view > div.info > dl.col4 > dd:nth-child(6)")[0].text

        # 데이터 삽입
        ref.update({'notice_num': notice_num.strip()})
        ref.update({'title' : title})
        ref.update({'description' : description})
        ref.update({'author' : author})
        ref.update({'date' : date})

        ++number

noticePageCrawler()

def test_answer():
    exist = noticePageCrawler()
    return exist