# Консольний довідник з Python
import os
import random  # Імпортуємо модуль для випадкового вибору

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        # Безпечний код очищення без сторонніх літер
        print("\033[H\033[J", end="")

def show_menu():
    print("\n=== Довідник Python ===")
    print("1. Показати поради щодо списків")
    print("2. Показати поради щодо словників")
    print("3. Показати поради щодо рядків")
    print("4. Очистити екран")
    print("0. Вихід")

def get_list_tips():
    return [
        "Створення списку: my_list = [1, 2, 3]",
        "Додавання елемента: my_list.append(4)",
        "Вставка за індексом: my_list.insert(0, 'новий')"  # Додано новий рядок
    ]

def get_dict_tips():
    return [
        "Створення словника: my_dict = {'key': 'value'}",
        "Безпечне отримання елемента: my_dict.get('key')",
        "Оновлення або додавання: my_dict.update({'new_key': 5})"  # Додано новий рядок
    ]

def get_string_tips():
    return [
        "Форматування рядків (f-strings): f'Привіт, {name}!'",
        "Зміна регістру: text.lower(), text.upper(), text.title()",
        "Пошук підрядка: 'python' in text або text.find('th')"
    ]

# Нова супер-проста функція
def get_goodbye_message():
    phrases = [
        "Успіхів у програмуванні! 🚀",
        "Код сам себе не напише, повертайтеся швидше! 💻",
        "Гарного дня та чистих логів! ✨",
        "Пам'ятайте: Zen of Python — це шлях! 🧘"
    ]
    return random.choice(phrases)  # Повертає одну випадкову фразу з переліку

def main():
    while True:
        show_menu()
        choice = input("Оберіть номер пункту: ")
        if choice == "1":
            print("\n--- Поради щодо списків ---")
            for tip in get_list_tips():
                print(f"• {tip}")
        elif choice == "2":
            print("\n--- Поради щодо словників ---")
            for tip in get_dict_tips():
                print(f"• {tip}")
        elif choice == "3":
            print("\n--- Поради щодо рядків ---")
            for tip in get_string_tips():
                print(f"• {tip}")
        elif choice == "4":
            clear_screen()
        elif choice == "0":
            # Викликаємо нову функцію під час виходу
            print(f"\n{get_goodbye_message()}")
            break # Зупиняє нескінченний цикл
        else:
            print("❌ Невірний вибір. Будь ласка, введіть 1, 2, 3, 4 або 0.")

if __name__ == "__main__":
    main()

