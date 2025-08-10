"""
Числа Каталана: подробное изучение
==================================

Числа Каталана — это последовательность натуральных чисел, 
которая возникает во многих задачах комбинаторики.
"""

import math
from fractions import Fraction


def catalan_formula_factorial(n):
    """
    Вычисление n-го числа Каталана через формулу с факториалами
    C(n) = (2n)! / ((n+1)! * n!)
    """
    if n == 0:
        return 1
    return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))


def catalan_formula_binomial(n):
    """
    Вычисление n-го числа Каталана через биномиальные коэффициенты
    C(n) = (1/(n+1)) * C(2n, n)
    где C(2n, n) - биномиальный коэффициент
    """
    if n == 0:
        return 1
    return math.comb(2 * n, n) // (n + 1)


def catalan_recursive_formula(n):
    """
    Вычисление n-го числа Каталана через рекуррентную формулу
    C(0) = 1
    C(n) = sum(C(i) * C(n-1-i)) для i от 0 до n-1
    """
    if n <= 1:
        return 1
    
    # Используем мемоизацию для эффективности
    memo = [0] * (n + 1)
    memo[0] = memo[1] = 1
    
    for i in range(2, n + 1):
        for j in range(i):
            memo[i] += memo[j] * memo[i - 1 - j]
    
    return memo[n]


def catalan_dp(n):
    """
    Динамическое программирование для вычисления всех чисел Каталана до n
    """
    if n == 0:
        return [1]
    
    catalan = [0] * (n + 1)
    catalan[0] = catalan[1] = 1
    
    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]
    
    return catalan


def demonstrate_catalan_properties():
    """Демонстрация основных свойств чисел Каталана"""
    print("=" * 60)
    print("ЧИСЛА КАТАЛАНА: ОСНОВНЫЕ СВОЙСТВА")
    print("=" * 60)
    
    print("\n1. ОПРЕДЕЛЕНИЕ:")
    print("   Числа Каталана C(n) определяются как количество способов")
    print("   правильно расставить n пар скобок.")
    
    print("\n2. ФОРМУЛЫ:")
    print("   • Через факториалы: C(n) = (2n)! / ((n+1)! * n!)")
    print("   • Через биномиальные коэффициенты: C(n) = (1/(n+1)) * C(2n, n)")
    print("   • Рекуррентная: C(n) = Σ(C(i) * C(n-1-i)) для i=0..n-1")
    
    print("\n3. ПЕРВЫЕ ЧИСЛА КАТАЛАНА:")
    print("   n  |  C(n)  |  Применение")
    print("   ---|--------|--------------------------------")
    
    for i in range(8):
        cn = catalan_formula_factorial(i)
        applications = {
            0: "Пустая последовательность",
            1: "Одна пара скобок: ()",
            2: "Два способа: (()), ()()",
            3: "Пять способов скобок",
            4: "14 способов",
            5: "42 способа",
            6: "132 способа",
            7: "429 способов"
        }
        print(f"   {i}  |  {cn:4d}  |  {applications.get(i, f'{cn} способов')}")


def catalan_applications():
    """Примеры применения чисел Каталана"""
    print("\n" + "=" * 60)
    print("ПРИМЕНЕНИЯ ЧИСЕЛ КАТАЛАНА")
    print("=" * 60)
    
    applications = [
        {
            "name": "1. Правильные скобочные последовательности",
            "description": "Количество способов расставить n пар скобок",
            "example": "n=3: ((())), (()()), (())(), ()(())(), ()()()",
            "formula": "C(n)"
        },
        {
            "name": "2. Бинарные деревья",
            "description": "Количество различных бинарных деревьев с n внутренними узлами",
            "example": "n=3: 5 различных структур деревьев",
            "formula": "C(n)"
        },
        {
            "name": "3. Триангуляция многоугольника",
            "description": "Количество способов разбить выпуклый (n+2)-угольник на треугольники",
            "example": "Пятиугольник можно триангулировать 5 способами",
            "formula": "C(n)"
        },
        {
            "name": "4. Пути в решетке",
            "description": "Количество монотонных путей от (0,0) до (n,n), не пересекающих диагональ y=x",
            "example": "Пути, которые не поднимаются выше диагонали",
            "formula": "C(n)"
        },
        {
            "name": "5. Способы перемножения матриц",
            "description": "Количество способов расставить скобки при перемножении n+1 матриц",
            "example": "A*B*C*D можно вычислить ((A*B)*C)*D, (A*B)*(C*D), и т.д.",
            "formula": "C(n)"
        }
    ]
    
    for app in applications:
        print(f"\n{app['name']}")
        print(f"   Описание: {app['description']}")
        print(f"   Пример: {app['example']}")
        print(f"   Формула: {app['formula']}")


def generate_parentheses_catalan(n):
    """
    Генерация всех правильных скобочных последовательностей
    (демонстрация связи с числами Каталана)
    """
    result = []
    
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return result


def demonstrate_bracket_sequences():
    """Демонстрация скобочных последовательностей для разных n"""
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ: СКОБОЧНЫЕ ПОСЛЕДОВАТЕЛЬНОСТИ")
    print("=" * 60)
    
    for n in range(1, 5):
        sequences = generate_parentheses_catalan(n)
        catalan_n = len(sequences)
        theoretical_catalan = catalan_formula_factorial(n)
        
        print(f"\nn = {n}:")
        print(f"Число Каталана C({n}) = {theoretical_catalan}")
        print(f"Сгенерировано последовательностей: {catalan_n}")
        print(f"Совпадение: {'✓' if catalan_n == theoretical_catalan else '✗'}")
        print("Последовательности:")
        
        for i, seq in enumerate(sequences, 1):
            print(f"  {i:2d}. {seq}")


