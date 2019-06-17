import os
import shutil

#caminho de copia do arquivo
src = "D:/"
#diretorio alvo
target = "C:/cnc"

#lista os arquivos do diretorio
src_files = os.listdir(src)
for file_name in src_files:
 #separa a extencao do nome do arquivo
 arquivoExtencao = file_name.split(".")
 #se a extencao e igual a .pim ele copia para outro diretorio
 if(arquivoExtencao[1] == "pim"):
   full_file_name = os.path.join(src, file_name)
   shutil.copy(full_file_name, target)
