# Функция создания елки 
def create_tree(levels):
    
    if levels == 0:
        return ["Недостаточно материала для построения елки. Введите положительное значение "]

    
    tree = []

    
    for i in range(1, levels + 1):
        if i == 1:
            
            spaces = " " * (4 * (i - 1) + (levels - 1))   
            tree.append(spaces + "  W")  
            tree.append(spaces + "  *")  
        elif i == 2:
            tree.append(" " * (levels - 1) + "@" + "*" * 5)
        else:
            # Создаем строку звезд в зависимости от уровня
            stars = "*" * (4 * (i - 1))
            # Вычисляем количество пробелов перед звездами
            spaces = " " * (levels - i)
            # четный 
            if i % 2 == 0:
                #@ перед звездами
                tree.append(spaces + "@" + stars)
            else:
                # после звезд @
                tree.append(spaces + stars + "@")

    # TTTTT
    tree.extend([" " * (levels - 1) + "TTTTT"] * 2)
    return tree

# Функция сохранения
def save_tree_to_file(tree, filename):
    with open(filename, 'w') as f:
        for line in tree:
            f.write(line + '\n')

# Функция  сохранения в файл
def save_error_message_to_file(message, filename):
    with open(filename, 'tree') as f:
        f.write(message)

# Основная функция
def main():
    # Ввести кол-во уровней
    levels = int(5)
    # Путь к файлу
    filename = r"C:\Users\Wolne\OneDrive\Desktop\елки иголки\tree,txt"

    # значение отрицательное
    if levels < 0:
        save_error_message_to_file("Елки не растут вниз. Введите пожалуйста положительное значение", filename)
        print("Файл с сообщением об ошибке успешно создан.")
    else:
        # Создаем елку
        tree = create_tree(levels)
        # Сохраняем
        save_tree_to_file(tree, filename)
       
        if tree[0] != "Недостаточно материала для построения елки. Введите положительное значение ":
            print("Файл успешно создан.")
        else:
            print(tree[0])

if __name__ == "__main__":
    main()
