def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
        todos = [todo.strip() for todo in todos]
    return todos


def add_todos(todos_args, filepath="todos.txt"):
    with open(filepath, 'w') as file_local:
        file_local.writelines('\n'.join(todos_args))

if __name__ == "__main__":
    print(get_todos())