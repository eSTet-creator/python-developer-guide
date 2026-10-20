# Консольний довідник з Python

def show_menu():
    print("=== Довідник Python ===")
    print("1. Показати поради")
    print("0. Вихід")

def get_list_tips():
    return [
        "Створення списку: my_list = [1, 2, 3]",
        "Додавання елемента: my_list.append(4)"
    ]

print('YA SHARU')

if __name__ == "__main__":
    show_menu()