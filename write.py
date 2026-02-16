import os

# Папка, где находится сам .py файл
script_dir = os.path.dirname(os.path.abspath(__file__))

# Отсюда будем читать файлы
folder_path = script_dir

output_file = os.path.join(script_dir, "files_list.txt")

files = [
    f for f in os.listdir(folder_path)
    if os.path.isfile(os.path.join(folder_path, f))
]

with open(output_file, "w", encoding="utf-8") as f:
    for file_name in files:
        f.write(file_name + "\n")

print("Готово. Список файлов сохранён рядом со скриптом.")
