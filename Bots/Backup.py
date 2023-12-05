import os
import shutil
from datetime import datetime

def fazer_backup(origem, destino):
    data_atual = datetime.now().strftime("%d-%m-%Y_%H%M%S")
    destino_backup = os.path.join(destino, f"backup_{data_atual}")

    try:
        os.makedirs(destino_backup)

        for root, dirs, files in os.walk(origem):
            rel_path = os.path.relpath(root, origem)
            destino_relativo = os.path.join(destino_backup, rel_path)

            if not os.path.exists(destino_relativo):
                os.makedirs(destino_relativo)

            for file in files:
                origem_arquivo = os.path.join(root, file)
                destino_arquivo = os.path.join(destino_relativo, file)
                shutil.copy2(origem_arquivo, destino_arquivo)

        print("Backup concluído com sucesso!")

    except Exception as e:
        print(f"Erro durante o backup: {e}")

# Exemplo de uso
pasta_origem = "/home/joaobreno/Documentos/Introdução a Automações"
pasta_destino = "/run/media/joaobreno/Backup/Backup"

fazer_backup(pasta_origem, pasta_destino)


# Podemos converter esse programa em um executalvel com os seguintes comandos:
# pip install pyinstaller
# pyinstaller --onefile Backup.py
# O executavel será criado na pasta dist