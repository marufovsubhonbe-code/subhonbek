def salalomlash(ism):
    return f"salom {ism}"

# m = salalomlash
# print(m("Ali"), m.__name__)

def uch_marta(funk,ism):
    return funk(ism),funk(ism),funk(ism)

print(uch_marta(salalomlash, "ali"))


amaliy = [len, str.upper,str.lower]
for a in amaliy:
    print(a("Subhonbek"))

    