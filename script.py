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
#--------------------------------------------------------------------

#---------------------Configurações do SCRIPT------------------------

#Carregar variáveis de ambiente
load_dotenv()

# Configurações das variáveis de ambiente
report_url = os.getenv('REPORT_URL')
chrome_driver_path = os.getenv('CHROME_DRIVER_PATH')
user_data_dir = os.getenv('USER_DATA_DIR')
download_path = os.getenv('DOWNLOAD_PATH')


#Configurações adicionais para download
prefs = {
    'download.default_directory': download_path,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
}

# Configurar opções do Chrome
chrome_options = Options()
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
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
    time.sleep(60)
    
    #Clicar no botão para ir para a aba de Exec implantação
    btn_Exec_Implantacao_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration-footer-modern/div/ul/carousel/div/div[2]/li[3]/exploration-navigation-tab/div/pbi-text-label/div'
    btn_Exec_Implantacao = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, btn_Exec_Implantacao_xpath)))
    btn_Exec_Implantacao.click()
    time.sleep(10)

    #Aparecer botao que abre janela de opções do relatório
    element_to_hover_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[11]/transform/div/div[3]/div'
    element_to_hover = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, element_to_hover_xpath)))
    action = ActionChains(driver)
    action.move_to_element(element_to_hover).perform()
    time.sleep(10)

    #Clicar no botao que abre janela de opções do relatório
    btn_abrir_janela_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[11]/transform/div/visual-container-header/div/div/div/visual-container-options-menu/visual-header-item-container/div/button'
    btn_abrir_janela = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, btn_abrir_janela_xpath)))
    btn_abrir_janela.click()
    time.sleep(10)

    #Clicar no botao de Exportar dados que está na janela de opções do relatório para abrir a próxima tela
    btn_janela_exportar_xpath = '//*[@id="0"]'
    btn_janela_exportar = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, btn_janela_exportar_xpath)))
    btn_janela_exportar.click()
    time.sleep(10)

    #Clicar no botão Exportar que vai realmente exportar e fazer o download
    btn_exportar_xpath = '//*[@id="mat-mdc-dialog-0"]/div/div/export-data-dialog/mat-dialog-actions/button[1]'
    btn_exportar = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, btn_exportar_xpath)))
    btn_exportar.click()
    time.sleep(30)

    #---------------------------------------------------------------------------------------------------------
finally:

    #------Fechar navegador------
    driver.quit()
    #----------------------------

#-----Chamar método para começar a movimentar o arquivo------
movimentar_arquivo()
#------------------------------------------------------------



