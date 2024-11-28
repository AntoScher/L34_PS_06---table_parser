from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

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


# Найти все карточки товаров
def find_product_cards():
    return wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.LlPhw')))


product_cards = find_product_cards()

print("Наименование:\t\tЦена:\t\tЛинк:")

for card in product_cards:
    try:
        name_element = card.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct')
        price_element = card.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH[data-testid="price"]')
        link_element = card.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct[href]')

        name = name_element.text.strip()
        price = price_element.text.strip()
        link = link_element.get_attribute("href").strip()

        if name and price and link:
            print(f'{name}\t{price}\t{link}')
    except NoSuchElementException:
        # Пропускаем карточки, в которых не найдены элементы
        continue
    except StaleElementReferenceException:
        # Переполучаем список карточек в случае устаревшего элемента
        product_cards = find_product_cards()
        break

# Закрываем браузер
driver.quit()
