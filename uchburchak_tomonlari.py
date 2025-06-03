print("bu dasrtur uchta tomonga ko'ra uchburchak yasash munkinmi yuqmi shini tekshiradi.")
a=float(input("uchburchakning tomonlarini kirit a="))
b=float(input("b="))
c=float(input("c="))
if a>b+c or b>a+c or c>a+b:
  print("bu o'lchamlardan uchburchak yasab bo'lmaydi.")
elif a<b+c and b<a+c and c<a+b:
 print("yasash mumkin")
