# 1
def tabriklash(ism):
    return f"Tabriklaymiz {ism}"

o = tabriklash
print(o("Ali"))
print(o.__name__, tabriklash.__name__)

amal = [str.upper, str.lower,len]
for i in amal:
    print(i("Toshkent"))

# 2
def uch_marta(funk, x):
    return funk(funk(funk(x)))

def qosh10(son):
    return son + 10

def ikkilantir(son):
    return son * 2

print(uch_marta(qosh10, 5))      
print(uch_marta(ikkilantir, 5))  
print(uch_marta(str.upper, "salom"))  

# 3
def darajaga(n):
    def ichki(son):
        return son ** n
    return ichki
kvadrat = darajaga(2)
kub = darajaga(3)
print(kvadrat(5))
print(kub(5))

# 4 
def darajaga(n):
    def daraja(x):
        return x ** n
    return daraja

kub = darajaga(3)
print(kub(2))                      

print(kub.__closure__)             
print(len(kub.__closure__))        


print(kub.__closure__[0].cell_contents) 

def oddiy(x):
    return x * 2

print(oddiy.__closure__)

# 5
def hisoblagich():
    jami = 0
    def qoshish(son):
        nonlocal jami
        jami += son
        return jami
    return qoshish
h = hisoblagich()
print(h(10000))
print(h(8000))
print(h(3000))

# 6
def parol_tekshir(togri_parol):
    urunishlar_soni = 0
    def kirish(kiritish):
        nonlocal urunishlar_soni
        if urunishlar_soni >= togri_parol:
            return "dastur tugadi"
        urunishlar_soni += 1
        return f"{kiritish}({urunishlar_soni}/{togri_parol}) ta urunishlar qoldi"
    return kirish
parol = parol_tekshir(2)
print(parol("Ali"))

# 7
def chiziq(funk):
    def orob():
        print("*"*15)
        funk()
        print("*"*15)
    return orob
def xabar():
    print("dars boshlandi")

xabar = chiziq(xabar)
xabar()

# 8

def chiziq(funk):
    def orob():
        print("[    boshlandi   ]")
        funk()
        print("[     tugadi     ]")
    return orob
def nuqta(funk):
    def orob():
        print("...")
        funk()
        print("...")
    return orob
@chiziq
@nuqta

def salom():
    print("salom Ali")

salom()

# 9

def bezash(func):
    def wrapper(*args, **kwargs):
        print("Funksiya nomi:", func.__name__)
        natija = func(*args, **kwargs)
        return natija
    return wrapper


@bezash
def kopaytir(a, b):
    return a * b
print(kopaytir(6, 7))   

# 10
from functools import wraps


def bezash(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bezash
def salom():
    """Bu salom funksiyasi"""
    return "Salom"

print(salom.__name__)   
print(salom.__doc__)    

def bezash2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bezash2
def salom2():
    return "Salom"


print(salom2.__name__) 
print(salom2.__doc__)  

# 11
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        boshlanish = time.perf_counter()
        natija = func(*args, **kwargs)
        tugash = time.perf_counter()
        print(f"{func.__name__} vaqti: {tugash - boshlanish:.4f} soniya")
        return natija
    return wrapper

@timer
def kvadratlar(n):
    return [i ** 2 for i in range(n)]

@timer
def kvadratlar_sikl(n):
    natija = []
    for i in range(n):
        natija.append(i ** 2)
    return natija


n = 1_000_000
kvadratlar(n)
kvadratlar_sikl(n)

# 12

"""
nima qilishni tushunmadim
"""