def fun():
print("Ошибка")

print('Введите дату в формате DD.MM')
k = float(input()) 
g = round(k) 
l = round((k-g)*100)
if g in range(1, 31):
    if l==1:
        print ("Январь")
    else:
        if l==2:
            print ("Февраль")
        else:
            if l==3:
                print ("Март")
            else:
                if l==4:
                    print ("Апрель")
                else:
                    if l==5:
                        print ("Май")
                    else:
                        if l==6:
                            print ("Июнь")
                        else:
                            if l==7:
                                print ("Июль")
                            else:
                                if l==8:
                                    print ("Август")
                                else:
                                    if l==9:
                                        print ("Сентябрь")
                                    else:
                                        if l==10:
                                            print ("Октябрь")
                                        else:
                                            if l==11:
                                                print ("Ноябрь")
                                            else:
                                                if l==12:
                                                    print ("Декабрь")
                                                else:
                                                    fun()
    fun()