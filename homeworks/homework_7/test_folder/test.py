# Введите ваше решение ниже
# with open("__init__.py", "w") as file:
#     file.write("__all__ = ['rename_files']")
#     # file.write("    # Здесь код функции\n")
#
# # Проверка содержимого файла
# with open("__init__.py", "r") as file:
#     print(file.read())
with open("__init__.py", "w") as file:
    file.write("def rename_files():\n    pass")
    # file.write("    pass\n")

# Проверка содержимого файла
with open("__init__.py", "r") as file:
    print(file.read())
