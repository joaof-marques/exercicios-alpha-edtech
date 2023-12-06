import zipfile
import os
import sys

def zipar_arquivos(diretorio):
    # Listar os arquivos .py no diretório
    arquivos = [f for f in os.listdir(diretorio) if f.endswith('.py')]
    
    # Excluir todos os arquivos .zip existentes no diretório
    arquivos_zip_existente = [f for f in os.listdir(diretorio) if f.endswith('.zip')]
    for arquivo_zip in arquivos_zip_existente:
        caminho_arquivo_zip = os.path.join(diretorio, arquivo_zip)
        os.remove(caminho_arquivo_zip)

    # Para cada arquivo .py, criar um arquivo zip com o mesmo nome
    for arquivo in arquivos:
        nome_arquivo = os.path.splitext(arquivo)[0]  # Remove a extensão .py
        arquivo_zip = nome_arquivo + '.zip'
        
        with zipfile.ZipFile(arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.write(os.path.join(diretorio, arquivo), arquivo)

    print("Arquivos zipados com sucesso!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 ziparArquivos.py <diretorio>")
        sys.exit(1)

    diretorio = sys.argv[1]
    print(diretorio)
    zipar_arquivos(diretorio)

