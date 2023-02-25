#Definindo uma função básica
def myFunction():
  print("It's my first funcion")

myFunction()


#Função recebe argumentos
def myFunctionArg(name, age):
  print(f'Hello {name}, welcome! You are {age} years old!')

myFunctionArg('Vinicius', 27)

#Função que retorna um valor 
def functionReturn(x,y):
  return x * y

result = functionReturn(8,9)
print(result)
