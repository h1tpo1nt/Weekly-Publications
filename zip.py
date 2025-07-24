import zipfile
import os

def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

folder_to_zip = './output'  # Путь к папке, которую нужно заархивировать
output_zip = 'archive.zip'   # Имя выходного ZIP-файла

zip_directory(folder_to_zip, output_zip)
print(f"Папка '{folder_to_zip}' успешно заархивирована в '{output_zip}'")
