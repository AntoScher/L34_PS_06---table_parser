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

# Найти все элементы с указанными классами и избежать ошибки stale element
def find_elements_with_classes():
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '*')))
    for _ in range(3):  # Повторяем попытку 3 раза, чтобы избежать ошибки stale element
        for element in elements:
            try:
                class_attr = element.get_attribute('class')
                if class_attr:
                    class_names = class_attr.split()
                    if all(class_name in class_names for class_name in ['ui-GPFV8', 'qUioe', 'ProductName', 'ActiveProduct']):
                        text_content = element.text.strip()
                        if text_content:  # Удаляем элементы с пустыми значениями
                            print(f'Наименование: {text_content}')
            except StaleElementReferenceException:
                elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '*')))
                break
        else:
            break

# Вызов функции для элементов с указанными классами
find_elements_with_classes()

# Поиск новой группы элементов <span> с классами и вложенными элементами
def find_elements_with_price():
    elements = driver.find_elements(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH[data-testid="price"]')
    for element in elements:
        text_content = element.text.strip()
        if text_content:  # Удаляем элементы с пустыми значениями
            print(f'Цена: {text_content}')

# Вызов функции для элементов с классом price и вложенными элементами
find_elements_with_price()

# Найти все элементы ссылки с атрибутом href и избежать ошибки stale element
def find_elements_with_href():
    elements = driver.find_elements(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct[href]')
    for element in elements:
        try:
            href_content = element.get_attribute("href").strip()
            if href_content:  # Удаляем элементы с пустыми значениями
                print(f'Линк: {href_content}')
        except StaleElementReferenceException:
            elements = driver.find_elements(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct[href]')
            break

# Вызов функции для элементов с атрибутом href
find_elements_with_href()

# Закрываем браузер
driver.quit()
