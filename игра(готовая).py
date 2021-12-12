import random
d=10
z=100
y=20
v=30
dn=1
print('Добро пожаловать в игру. Ваш герой - зайчик. И ваша задача заключается в поодержании его жизни. Удачи)')
while dn>=1:
    if dn%2==0:
        print('Ночь')
        d=d-2
        z=z+20
        y=y-2
        v=v-5
        print('Длинна норы -',d)
        print('Здоровье -',z)
        print('Уавжение -',y)
        print('Вес -',v)
        dn=dn+1
    else:
        print('День')
        print('Длинна норы -',d)
        print('Здоровье -',z)
        print('Уавжение -',y)
        print('Вес -',v)
        print('Выбери действие:')
        print('Набери 1, если будешь копать нору')
        print('Набери 2, если хочешь поесть травы')
        print('Набери 3, если Хочешь подраться')
        print('Набери 4, если хочешь спать весь день')
        a=int(input())
        if a==1:
            print('Набери 1, если хочешь копать интенсивно')
            print('Набери 2, если хочешь копать лениво')
            b1=int(input())
            if b1==1:
                d=d+5
                z=z-30
            elif b1==2:
                d=d+2
                z=z-10
        elif a==2:
            print('Набери 1, если хочешь поесть жухлой травки')
            print('Набери 2, если хочешь поесть зелёной травки')
            b2=int(input()) 
            if b2==1:
                z=z+10
                v=v+15
            elif b2==2:
                if y<30:
                    z=z-30
                elif y>=30:
                    z=z+30
                    v=v+30
        elif a==3:
            print('Введите тип существа:')
            print('Нажми 1, если выбираешь слабое существо')
            print('Нажми 2, если выбираешь среднее существо')
            print('Нажми 3, если выбираешь сильное существо')
            suh=int(input())
            if suh==1:
                ves=30
                ver=v+30
            elif suh==2:
                ves=50
                ver=v+50
            elif suh==3:
                ves=70
                ver=v+70  
            ver1=random.randint(1,ver)
            if ver1<=v:
                if v<ves:
                    y=y+40
                elif v==ves:
                    y=y+20
                elif v>ves:
                    y=y+10   
            else:
                if v<ves:
                    z=z-40
                elif v==ves:
                    z=z-20
                elif v>ves:
                    z=z-10 
        elif a==4:
            d=d-2
            z=z+20
            y=y-2
            v=v-5
        dn=dn+1
    print('Длинна норы -',d)
    print('Здоровье -',z)
    print('Уавжение -',y)
    print('Вес -',v)
    if y>=100:
        print('Уважение больше 100 - Вы выйграли!')
        break
    if (d<=0) or (z<=0) or (v<=0) or (y<=0):
        print('Зайчик умер - Вы проиграли')
        break


        
