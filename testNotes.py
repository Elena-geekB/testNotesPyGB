import json
import os
from datetime import datetime

def generate_id():
    return datetime.now().strftime("%Y%m%d%H%M%S%f")

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите содержание заметки: ")
    note_id = generate_id()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": note_id, "title": title, "body": body, "timestamp": timestamp}
    save_note(note)
    print("Заметка успешно добавлена.")

def save_note(note):
    if not os.path.exists("notes.json"):
        with open("notes.json", "w") as file:
            json.dump([], file)
    with open("notes.json", "r+") as file:
        data = json.load(file)
        data.append(note)
        file.seek(0)
        json.dump(data, file, indent=4)

def read_notes():
    if not os.path.exists("notes.json"):
        print("У вас пока нет заметок.")
        return
    with open("notes.json", "r") as file:
        notes = json.load(file)
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Содержание: {note['body']}")
            print(f"Дата/время создания: {note['timestamp']}")
            print("---")

def edit_note():
    note_id = input("Введите ID заметки, которую хотите отредактировать: ")
    with open("notes.json", "r+") as file:
        data = json.load(file)
        for note in data:
            if note['id'] == note_id:
                new_title = input("Введите новый заголовок заметки: ")
                new_body = input("Введите новое содержание заметки: ")
                note['title'] = new_title
                note['body'] = new_body
                note['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.seek(0)
                json.dump(data, file, indent=4)
                print("Заметка успешно отредактирована.")
                return
        print("Заметка с указанным ID не найдена.")

def delete_note():
    note_id = input("Введите ID заметки, которую хотите удалить: ")
    with open("notes.json", "r+") as file:
        data = json.load(file)
        for i, note in enumerate(data):
            if note['id'] == note_id:
                del data[i]
                file.seek(0)
                json.dump(data, file, indent=4)
                print("Заметка успешно удалена.")
                return
        print("Заметка с указанным ID не найдена.")

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить новую заметку")
        print("2. Просмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
