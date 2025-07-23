import os
import shutil
from pathlib import Path

# Пути к папкам
output_folder = "output"  # локальная папка в Jupyter
base_network_path = r"\\uc.local\MSK\Files\Аналитика закрытая часть\REPORTS\1 - Raw Data\Weekly Publications"

# Словарь с правилами распределения файлов
file_rules = {
    # Fertecon файлы
    "Ammonia Market Report": [
        os.path.join(base_network_path, r"Freights\Fertecon Ammonia")
    ],
    "Sulphuric Acid Market Report": [
        os.path.join(base_network_path, r"Line-up\Fertecon Sulphuric Acid")
    ],
    "Nitrogen Market Report": [
        os.path.join(base_network_path, r"Tenders\Fertecon Nitrogen")
    ],
    "Phosphate Market Report": [
        os.path.join(base_network_path, r"Tenders\Fertecon Phosphates")
    ],
    
    # Argus файлы
    "Argus Ammonia_Russia version": [
        os.path.join(base_network_path, r"Freights\Argus Ammonia"),
        os.path.join(base_network_path, r"Line-up\Argus Ammonia")
    ],
    "Argus Nitrogen _ Russia version": [
        os.path.join(base_network_path, r"Freights\Argus Nitrogen")
    ],
    "Argus NPKs_Russia version": [
        os.path.join(base_network_path, r"Freights\Argus NPK"),
        os.path.join(base_network_path, r"Line-up\Argus NPKs")
    ],
    "Argus Phosphates_Russia version": [
        os.path.join(base_network_path, r"Freights\Argus Phosphates"),
        os.path.join(base_network_path, r"Line-up\Argus Phosphates"),
        os.path.join(base_network_path, r"Tenders\Argus Phosphates")
    ],
    "Argus Potash _Russia version": [
        os.path.join(base_network_path, r"Freights\Argus Potash"),
        os.path.join(base_network_path, r"Line-up\Argus Potash")
    ],
    
    # ICIS файлы
    "The Market-Phosphates": [
        os.path.join(base_network_path, r"Freights\ICIS Phosphates"),
        os.path.join(base_network_path, r"Line-up\ICIS Phosphates"),
        os.path.join(base_network_path, r"Tenders\ICIS Phosphates")
    ],
    "The Market-Potash": [
        os.path.join(base_network_path, r"Freights\ICIS Potash"),
        os.path.join(base_network_path, r"Line-up\ICIS Potash")
    ],
    "The Market-Sulphur": [
        os.path.join(base_network_path, r"Freights\ICIS Sulfur"),
        os.path.join(base_network_path, r"Line-up\ICIS Sulphur")
    ],
    "The Market-Urea and Nitrates": [
        os.path.join(base_network_path, r"Freights\ICIS Urea and Nitrates"),
        os.path.join(base_network_path, r"Line-up\ICIS Urea and Nitrates")
    ],
    "The Market-Ammonia": [
        os.path.join(base_network_path, r"Line-up\ICIS Ammonia")
    ],
    
    # Другие файлы
    "weekly-overview": [
        os.path.join(base_network_path, r"Freights\CRU")
    ],
    "ProfercyAmmonia": [
        os.path.join(base_network_path, r"Line-up\ProfercyAmmonia")
    ]
}

def copy_files_by_rules():
    """Копирует файлы из папки output по сетевым папкам согласно правилам"""
    
    # Проверяем существование папки output
    if not os.path.exists(output_folder):
        print(f"Папка {output_folder} не найдена!")
        return
    
    # Получаем список всех файлов в папке output
    files = os.listdir(output_folder)
    print(f"Найдено файлов: {len(files)}")
    
    processed_count = 0
    
    # Обрабатываем каждый файл
    for filename in files:
        file_path = os.path.join(output_folder, filename)
        
        # Пропускаем папки
        if os.path.isdir(file_path):
            continue
            
        # Ищем совпадение по правилам
        matched = False
        for pattern, target_folders in file_rules.items():
            if pattern.lower() in filename.lower():
                matched = True
                print(f"Обработка файла: {filename}")
                
                # Создаем целевые папки и копируем файл
                for target_folder in target_folders:
                    try:
                        # Создаем папку если не существует
                        os.makedirs(target_folder, exist_ok=True)
                        
                        # Копируем файл
                        target_path = os.path.join(target_folder, filename)
                        shutil.copy2(file_path, target_path)
                        print(f"  → Скопирован в: {target_folder}")
                        
                    except Exception as e:
                        print(f"  ❌ Ошибка при копировании в {target_folder}: {e}")
                
                processed_count += 1
                break
        
        if not matched:
            print(f"⚠️  Файл не соответствует ни одному правилу: {filename}")
    
    print(f"\n✅ Обработано файлов: {processed_count}")

# Запуск функции
copy_files_by_rules()
