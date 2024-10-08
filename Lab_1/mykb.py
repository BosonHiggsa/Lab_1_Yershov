import pandas
KB={("гнсс", "перевага", "швидкість"),
    ("гнсс", "перевага", "дешевизна"),
    ("гнсс", "недолік", "низька точність"),
    ("гнсс", "недолік", "залежність від звязку"),
    ("тахеометр", "перевага", "точність"),
    ("тахеометр", "перевага", "автономність"),
    ("тахеометр", "недолік", "часозатратність"),
    ("тахеометр", "недолік", "дороговизна"),
    ("лідар", "перевага", "швидкість"),
    ("лідар", "перевага", "точність"),
    ("лідар", "недолік", "дороговизна"),
    ("лідар", "недолік", "довге опрацювання")}
df = pandas.DataFrame(columns=["s","p","o"])
i=0
for s,p,o in KB:
    df.loc[i]={"s":s, "p":p, "o":o}
    i+=1
#df.to_csv('kb.csv', index=False)
df = pandas.read_csv('kb.csv')