import os

script_dir = os.path.dirname(os.path.abspath(__file__))
items = os.listdir(script_dir)

with open("files_list.txt", "w", encoding="utf-8") as f:
    for item in items:
        full_path = os.path.join(script_dir, item)
        if os.path.isdir(full_path):
            f.write(f"[DIR] {item}\n")
        else:
            f.write(f"[FILE] {item}\n")

print("Готово.")
input("")