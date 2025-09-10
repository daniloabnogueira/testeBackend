import os
import shutil
import logging
import datetime

# Variáveis de caminhos e tempo de retenção
FONTE_DIR = "/home/valcann/backupsFrom"
DESTINO_DIR = "/home/valcann/bavkupsTo"
LOG_FROM_PATH = "/home/valcann/backupsFrom.log"
LOG_TO_PATH = "/home/valcann/backupsTo.log"
DIAS_RETENCAO = 3

def setup_logger(nome, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.addHandler(handler)


    logger = logging.getLogger(nome)
    logger.setLevel(level)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger


def gerir_backups():
    os.makedirs(DESTINO_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(LOG_FROM_PATH), exist_ok=True)

    from_logger = setup_logger('backupsFromLogger', LOG_FROM_PATH)
    to_logger = setup_logger('backupsToLogger', LOG_TO_PATH)


    retention_limit_time = datetime.datetime.now() - datetime.timedelta(days=DIAS_RETENCAO)

    print("Analisando arquivos em: {FONTE_DIR}")

    try:
        if not os.path.isdir(FONTE_DIR):
            print("Erro: Diretório de origem '{FONTE_DIR}' não encontrado.")
            from_logger.error("Diretório de origem '{FONTE_DIR}' não encontrado.")
            return
        for filename in os.listdir(FONTE_DIR):
            source_file_path = os.path.join(FONTE_DIR, filename)

            if os.path.isfile(source_file_path):
                try:
                    stat = os.stat(source_file_path)
                    creation_time_ts = os.path.getctime(source_file_path)
                    creation_time = datetime.datetime.fromtimestamp(creation_time_ts)
                    modification_time = datetime.datetime.fromtimestamp(stat.st_mtime)
                    file_size = stat.st_size

                    log_message = (
                        f"Arquivo: {filename}, "
                        f"Tamanho: {file_size} bytes, "
                        f"Criação: {creation_time.strftime('%Y-%m-%d %H:%M:%S')}, "
                        f"Modificação: {modification_time.strftime('%Y-%m-%d %H:%M:%S')}"
                    )
                    from_logger.info(log_message)

                    if creation_time <= retention_limit_time:
                        os.remove(source_file_path)
                        print(f"Removido arquivo antigo: {filename}")
                    else:
                        dest_file_path = os.path.join(DESTINO_DIR, filename)
                        shutil.copy2(source_file_path, dest_file_path)

                        to_logger.info(f"Arquivo '{filename}' copiado para '{DESTINO_DIR}'.")
                        print(f"Copiado arquivo recente: {filename}")
                
                except OSError as e:
                    error_msg = f"Erro ao processar o arquivo {filename}: {e}"
                    print(error_msg)
                    from_logger.error(error_msg)
                    to_logger.error(error_msg)
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        print("Processo de gerenciamento de backups concluído.")
        print(f"Lod de origem salvo em: {LOG_FROM_PATH}")
        print(f"Log de destino salvo em: {LOG_TO_PATH}")

if __name__ == "__main__":
    gerir_backups()





