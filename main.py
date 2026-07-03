import fire
import os

# class ToDos:
def add(todo):

     existing = []
     with open ('todo.txt', 'r') as file:
          existing = file.readlines()
     
      
     
     if (todo + "\n") in existing:
          print("Already added")
     else:
           with open("todo.txt", "a") as file:
            file.write(todo + '\n')
            print(f"{todo} added  on your list")
            
     

def list():
        with open('todo.txt', 'r') as file:
              todo = file.readlines()
              print(todo)

def remove(erase):
     todo = []
     with open ('todo.txt', 'r') as file:
          todo = file.readlines()
          
     todo.remove(erase + "\n")
     with open ('todo.txt', 'w') as file:
          for item in todo:
               file.write(item)

     print(todo)
       
    
if __name__ == '__main__':
  fire.Fire()