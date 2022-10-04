x_1 = float(input('digite o x de p1: '))
y_1 = float(input('digite o y de p1: '))
x_2 = float(input('digite o x de p2: '))
y_2 = float(input('digite o y de p2: '))

tup_1 = (x_1,y_1)
tup_2 = (x_2,y_2)


distance =(((( tup_2 [0] - tup_1[0])*( tup_2[0] - tup_1[0])) + ((tup_2[1] - tup_1[1])*(tup_2[1] - tup_1[1])))**(1/2))

print('A distância é:', distance)