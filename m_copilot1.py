import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Создаем драйвер для Chrome
driver = webdriver.Chrome()
url = "https://tomsk.hh.ru/vacancies/programmist"  # Укажите URL страницы, которую хотите парсить
driver.get(url)
time.sleep(3)  # Даем время странице загрузиться

# Получаем содержимое страницы
page_source = driver.page_source

# Закрываем драйвер
driver.quit()

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(page_source, 'html.parser')

# Находим все элементы <span> с указанным атрибутом data-qa
spans = soup.find_all('span', {'data-qa': 'vacancy-serp__vacancy-employer-text'})

parsed_data = []
for span in spans:
    class_list = span.get('class', [])
    for class_name in class_list:
        if 'magritte-text___tkzIl_4-3-12' in class_name:
            text_content = span.get_text(strip=True)
            parsed_data.append([ text_content])

# Проверяем, собраны ли данные
if not parsed_data:
    print("Данные не найдены или не соответствуют условиям")

# Добавляем нумерацию строк и форматируем данные
formatted_data = [[index + 1] + row for index, row in enumerate(parsed_data)]

# Записываем данные в CSV-файл с кодировкой utf-8-sig
file_path = "C:/DEV/python/L34_PS_06---table_parser/hh.csv"  # Укажите полный путь к файлу
with open(file_path, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Номер', 'Текст'])
    writer.writerows(formatted_data)

print("Парсинг завершен, данные сохранены в файл hh.csv")
