#Declarando e iniciando uma variável
study_python = 'Study Python is Cool! :)'
print(study_python)

#Declarando a mesma variável
study_python = "Python isn't typed language. I can declare everywhere, everytime."
print(study_python)

#Gerando um erro, tentando unir variáveis de tipos diferentes 
#print("It's a string" + 123) 
#TypeError: can only concatenate str (not "int") to str

#Variável global x Variável local

def funcion():
  cool = 'Python'
  print(cool)


funcion()