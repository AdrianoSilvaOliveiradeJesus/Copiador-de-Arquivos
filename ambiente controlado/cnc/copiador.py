import os
import shutil

src = os.getcwd()
print(src)

src_files = os.listdir(src)
print(src_files)
for file_name in src_files:
 full_file_name = os.path.join(src, file_name)
 if os.path.isfile(full_file_name):
    shutil.copy(full_file_name, "/home/metalzilo/Área de Trabalho/Copiador-de-Arquivos/ambiente controlado/cnc")