def catalan_asymptotic():
    """Асимптотическое поведение чисел Каталана"""
    print("\n" + "=" * 60)
    print("АСИМПТОТИЧЕСКОЕ ПОВЕДЕНИЕ")
    print("=" * 60)
    
    print("Асимптотическая формула для больших n:")
    print("C(n) ≈ (4^n) / (√π * n^(3/2))")
    print()
    
    print("Сравнение точного значения с асимптотикой:")
    print("n  |  C(n) точное  |  C(n) асимптотика  |  Отношение")
    print("---|---------------|--------------------|-----------")
    
    for n in range(5, 16):
        exact = catalan_formula_factorial(n)
        asymptotic = (4**n) / (math.sqrt(math.pi) * (n**(3/2)))
        ratio = exact / asymptotic if asymptotic > 0 else 0
        
        print(f"{n:2d} | {exact:11d} | {asymptotic:16.0f} | {ratio:8.4f}")


def interesting_facts():
    """Интересные факты о числах Каталана"""
    print("\n" + "=" * 60)
    print("ИНТЕРЕСНЫЕ ФАКТЫ О ЧИСЛАХ КАТАЛАНА")
    print("=" * 60)
    
    facts = [
        "• Названы в честь бельгийского математика Эжена Каталана (1814-1894)",
        "• Впервые изучены китайским математиком Мин Анту в 1730-х годах",
        "• Связаны с золотым сечением через производящую функцию",
        "• Каждое число Каталана можно выразить как разность двух биномиальных коэффициентов:",
        "  C(n) = C(2n, n) - C(2n, n+1)",
        "• Производящая функция: C(x) = (1 - √(1-4x)) / (2x)",
        "• Сумма всех чисел Каталана до бесконечности расходится",
        "• C(n) всегда целое число, хотя формула содержит деление",
        "• Рост: C(n+1) / C(n) стремится к 4 при n → ∞"
    ]
    
    for fact in facts:
        print(fact)


def main():
    """Основная функция демонстрации"""
    demonstrate_catalan_properties()
    catalan_applications()
    demonstrate_bracket_sequences()
    catalan_asymptotic()
    interesting_facts()
    
    print("\n" + "=" * 60)
    print("ИНТЕРАКТИВНАЯ ЧАСТЬ")
    print("=" * 60)
    
    while True:
        try:
            n = int(input("\nВведите n для вычисления C(n) (или 0 для выхода): "))
            if n == 0:
                break
            if n < 0:
                print("n должно быть неотрицательным!")
                continue
            if n > 20:
                print("Слишком большое n! Ограничимся n ≤ 20")
                continue
                
            # Вычисляем разными способами
            c1 = catalan_formula_factorial(n)
            c2 = catalan_formula_binomial(n)
            c3 = catalan_recursive_formula(n)
            
            print(f"\nРезультаты для n = {n}:")
            print(f"  Через факториалы:     C({n}) = {c1}")
            print(f"  Через биномиальные:   C({n}) = {c2}")
            print(f"  Через рекуррентную:   C({n}) = {c3}")
            print(f"  Все методы совпадают: {'✓' if c1 == c2 == c3 else '✗'}")
            
            # Показываем применение к скобкам для малых n
            if n <= 4:
                sequences = generate_parentheses_catalan(n)
                print(f"\nВсе {len(sequences)} скобочных последовательностей:")
                for i, seq in enumerate(sequences, 1):
                    print(f"    {i:2d}. {seq}")
                    
        except ValueError:
            print("Введите корректное число!")
        except KeyboardInterrupt:
            print("\nВыход...")
            break


if __name__ == "__main__":
    main() 

'''
Резюме: Числа Каталана
Числа Каталана — это фундаментальная последовательность в комбинаторике, которая определяет количество способов решения множества различных задач.
Основные определения:
Основная формула: C(n) = (2n)! / ((n+1)! × n!)
Альтернативная формула: C(n) = (1/(n+1)) × C(2n,n)
Рекуррентная формула: C(n) = Σ C(i) × C(n-1-i) для i=0..n-1
Первые значения:
C(0) = 1, C(1) = 1, C(2) = 2, C(3) = 5, C(4) = 14, C(5) = 42, C(6) = 132...
Главные применения:
Скобочные последовательности - количество правильных способов расставить n пар скобок
Бинарные деревья - количество различных структур с n узлами
Триангуляция - способы разбить многоугольник на треугольники
Пути в решетке - монотонные пути, не пересекающие диагональ
Матричные произведения - способы расстановки скобок при перемножении
Ключевые свойства:
Рост: асимптотически растут как 4^n / (√π × n^(3/2))
Целочисленность: всегда дают целые числа
История: названы в честь Эжена Каталана, но изучались еще в XVIII веке
Связи: связаны с биномиальными коэффициентами и золотым сечением
Практическое значение:
Числа Каталана встречаются во множестве алгоритмических задач, особенно связанных с:
Рекурсивными структурами данных
Парсингом и синтаксическим анализом
Динамическим программированием
Комбинаторной оптимизацией
Понимание чисел Каталана помогает решать широкий класс задач в программировании и математике!


'''