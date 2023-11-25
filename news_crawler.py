# 콘솔창 안뜨게 설정
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

# 셀리니움
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.alert import Alert

# 기타
from time import sleep
import chromedriver_autoinstaller
import os
#import json
import pandas as pd
#import openpyxl
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager

# 크롬 드라이버 옵션 설정
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--privileged')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('disable-gpu')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36")
chrome_options.add_argument('lang=ko_KR')
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

# 크롬 드라이버 자동 설치
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'
if not os.path.exists(driver_path):
    chromedriver_autoinstaller.install(True)

service = Service(driver_path)
service.creationflags = CREATE_NO_WINDOW
##### Before starting the crawler, check the data
#driver = webdriver.Chrome('C:/Users/acin/crawler/chromedriver.exe')
#driver = webdriver.Chrome(driver_path,options=chrome_options,service=service)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
#driver.get("https://sport-strategy.org/latest_news")
driver.implicitly_wait(5)
data = []
input_list = []

# 35까지만 반복해도 충분 합니다(날짜 때문에)
for p in tqdm(range(1, 36)): # => 35으로 해야됨
    # 페이지로 넘어가기
    url = f'https://sport-strategy.org/latest_news?page={p}'
    driver.get(url)
    driver.implicitly_wait(5)
    # 한 페이지에 카드 12개
    for c in range(0, 12):
        card = driver.find_elements(By.CSS_SELECTOR, '.list__item__title')
        # 카드 내부로 들어가기
        card[c].click()
        input_list = []

        news_title = driver.find_element(By.CSS_SELECTOR, '.bo_v_title')
        #news_content = driver.find_element(By.CSS_SELECTOR, '.board__content')
        news_contents = driver.find_element(By.ID,'bo_v_con').find_elements(By.TAG_NAME,'p')

        temp = ""
        for t in news_contents :
            temp += t.text
        
        news_content = temp

        input_list.append(news_title.text)
        input_list.append(news_content)
        
        print(f'{p}페이지 [{news_title.text}] => 완료')
        
        data.append(input_list)

        # 카드 밖으로 나오기
        driver.back()

df = pd.DataFrame(data,columns=['title', 'content'])

df.to_excel(f'./ISF_news.xlsx', sheet_name='data_01')

