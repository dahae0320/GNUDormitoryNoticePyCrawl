import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("mykey.json")
firebase_admin.initialize_app(cred, {
    # 'databaseURL' : '데이터 베이스 URL'
    'databaseURL' : 'https://gnudormitorynotice.firebaseio.com/'
})

# 공지사항 페이지 1
for i in range(15):
    num = i+1
    data = requests.get('http://dorm.gnu.ac.kr/program/multipleboard/BoardList.jsp?groupNo=11171&searchType=&searchString=&category=&type=&cpage=1')
    data.encoding = "UTF-8"
    parser = BeautifulSoup(data.text, 'html.parser')    #, from_encoding='utf-8'
    notice_num = parser.select("#body_content > form > div > div.board > table > tbody > tr.row"+ str(num) +"> td.first")[0].text
    # print(num)
    # print(notice_num.strip())

    detail_data = requests.get('http://dorm.gnu.ac.kr/program/multipleboard/BoardView.jsp?groupNo=11171&boardNo='+str(notice_num.strip()))
    parser1 = BeautifulSoup(detail_data.text, 'html.parser')
    title = parser1.select("#body_content > form > div.board > div.view > div.title > h3:not(span)")[0].text
    description = parser1.select("#body_content > form > div.board > div.view > div.substance")[0].text
    author = parser1.select("#body_content > form > div.board > div.view > div.info > dl.col4 > dd:nth-child(4)")[0].text
    print(author)
    # date =

    # ref = db.reference(notice_num.strip())
    # ref.update({'title' : '안녕하세요 오늘은...'})

