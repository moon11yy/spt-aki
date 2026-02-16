FILES_LIST = "files_list.txt"
KEEPING_ITEMS = "keepingitems.txt"

# читаем список строк, которые нужно удалить
with open(KEEPING_ITEMS, "r", encoding="utf-8") as f:
    items_to_remove = {
        line.strip() for line in f if line.strip()
    }

# читаем основной файл
with open(FILES_LIST, "r", encoding="utf-8") as f:
    lines = f.readlines()

# фильтруем строки
filtered_lines = [
    line for line in lines
    if line.strip() not in items_to_remove
]

# перезаписываем файл
with open(FILES_LIST, "w", encoding="utf-8") as f:
    f.writelines(filtered_lines)

print("Готово. Строки из keepingitems.txt удалены из files_list.txt")
input("\nНажми Enter для выхода...")
