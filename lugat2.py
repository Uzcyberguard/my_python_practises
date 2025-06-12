lugat={"float":"o'nli son","str":"matn",".pop()":"to'plamdan nimanidir sug'urish",\
".remove('')":"nimanidir o'chirish"}
a=input("so'z kiriting>>>").lower()
b=lugat.get(a.lstrip(),"bunday so'z mavjud emas")
print(b)