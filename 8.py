a=int(input('Bu dastur sizlarga sekundlarni soat, minut va sekundlarga aylantiradi. PLS...Sekundlarni kirit (ko"pi bilan 5 xonali):'))
if len(str(a))>5 :
    print('dastur faqat 5 xonali songacha ishlaydi!!!!')   
elif len(str(a))==5:
    b=a//3600
    a%=3600
    c=a//60
    a%=60
    print(b,'soat',c,'daqiqa',a,'sekund')
elif len(str(a))==4:
    b=a//3600 
    a%=3600
    c=a//60
    a%=60
    print(b,'soat',c,'daqiqa',a,'sekund')
elif  len(str(a))==3:
    c=a//60
    a%=60
    print(c,'daqiqa',a,'sekund')        
elif len(str(a))==2:
    c=a//60
    a%=60
    print(c,'daqiqa',a,'sekund')
elif len(str(a))==1:
    print(a,'sekund')
