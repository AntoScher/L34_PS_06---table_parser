import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем драйвер для Chrome
driver = webdriver.Chrome()
url = "https://tomsk.hh.ru/vacancies/programmist"  # Укажите URL страницы, которую хотите парсить
driver.get(url)
time.sleep(3)  # Даем время странице загрузиться

# Находим все карточки вакансий
vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.vacancy-info--umZA61PpMY07JVJtomBA')
print(f"Найдено вакансий: {len(vacancies)}")  # Отладочная информация

parsed_data = []

# Собираем данные из каждой карточки вакансии
for vacancy in vacancies:
    try:
        title_element = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-12')
        link = title_element.get_attribute('href')
        company = vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text"]').text
        parsed_data.append([link, company])
        print(f"Добавлена вакансия: {link} - {company}")  # Отладочная информация
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")

# Закрываем драйвер
driver.quit()

# Добавляем нумерацию строк и форматируем данные
formatted_data = [[index + 1] + row for index, row in enumerate(parsed_data)]

# Записываем данные в CSV-файл с кодировкой utf-8-sig
file_path = "C:/DEV/python/L34_PS_06---table_parser/hh.csv"  # Укажите полный путь к файлу
with open(file_path, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Номер', 'Ссылка', 'Компания'])
    writer.writerows(formatted_data)

print("Парсинг завершен, данные сохранены в файл hh.csv")
