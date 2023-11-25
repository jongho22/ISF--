from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl

##### Before starting the crawler, check the data
driver = webdriver.Chrome('C:/isf/crawler/chromedriver.exe')
driver.get("https://sport-strategy.org/seek_job")
driver.implicitly_wait(5)
print("1111111111111111111111111111111")
# Check the total number of pages
end_button = driver.find_element(By.CSS_SELECTOR, '.pg_page.pg_end')
end_button.click()
end_page_num = driver.find_element(By.CSS_SELECTOR, '.pg_current.pg_page.pg-for-css')
total_page = int(end_page_num.text)
print("total number of pages :", total_page)   # Current: p.193

# Back to the first page for start crawling
start_button = driver.find_element(By.CSS_SELECTOR, '.pg_page.pg_start')
start_button.click()

##### Save crawled information to dictionary
dic = {}
d_index = 0
zero = 0        # Save 0  (For the number of cards)
tweleve = 12    # Save 12 (The number of cards in a page is 12.)

# From beginning to end of page & card within page from beginning to end
for p in range(2, total_page + 2):
    title = driver.find_elements(By.CSS_SELECTOR, '.list__item__title')
    content = driver.find_elements(By.CSS_SELECTOR, '.list__item__bot__content')
    content_num = 0
    for card in range(zero, tweleve):
        career = driver.find_elements(By.XPATH, f'//*[@id="fboardlist"]/div/div[{card + 1}]/div[1]')
        try:
            dic[d_index] = [title[card].text, career[0].text, content[content_num].text, content[content_num + 1].text, content[content_num + 2].text]
        # if card does not exist
        except:
            break
        d_index += 1
        content_num += 3
    if total_page == total_page + 1:
        break
    url = f'https://sport-strategy.org/seek_job?page={p}'
    driver.get(url)
    driver.implicitly_wait(5)
print("Crawling is over.")
print("I'll save it in Excel")
print(dic)

#### Save data to Excel
list_number = list(range(1, d_index + 1))
rows = d_index  # Total number of cards
cols = 5        # Number of columns

initialization = [[0 for c in range(cols)] for r in range(rows)]
for i in range(len(dic)):
    initialization[i] = dic[i]

df = pd.DataFrame(initialization,
                  list_number, columns=['Title', 'Career', 'employment', 'Date of Apply', 'Date of Write'])

with pd.ExcelWriter('C:/isf/crawler/excel/isf.xlsx') as writer:
    df.to_excel(writer, sheet_name='sheet1')

print("The file has been saved.")