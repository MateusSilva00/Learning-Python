import os
import shutil

originalPath = "media/mateus/Externo/serie"
newPath = "media/mateus/Externo/serie2"

try:
    os.mkdir(newPath)
except FileExistsError as e:
    print(f'Pasta {newPath} já exoste')


for root, dirs, files in os.walk(newPath):
    for file in files:
        oldFilePath = os.path.join(root, file)
        newFilePath = os.path.join(newPath, file)

        shutil.move(oldFilePath, newPath)
        print(f'Arquivo {file} movido com sucesso')