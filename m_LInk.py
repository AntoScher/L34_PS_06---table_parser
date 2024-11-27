import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем драйвер для Chrome
driver = webdriver.Chrome()
url = "https://tomsk.hh.ru/vacancies/programmist"  # Укажите URL страницы, которую хотите парсить
driver.get(url)
time.sleep(3)  # Даем время странице загрузиться

links = driver.find_elements(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-12.magritte-link_style_accent___r-MW4_4-3-12.magritte-link_block___Lk0iO_4-3-12[href]')

parsed_data = []
for link in links:
    try:
        # Получаем текст и ссылку
        link_text = link.text
        href = link.get_dom_attribute('href')
        parsed_data.append([ href, link_text])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")

# Закрываем драйвер
driver.quit()

# Записываем данные в CSV-файл с кодировкой utf-8-sig
file_path = "C:/DEV/python/L34_PS_06---table_parser/hh.csv"  # Укажите полный путь к файлу
with open(file_path, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Ссылка', 'Текст ссылки'])
    writer.writerows(parsed_data)

print("Парсинг завершен, данные сохранены в файл hh.csv")
