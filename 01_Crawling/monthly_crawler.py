#이름, 시작 연월, 종료 연월 입력하여 월별로 크롤링하는 코드.

from selenium import webdriver
from urllib.parse import quote_plus
from urllib.request import urlopen
import os
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta


def save_images(images, save_path, year, month_str):
    for index, image in enumerate(images[:500]):
        src = image.get_attribute('src')
        t = urlopen(src).read()
        file_name = f"{year}{month_str}_{index + 1}.jpg"
        file = open(os.path.join(save_path, file_name), "wb")
        file.write(t)
        print("img save " + os.path.join(save_path, file_name))


def create_folder_if_not_exists(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def make_url(search_term, year, month):
    base_url = 'https://search.naver.com/search.naver?where=image&section=image&query='
    date_url = f'&res_fr=0&res_to=0&sm=tab_opt&color=&ccl=0&nso=so%3Ar%2Cp%3Afrom{year}{month}01to{year}{month}31' \
               f'&recent=0&datetype=6&startdate={year}.{month}.01&enddate={year}.{month}.31&gif=0&optStr=d&nso_open=1'
    return base_url + quote_plus(search_term) + date_url


def crawl_images(search_term, start_year, start_month, end_year, end_month):
    start_date = datetime(start_year, start_month, 1)
    end_date = datetime(end_year, end_month, 1)

    while start_date <= end_date:
        year = start_date.year
        month = start_date.month
        month_str = str(month).zfill(2)

        # URL 생성
        url = make_url(search_term, year, month_str)

        # Chrome 브라우저 열기
        browser = webdriver.Chrome('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
        browser.implicitly_wait(3)
        browser.get(url)

        # Scroll down to load more images
        time.sleep(5)
        for _ in range(30):
            browser.execute_script("window.scrollBy(0,1000)")
            time.sleep(1)

        # 이미지 긁어오기
        images = browser.find_elements(By.CLASS_NAME, "_image")

        # 저장 폴더 생성
        save_folder = f"C:/{search_term}/{year}-{month_str}/"
        create_folder_if_not_exists(save_folder)

        # 이미지 저장
        save_images(images, save_folder, year, month_str)

        # 마무리
        print(search_term + f" {year}-{month_str} 저장 성공")
        browser.close()

        # 다음 달로 이동
        start_date = start_date + timedelta(days=31)
        start_date = start_date.replace(day=1)


if __name__ == '__main__':
    search_term = input('원하는 검색어: ')
    start_year = int(input('시작 년도를 입력하세요: '))
    start_month = int(input('시작 월을 입력하세요: '))
    end_year = int(input('종료 년도를 입력하세요: '))
    end_month = int(input('종료 월을 입력하세요: '))

    crawl_images(search_term, start_year, start_month, end_year, end_month)
