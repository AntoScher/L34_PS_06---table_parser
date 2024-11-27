import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем драйвер для Chrome
driver = webdriver.Chrome()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)
time.sleep(3)

vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.vacancy-info--umZA61PpMY07JVJtomBA')

parsed_data = []
for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-2').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-12.magritte-link_style_accent___r-MW4_4-3-12.magritte-link_block___Lk0iO_4-3-12[href]').get_attribute('href')
        company = vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text"]').text

        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-labels--cR9OD8ZegWd3f7Mzxe6z').text
        except:
            salary = "Не указана"

        parsed_data.append([title, company, salary, link])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")

# Закрываем драйвер
driver.quit()

# Записываем данные в CSV-файл
with open("hh.csv", 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)
