# testeBackend

# Desafio Backend - Questão 1 e 3:
Neste repositório contém a solução para as questões um e três em formato PDF.

# Desafio Backend - Questão 2: Automação de Backups

Este repositório contém a solução para a segunda questão do desafio de backend. O script `automacao.py` automatiza a gestão de arquivos em um servidor de backup.

## Funcionalidades

O script realiza as seguintes ações:

  * Lista todos os arquivos de um diretório de origem (`/home/valcann/backupsFrom`), incluindo nome, tamanho e datas de criação/modificação.
  * Salva essa listagem em um arquivo de log (`/home/valcann/backupsFrom.log`).
  * Remove arquivos do diretório de origem com mais de 3 dias de criação.
  * Copia os arquivos com 3 dias ou menos para um diretório de destino (`/home/valcann/backupsTo`).
  * Salva um log das operações de cópia em um segundo arquivo (`/home/valcann/backupsTo.log`).

## Pré-requisitos

  * **Python 3**: O script foi desenvolvido em Python 3. Para verificar sua versão, utilize `python3 --version`.
  * **Nenhuma biblioteca externa**: O script utiliza apenas módulos padrão do Python.

## Como Preparar o Ambiente

Antes de executar, siga os passos abaixo para configurar a estrutura de diretórios e os arquivos de teste.

1.  **Salve o código**
    Salve o código Python fornecido em um arquivo chamado `automacao.py`.

2.  **Crie a estrutura de diretórios**
    O script precisa que o diretório de origem exista. Execute o seguinte comando no seu terminal:

    ```bash
    mkdir -p /home/valcann/backupsFrom
    ```

3.  **Crie arquivos de teste**
    Para simular o cenário, crie arquivos recentes (que serão copiados) e arquivos antigos (que serão removidos):

    ```bash
    # Criar arquivos recentes (menos de 3 dias)
    touch /home/valcann/backupsFrom/backup_recente_1.zip
    touch /home/valcann/backupsFrom/backup_recente_2.iso

    # Criar arquivos antigos (mais de 3 dias)
    touch -d "4 days ago" /home/valcann/backupsFrom/backup_antigo_1.tar.gz
    touch -d "10 days ago" /home/valcann/backupsFrom/backup_antigo_2.db
    ```

## Como Executar

Com o ambiente preparado, execute o script com o seguinte comando:

```bash
python3 automacao.py
```

Você verá no console o status de cada operação (remoção e cópia de arquivos).

## Verificando o Resultado

Após a execução, você pode verificar se o script funcionou corretamente.

### 1\. Estrutura de Diretórios

  * **Diretório de Origem**: Os arquivos antigos (`backup_antigo_*`) devem ter sido removidos. Os arquivos recentes permanecerão.
    ```bash
    ls -l /home/valcann/backupsFrom
    ```
  * **Diretório de Destino**: Os arquivos recentes (`backup_recente_*`) devem ter sido copiados para esta pasta.
    ```bash
    ls -l /home/valcann/backupsTo
    ```

### 2\. Arquivos de Log

  * **Log de Origem**: Deve conter a lista de **todos os quatro arquivos** que existiam antes da execução.
    ```bash
    cat /home/valcann/backupsFrom.log
    ```
  * **Log de Destino**: Deve conter o registro de cópia apenas dos **dois arquivos recentes**.
    ```bash
    cat /home/valcann/backupsTo.log
    ```