from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def initialConfigurations(start_maximized=True, headless=False):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    if start_maximized and not headless:
        driver.maximize_window()
    return driver


if __name__ == '__main__':
    driver = initialConfigurations()

    driver.get("https://duckduckgo.com/")

    wait = WebDriverWait(driver, 10)
    search = wait.until(EC.presence_of_element_located((By.NAME, "q")))

    query = 'vaga desenvolvedor júnior home office site:linkedin.com OR site:gupy.io OR site:remotar.com.br OR site:glassdoor.com.br'
    search.send_keys(query)
    search.send_keys(Keys.RETURN)

    # Espera o primeiro bloco de resultados
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-testid='result-title-a']")))

    # Loop para carregar mais resultados
    # Loop para carregar mais resultados
for _ in range(3):  # ou mais vezes, se quiser
    try:
        # Rola até o fim da página
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Espera o botão de mais resultados pelo ID e clica
        more_btn = wait.until(EC.element_to_be_clickable((By.ID, "more-results")))
        more_btn.click()
        time.sleep(3)  # dá um tempo para novos resultados aparecerem
    except:
        print("Botão de mais resultados não encontrado ou fim da lista.")
        break

    # Coleta todos os resultados visíveis na página
    results = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='result-title-a']")

    print("\nTítulos e links encontrados:")
    for result in results:
        title = result.text.strip()
        link = result.get_attribute("href")
        if title and link:
            print(f"- {title}")
            print(f"  ↪ {link}\n")

    time.sleep(2)
    driver.quit()