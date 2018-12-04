import os
import urllib.request 
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 크롬 브라우저 헤드레스 옵션
options = webdriver.ChromeOptions()
options.add_argument('headless') #이 옵션에 따라 브라우저 창 visible 결정
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

# 사용할 브라우저 설정 (브라우저 드라이브 필요)
driver = webdriver.Chrome('D:/001.Project/005.Python/chromedriver_win32/chromedriver.exe', chrome_options=options)

driver.implicitly_wait(3)

# 로그인 사이트 주소와 id pw 값 소스에서 찾기
driver.get('https://www.facebook.com/')

print (driver.current_url)
print (driver.title)

# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('email').send_keys('id')
driver.find_element_by_name('pass').send_keys('pw')

# 로그인 버튼 클릭
driver.find_element_by_xpath("//input[@data-testid='royal_login_button']").click()

driver.implicitly_wait(3)

# 타임라인 선택
title = driver.find_element_by_xpath("//a[@title='프로필']")

print (title.get_attribute('href'))

driver.get(title.get_attribute('href'))

# 스크롤 대기 시간
SCROLL_PAUSE_TIME = 0.5
# 현재 스크롤 크기 
last_height = driver.execute_script("return document.body.scrollHeight")

#스크롤 끝까지 내리기
while True:
    # 스크롤 다운 버튼
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME
    # 새로 로드된 스크롤 길이 확인
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



# 친구 목록 선택 
title = driver.find_element_by_xpath("//a[@data-tab-key='friends']")

print (title.get_attribute('href'))

driver.get(title.get_attribute('href'))

titles = driver.find_elements_by_xpath("//ul[@*]")

for title in titles:
    text = title.get_attribute('class')
    print (text)
    idx = text.find('uiList')
    if idx >= 0:
        break 

print (title.get_attribute('class'))

# 친구 이름, 페이스북 주소, 프로필 사진을 수집
items = title.find_elements_by_tag_name("li")
for item in items:
    freinds = item.find_elements_by_xpath("//div[@class='uiProfileBlockContent']")
    hrefs = item.find_elements_by_xpath("//a[@aria-hidden]")
    srcs = item.find_elements_by_xpath("//img[@role='img']")

# 사진 저장할 폴더 확인 및 디렉토리 생성
srcdir = 'D:/001.Project/005.Python/imgsrc/01084356980'
if not(os.path.isdir(srcdir)):
    os.makedirs(os.path.join(srcdir))

i = 0
for freind in freinds:
    text = freind.text
    hrefinfo = hrefs[i].get_attribute('href')
    srcinfo = srcs[i].get_attribute('src')
    i = i + 1
    print (hrefinfo)
    print (srcinfo)
    print (text)
    # 이미지 저장
    urllib.request.urlretrieve(srcinfo, srcdir + str(i) + '.png' )


driver.quit()
