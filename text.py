list=[]
while True:
    a=int(input('1= add expence, 2= view expence, 3= delete expence, 4= exit: '))
    if a==1:
        print('add expence')
        name=input('enter expence name:')
        exp=int(input('enter expence amount:'))
        list.append((name, exp))
    elif a==2:
        print('view expence')
        for name, exp in list:
            print(name, exp)
    elif a==3:
        print('delete expence')
        name=input('enter expence name to delete:')
        list=[(n,e) for n,e in list if n!=name]
    elif a==4:
        print('bye')
        break
