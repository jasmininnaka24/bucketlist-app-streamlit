import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Bucketlist App")
# st.subheader("Set, track, and achieve your life goals — one milestone at a time.")
st.write("Set, track, and achieve your life goals — one milestone at a time.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun() 

st.text_input(label="", placeholder="Enter a new item", on_change=add_todo, key="new_todo")

st.session_state