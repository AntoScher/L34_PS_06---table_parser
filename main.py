import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Устанавливаем опции для браузера
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме (без графического интерфейса)

# Путь к драйверу ChromeDriver
chromedriver_path = 'C:\\Users\\lsche\\.cache\\selenium\\chromedriver\\win64\\131.0.6778.85\\chromedriver.exe'


# Инициализируем браузер
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.divan.ru/category/svet"
driver.get(url)
time.sleep(3)

vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.Pk6w8.F15NT')

parsed_data = []
for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct').text
        price = vacancy.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH[data-testid="price"]').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct[href]').get_attribute('href')
        parsed_data.append([title, price, link])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        # Если произошла ошибка, переходим к следующему элементу
        continue

# Закрываем драйвер
driver.quit()

# Записываем данные в CSV-файл
with open("hh.csv", 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка на товар'])
    writer.writerows(parsed_data)
