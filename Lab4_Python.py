def Open(file_name, mode):
    """Безпечне відкриття файлу з обробкою винятків try-except"""
    try:
        file = open(file_name, mode, encoding='utf-8')
    except Exception as e:
        print(f"File {file_name} wasn't opened! Error: {e}")
        return None
    else:
        print(f"File {file_name} was opened!")
        return file

def create_initial_files():
    """Частина а): Створення файлів TF18_1 та TF18_2 із рядків різної довжини"""
    file1_name = "TF18_1.txt"
    file2_name = "TF18_2.txt"

    # Тексти з рядками різної довжини
    lines_1 = [
        "First file line 1 - length ok.",
        "Short.",
        "This is a longer sentence for the first file to test line lengths."
    ]
    
    lines_2 = [
        "Second file initial text.",
        "Another random string here.",
        "Python file processing task variant 15."
    ]

    # Запис у перший файл
    f1 = Open(file1_name, "w")
    if f1:
        for line in lines_1:
            f1.write(line + "\n")
        f1.close()
        print(f"File {file1_name} created successfully.\n")

    # Запис у другий файл
    f2 = Open(file2_name, "w")
    if f2:
        for line in lines_2:
            f2.write(line + "\n")
        f2.close()
        print(f"File {file2_name} created successfully.\n")

# main
print("Step 1: Creating initial files")
create_initial_files()
