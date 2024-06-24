#--------------------Importação das bibliotecas-----------------------
from movimentar_arquivo import movimentar_arquivo
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import shutil
import pickle
#--------------------------------------------------------------------

#---------------------Configurações do SCRIPT------------------------

#Carregar variáveis de ambiente
load_dotenv()

# Configurações das variáveis de ambiente
report_url = os.getenv('REPORT_URL')
chrome_driver_path = os.getenv('CHROME_DRIVER_PATH')
user_data_dir = os.getenv('USER_DATA_DIR')
download_path = os.getenv('DOWNLOAD_PATH')
cookies_file = 'cookies.pkl'


#Configurações adicionais para download
prefs = {
    'download.default_directory': download_path,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
}

# Configurar opções do Chrome
chrome_options = Options()
#chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option('prefs', prefs)


#Inicializar instancia de navegação
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

#-------------------------------------------------------------------

try:
    #-----------------Começo dos passos para acessar power bi e fazer o download do arquivo-------------------

    #Carregar a URL do Power Bi
    driver.get(report_url)
    
    with open(cookies_file, 'rb') as f:
        cookies = pickle.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    
    driver.get(report_url)

    time.sleep(1000)
    #---------------------------------------------------------------------------------------------------------
finally:

    #------Fechar navegador------
    driver.quit()
    #----------------------------




