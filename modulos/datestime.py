from datetime import date, datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays
import winsound as ws

setlocale(LC_ALL, "PT_BR.UTF-8")

data = datetime(2021, 6, 8, 10, 23, 44)
print(data.strftime("%d/%m/%Y  %H:%M:%S"))


data2 = datetime.strptime("21/11/2016", "%d/%m/%Y")
print(data2)

print(data2.timestamp()) # Segundos da data até o dia de hoje]]

d1 = datetime.strptime("20/11/1987 20:00:00", "%d/%m/%Y %H:%M:%S")
d2 = datetime.strptime("25/11/2003 22:30:05", "%d/%m/%Y %H:%M:%S")

print(d2 - d1)

dt = datetime.now()
formatacao = dt.strftime("%A, %d de %B de %Y  %H:%M:%S")
print(formatacao)

#for i in range(37,3000):
#    for j in range(30000):
#        ws.Beep(i, j)

mesAtual = int(dt.strftime("%m"))
print(mesAtual, mdays[mesAtual]) #Últimas dias de cada mês 