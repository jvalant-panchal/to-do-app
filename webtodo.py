import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["todo_new"] + "\n"
    todos.append(todo)
    functions.add_todos(todos)


st.title("My Todo app:")
st.write("This app is to Increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.add_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add new To-Do', on_change=add_todo, key="todo_new")
print("hello")

st.session_state
