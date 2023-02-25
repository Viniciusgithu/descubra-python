def conditional():
  x,y = 50,50
  
  if(x < y):
    print(f'The value: {x} is smaller than {y}')
  elif(x > y):
    print(f'The value {x} is bigger than {y}')
  else:
    print(f'The numbers {x} and {y} are similar')
#conditional()  


def loopWhile():
  x = 1
  while(x < 10):
    print(f'Card number: {x}, next card...')
    x += 1
    if(x == 10):
      print(f'Finesh card. I see you tomorrow!')
  
#loopWhile()


shop = ['Pineapple','Grapes','Kiwi','Lemon','Strawberry','Mango','Raspberry']

for goShop in shop:
  print(f'Go to the grocery and buy: {goShop}')
