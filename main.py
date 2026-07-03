import fire
import os

# class ToDos:
def add(todo):
       
       with open("todo.txt", "a") as file:
            file.write(todo + '\n')
            print(f"{todo} added  on your list")

def list():
        with open('todo.txt', 'r') as file:
              todo = file.readlines()
              print(todo)

def remove(erase):
    todos = []
    with open ('todo.txt', 'r') as file:
         todos = file.readlines()
      
    print(todos)

    todos.remove(erase + "\n")
    with open ('todo.txt', 'w') as file:
         for item in todos:
            file.write(item)
       

       
    
if __name__ == '__main__':
  fire.Fire()