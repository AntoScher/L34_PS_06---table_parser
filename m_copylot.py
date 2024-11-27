import time
import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from main_zer import company

# Создаем драйвер для Chrome
driver = webdriver.Chrome()
url = "https://tomsk.hh.ru/vacancies/programmist"  # Укажите URL страницы, которую хотите парсить
driver.get(url)
time.sleep(3)  # Даем время странице загрузиться

vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.vacancy-info--umZA61PpMY07JVJtomBA')
soup = BeautifulSoup(url, 'html.parser')
spans = soup.find_all('span', {'data-qa': 'vacancy-serp__vacancy-employer-text'})

parsed_data = []
for vacancy in vacancies:
    try:
        links = driver.find_elements(By.CSS_SELECTOR,
                                     'a.magritte-link___b4rEM_4-3-12.magritte-link_style_accent___r-MW4_4-3-12.magritte-link_block___Lk0iO_4-3-12[href]')

        title = driver.find_element(By.CSS_SELECTOR, 'a.magritte-text_typography-title-4-semibold___vUqki_3-0-18').text
        #company=spans
       # company = driver.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text"]').text
        salary = driver.find_element(By.CSS_SELECTOR, 'span.compensation-labels--cR9OD8ZegWd3f7Mzxe6z').text
        parsed_data.append([title, company, salary, links])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")

# Закрываем драйвер
driver.quit()

# Записываем данные в CSV-файл с кодировкой utf-8-sig
#file_path = "C:/DEV/python/L34_PS_06---table_parser/hh.csv"  # Укажите полный путь к файлу
with open("hh.csv", 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Классы', 'Ссылка', 'Текст ссылки'])
    writer.writerows(parsed_data)

print("Парсинг завершен, данные сохранены в файл hh.csv")
