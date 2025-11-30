from turtle import *
import csv
#max salary
file=open("SALARY.csv")
income=csv.reader(file)
maxs=[]
for i in income:
    name=i[0:2]
    maxx=[]
    for j in i[2:]:
        maxx.append(j)
    maxs.append((name,max(maxx)))    
#barchart       
ht()
windows=Screen().bgcolor('#90EE90')
penup()
goto(-window_width()//3,200)
write('SALARY')
pendown()
right(90)
forward(300)
left(90)
forward(20)
for i in maxs:
    x=int(i[1])*10
    begin_fill()
    left(90)
    forward(x)
    right(90)
    write(i[1])
    forward(50)
    right(90)
    forward(x-10)
    write(i[0][0],font=('Tohoma',8),move=False,align='right')
    forward(10)
    fillcolor('#D8BFD8')
    write(i[0][1],font=('Tohoma',8),move=True,align='right')
    end_fill()
    left(90)
    forward(20)
forward(20)
write('NAMES')
done()
        