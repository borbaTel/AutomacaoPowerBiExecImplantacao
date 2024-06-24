from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pickle

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

service = ChromeService(executable_path='c:/Users/40416929/Desktop/Projeto_Automatizar_exprt _powerBi/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)
try:
    # Acesse o site onde você já está logado
    driver.get('https://app.powerbi.com/reportEmbed?reportId=2a3752df-2b38-482f-97fa-e328a7405fa2&autoAuth=true&ctid=9744600e-3e04-492e-baa1-25ec245c6f10')

    time.sleep(50)

    # Imprima os cookies para verificação
    cookies = driver.get_cookies()
    print(cookies)

    # Salvar os cookies em um arquivo usando pickle
    with open('cookies.pkl', 'wb') as f:
        pickle.dump(cookies, f)

finally:
    # Fechar o navegador ao finalizar
    driver.quit()
