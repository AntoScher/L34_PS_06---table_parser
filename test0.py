from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# Устанавливаем опции для браузера
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме (без графического интерфейса)

# Путь к драйверу ChromeDriver
chromedriver_path = 'C:\\Users\\lsche\\.cache\\selenium\\chromedriver\\win64\\131.0.6778.85\\chromedriver.exe'

# Инициализируем браузер
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Открываем веб-страницу
driver.get('https://www.divan.ru/category/svet')

# Ожидаем загрузку всех элементов
wait = WebDriverWait(driver, 10)

# Найти все элементы, принадлежащие заданному классу
def find_elements():
    return wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '*')))

elements = find_elements()
parsed_data = []

for _ in range(3):  # Повторяем попытку 3 раза, чтобы избежать ошибки stale element
    for element in elements:
        try:
            class_attr = element.get_attribute('class')
            if class_attr:
                class_names = class_attr.split()
                if all(class_name in class_names for class_name in ['ui-GPFV8', 'qUioe', 'ProductName', 'ActiveProduct']):
                    print(f' Текст: {element.text.strip()}')
        except StaleElementReferenceException:
            elements = find_elements()
            break
    else:
        break

# Закрываем браузер
driver.quit()
