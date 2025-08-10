def generate_parentheses(n):
    """
    Генерирует все правильные скобочные последовательности длины 2*n
    в лексикографическом порядке.
    
    Args:
        n (int): количество пар скобок
    
    Returns:
        list: список всех правильных скобочных последовательностей
    """
    result = []
    
    def backtrack(current_string, open_count, close_count):
        """
        Рекурсивная функция для генерации последовательностей
        
        Args:
            current_string (str): текущая строка
            open_count (int): количество открывающих скобок в текущей строке
            close_count (int): количество закрывающих скобок в текущей строке
        """
        # Базовый случай: достигли нужной длины
        if len(current_string) == 2 * n:
            result.append(current_string)
            return
        
        # Добавляем открывающую скобку, если можем
        if open_count < n:
            backtrack(current_string + "(", open_count + 1, close_count)
        
        # Добавляем закрывающую скобку, если можем
        if close_count < open_count:
            backtrack(current_string + ")", open_count, close_count + 1)
    
    # Начинаем рекурсию с пустой строки
    backtrack("", 0, 0)
    return result


def main():
    """Основная функция для демонстрации работы алгоритма"""
    print("Генератор правильных скобочных последовательностей")
    print("=" * 50)
    
    # Читаем входные данные
    try:
        n = int(input("Введите n (количество пар скобок): "))
        if n <= 0:
            print("n должно быть положительным числом!")
            return
    except ValueError:
        print("Некорректный ввод! Введите целое число.")
        return
    
    # Генерируем последовательности
    sequences = generate_parentheses(n)
    
    # Выводим результат
    print(f"\nВсе правильные скобочные последовательности для n = {n}:")
    print(f"Количество последовательностей: {len(sequences)}")
    print()
    
    for i, seq in enumerate(sequences, 1):
        print(f"{i:2d}. {seq}")


def test_algorithm():
    """Функция для тестирования алгоритма"""
    print("\nТестирование алгоритма:")
    print("-" * 30)
    
    test_cases = [1, 2, 3, 4]
    
    for n in test_cases:
        sequences = generate_parentheses(n)
        print(f"n = {n}: {len(sequences)} последовательностей")
        for seq in sequences:
            print(f"  {seq}")
        print()


def mathematical_note():
    """Математическая справка о числах Каталана"""
    print("\nМатематическая справка:")
    print("-" * 30)
    print("Количество правильных скобочных последовательностей")
    print("для n пар скобок равно n-му числу Каталана:")
    print("C(n) = (2n)! / ((n+1)! * n!)")
    print()
    
    # Вычисляем первые несколько чисел Каталана
    def catalan_number(n):
        if n <= 1:
            return 1
        catalan = [0] * (n + 1)
        catalan[0], catalan[1] = 1, 1
        
        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - 1 - j]
        return catalan[n]
    
    print("Первые числа Каталана:")
    for i in range(1, 8):
        print(f"C({i}) = {catalan_number(i)}")


if __name__ == "__main__":
    # Демонстрация работы
    main()
    
    # Тестирование
    test_algorithm()
    
    # Математическая справка
    mathematical_note() 