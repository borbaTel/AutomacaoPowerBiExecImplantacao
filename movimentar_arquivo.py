#--------------------Importação das bibliotecas-----------------------
import time
import os
import shutil
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
#--------------------------------------------------------------------

#---------Método para formatar a data que será colocada no nome do arquivo---------
def data_formatada():
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    am_pm = 'AM' if now.hour < 12 else 'PM'
    return f'{date_str}_{am_pm}'

#----------------------------------------------------------------------------------

#------------------------Movendo arquivo de Downloads para diretório solicitado---------------------------

def movimentar_arquivo():
    #Diretório de Downloads
    downloads_dir = os.getenv('DOWNLOAD_DIR')

    #Diretório de destino
    target_dir = os.getenv('TARGET_DIR')

    # Nome do arquivo que você deseja mover
    filename_old = 'Lista Materiais - Exec Implantação.xlsx'

    # Novo nome do arquivo que você deseja mover
    filename_new = f'Materiais_Exec_Implantação_{data_formatada()}.xlsx'

    # Caminho completo do arquivo na pasta de Downloads
    source_file_old = os.path.join(downloads_dir, filename_old)

    # Verificar se o arquivo existe na pasta de Downloads
    if os.path.exists(source_file_old):
        #Renomear arquivo
        source_file_new = os.path.join(downloads_dir, filename_new)
        os.rename(source_file_old, source_file_new)

        # Mover o arquivo para o diretório de destino
        target_file = os.path.join(target_dir, filename_new)
        shutil.move(source_file_new, target_file)

        #Resposta no console que deu certo a movimentação do arquivo
        print(f'Arquivo "{filename_new}" movido para: {target_file}')
    else:
        #Resposta no console que NÃO deu certo a movimentação do arquivo
        print(f'Arquivo "{filename_old}" não encontrado na pasta de Downloads.')

#---------------------------------------------------------------------------------------------------------

