import os

def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")
    note = {"title": title, "content": content}
    return note

def save_note(note):
    with open("notes.txt", "a") as file:
        file.write(note["title"] + "\n")
        file.write(note["content"] + "\n")
        file.write("---\n")

def delete_note():
    if not os.path.exists("notes.txt"):
        print("У вас пока нет заметок для удаления.")
        return
    title_to_delete = input("Введите заголовок заметки, которую хотите удалить: ")
    with open("notes.txt", "r") as file:
        notes = file.read().split("---\n")
    found = False
    for i, note in enumerate(notes):
        if note.strip():
            title, content = note.split("\n", 1)
            if title == title_to_delete:
                found = True
                del notes[i]
                with open("notes.txt", "w") as file:
                    file.write("---\n".join(notes))
                print("Заметка успешно удалена.")
                break
    if not found:
        print("Заметка с указанным заголовком не найдена.")

def main():
    while True:
        print("\nМеню:")
        print("1. Создать новую заметку")
        print("2. Посмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == "1":
            note = create_note()
            save_note(note)
            print("Заметка успешно сохранена.")
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
