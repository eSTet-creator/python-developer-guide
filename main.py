# Консольний довідник з Python

def show_menu():
    print("\n=== Довідник Python ===")
    print("1. Показати поради щодо списків")
    print("2. Показати поради щодо словників")
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

        elif choice == "0":
            print("Вихід з програми. До зустрічі!")
            break  # Зупиняє нескінченний цикл

        else:
            print("❌ Невірний вибір. Будь ласка, введіть 1, 2 або 0.")



print('YA SHARU')
# Створення словника
user = {"name": "Олена", "age": 25, "city": "Київ"}

# Отримання значення за ключем
print(user["name"])  # Виведе: Олена

# Безпечне отримання (якщо ключа немає, поверне None замість помилки)
print(user.get("email"))  # Виведе: None
if __name__ == "__main__":
    main()


