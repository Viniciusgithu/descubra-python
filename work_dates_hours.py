#importando módulos

from datetime import date
from datetime import time
from datetime import datetime

import calendar

def today():
  weekdays = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday','Sunday']
  data = date.today()
  print(f'A data de hoje é: {data}')
  print(f'Dia: {data.weekday()}, equivalante a: {weekdays[data.weekday()]}, do mês: {data.month}, do ano: {data.year} ')

  dataCompleted = datetime.now()
  temp = datetime.time(dataCompleted)
  print(f'Horas: {temp}')


#today()  


### Date Formatting ###

### %y/%Y - YEAR , %a/%A - WEEKDAYS , %b/%B - MONTH , %d - DAY OF MONTH ###

def formatDate():
  hoje = datetime.now()

  print(hoje.strftime('O ano é: %y'))
  print(hoje.strftime('Data e hora: %c'))


#formatDate()


### Time Formatting ###

### %I/%H - 12/24 horas, %M - minuto, %S - segundo, %p - AM/PM 

def horaAtual():
  hoje = datetime.now()
  print(hoje.strftime(f'A hora atual é: %I:%M:%S %p'))


#horaAtual()


def faltamQuantosDias(ano, mes, dia):
  hoje = date.today()
  dataDesejada = date(ano, mes, dia)
  quantosDias = dataDesejada - hoje

  msg = f'Faltam: {quantosDias} para a data: {dataDesejada.strftime("%y/%m/%d")}'

  print(msg)

#faltamQuantosDias(2023,3,1)  


def calendario():
  calendarioText = calendar.TextCalendar(calendar.SUNDAY)
  txtCalendario = calendarioText.formatmonth(2023, 2)
  print(txtCalendario)


#calendario()


def printMonth():
  for month in calendar.month_name:
    print(month)
  for days in calendar.day_name:
    print(days)  


printMonth()