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

#Левченко. Частина б
#Додається модуль/функція обміну вмістом файлів по 20 символів у рядку
def format_text_20_chars(text):
    """Допоміжна функція: розбиває суцільний текст на рядки по 20 символів"""
    #Видаляємо наявні переноси рядків для рівномірного форматування
    clean_text = text.replace("\n", "")
    formatted_lines = []
    
    for i in range(0, len(clean_text), 20):
        formatted_lines.append(clean_text[i:i+20])
        
    return formatted_lines

def swap_files_content():
    """Частина б): Перепис TF18_1 -> TF18_2 і TF18_2 -> TF18_1 через TF18_3 (по 20 символів)"""
    f1_name, f2_name, f3_name = "TF18_1.txt", "TF18_2.txt", "TF18_3.txt"

    #1. Читаємо TF18_1 і зберігаємо у допоміжний TF18_3 (форматуючи по 20 символів)
    f1 = Open(f1_name, "r")
    f3 = Open(f3_name, "w")
    if f1 and f3:
        text1 = f1.read()
        lines20_1 = format_text_20_chars(text1)
        for line in lines20_1:
            f3.write(line + "\n")
        f1.close()
        f3.close()

    #2. Читаємо TF18_2 і записуємо у TF18_1 (форматуючи по 20 символів)
    f2 = Open(f2_name, "r")
    f1 = Open(f1_name, "w")
    if f2 and f1:
        text2 = f2.read()
        lines20_2 = format_text_20_chars(text2)
        for line in lines20_2:
            f1.write(line + "\n")
        f2.close()
        f1.close()

    #3. Читаємо TF18_3 (колишній TF18_1) і записуємо у TF18_2
    f3 = Open(f3_name, "r")
    f2 = Open(f2_name, "w")
    if f3 and f2:
        text3 = f3.read()
        f2.write(text3)
        f3.close()
        f2.close()

    print("Files swapped successfully with 20 characters per line.\n")

#Швачич. Частина в

def read_and_print_files():
    """Частина в): Читає вміст файлів TF18_1 та TF18_2 і друкує його по рядках"""
    files_to_read = ["TF18_1.txt", "TF18_2.txt"]

    for file_name in files_to_read:
        print(f"--- Content of {file_name} ---")
        f = Open(file_name, "r")
        if f:
            for line in f:
                print(line.strip())
            f.close()
            print(f"File {file_name} closed.\n")

# main
print("Step 1: Creating initial files")
create_initial_files()

print("Step 2: Swapping files content (Part B)")
swap_files_content()
