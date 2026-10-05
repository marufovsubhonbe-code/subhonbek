# 1
class Uchuvchi:
    def harakat(self):
        return "uchyabdi"


class Suzuvchi:
    def harakat(self):
        return "suzyabdi"


class Goz(Uchuvchi, Suzuvchi):
    pass


class Goz2(Suzuvchi, Uchuvchi):
    pass


o = Goz()
o2 = Goz2()
print(o.harakat())
print(o2.harakat())

for k in Goz.__mro__:
    print(k.__name__)
for k in Goz2.__mro__:
    print(k.__name__)


# 2
class Odam:
    pass


class Talaba(Odam):
    pass


class Ishchi(Odam):
    pass


class IshlovchiTalaba(Talaba, Ishchi):
    pass


i = IshlovchiTalaba()
for k in IshlovchiTalaba.__mro__:
    print(k.__name__)
print(len(IshlovchiTalaba.__mro__), "ta klass")


# 3
class Odam2:
    def __init__(self, ism, **kw):
        self.ism = ism
        super().__init__(**kw)

    def tanish(self):
        print("Odam")


class Talaba2(Odam2):
    def __init__(self, ism, guruh, **kw):
        self.guruh = guruh
        super().__init__(ism, **kw)

    def tanish(self):
        print("Talaba:", self.guruh)
        super().tanish()


class Ishchi2(Odam2):
    def __init__(self, ism, maosh, **kw):
        self.maosh = maosh
        super().__init__(ism, **kw)

    def tanish(self):
        print("Ishchi:", self.maosh)
        super().tanish()


class IshlovchiTalaba2(Talaba2, Ishchi2):
    def tanish(self):
        print("Ishlovchi talaba")
        super().tanish()


i2 = IshlovchiTalaba2(ism="Ali", guruh="2-kurs", maosh=5000000)
i2.tanish()
for k in IshlovchiTalaba2.__mro__:
    print(k.__name__)


# 4
class A:
    pass


class B(A):
    pass


class X(B, A):
    pass


for k in X.__mro__:
    print(k.__name__)

try:
    class Y(A, B):
        pass
except TypeError as e:
    print("TypeError:", e)


# 5
class Qurilma:
    def yoq(self):
        return "Quqishni boshladim"


class Telefon(Qurilma):
    def yoq(self):
        return "Telefon yoqdi"


class Kamera(Qurilma):
    def yoq(self):
        return "Kamera yoqdi"


class Smartfon(Telefon, Kamera):
    pass


print(Smartfon().yoq())
mro = [k.__name__ for k in Smartfon.__mro__]
print(mro)
print("Quqilma necha marta:", mro.count("Qurilma"))


# 6
class Qurilma2:
    def yoq(self):
        print("Qurilma: hammasi tayyor")


class Telefon2(Qurilma2):
    def yoq(self):
        print("Telefon: ekran yondi")
        super().yoq()


class Kamera2(Qurilma2):
    def yoq(self):
        print("Kamera: suratga tayyor")
        super().yoq()


class Smartfon2(Telefon2, Kamera2):
    def yoq(self):
        print("Smartfon: quqish boshlandi")
        super().yoq()


Smartfon2().yoq()


# 7
class Odam3:
    def __init__(self, ism, **kw):
        self.ism = ism
        super().__init__(**kw)


class Talaba3(Odam3):
    def __init__(self, guruh, **kw):
        self.guruh = guruh
        super().__init__(**kw)


class Ishchi3(Odam3):
    def __init__(self, maosh, **kw):
        self.maosh = maosh
        super().__init__(**kw)


class IshlovchiTalaba3(Talaba3, Ishchi3):
    pass


i3 = IshlovchiTalaba3(ism="Ali", guruh="2-kurs", maosh=5000000)
print(i3.ism, i3.guruh, i3.maosh)


# 8
import json


class JSONMixin:
    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)


class Mahsulot(JSONMixin):
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx


m = Mahsulot("Choy qoshiq", 12000)
print(m.to_json())
print(type(m.to_json()))


# 9
class LogMixin:
    def log(self, xabar):
        print(f"[{type(self).__name__}] {xabar}")


class Kitob(JSONMixin, LogMixin):
    def __init__(self, nom, muallif, narx):
        self.nom = nom
        self.muallif = muallif
        self.narx = narx


k = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 45000)
print(k.to_json())
k.log("kitob qo'shildi")
for kl in Kitob.__mro__:
    print(kl.__name__)


# 10
class Xabar:
    def matn(self):
        return "salom"


class QavsMixin:
    def matn(self):
        return "[" + super().matn() + "]"


class YulduzMixin:
    def matn(self):
        return "*" + super().matn() + "*"


class Xabar1(QavsMixin, YulduzMixin, Xabar):
    pass


class Xabar2(YulduzMixin, QavsMixin, Xabar):
    pass


print(Xabar1().matn())
print(Xabar2().matn())


# 11
class Dvigatel:
    def ishga_tushir(self):
        return "Dvigatel ishga tushdi"


class ElektrDvigatel:
    def ishga_tushir(self):
        return "Elektr dvigatel jimgina ishga tushdi"


class Mashina:
    def __init__(self, dvigatel=None):
        self.dvigatel = dvigatel if dvigatel else Dvigatel()

    def yur(self):
        return self.dvigatel.ishga_tushir() + " -> mashina yurdi"


mashina = Mashina()
print(mashina.yur())

mashina.dvigatel = ElektrDvigatel()
print(mashina.yur())


# 12
print("Talaba/Odam -> is-a")
print("Kitob/Muallif -> has-a")
print("Kitob/JSON -> can-do")
print("Mashina/Gildirak -> has-a")
print("Ordak/Qush -> is-a")
print("Xodim/Loglash -> can-do")


class Xodim:
    def __init__(self, ism):
        self.ism = ism


class Oshpaz(Xodim):
    pass


class Gildirak:
    def __init__(self):
        self.ogirlik = 15


class Ttransport:
    def __init__(self):
        self.gildirak = Gildirak()


class Ofitsiant(JSONMixin, Xodim):
    pass


print(Oshpaz("Ali").ism)
print(Ttransport().gildirak.ogirlik)
print(Ofitsiant("Laylo").to_json())


# 13
class Odam4:
    def __init__(self, ism, **kw):
        self.ism = ism
        super().__init__(**kw)

    def tanish(self):
        print(f"Ism: {self.ism}")


class TalabaMixin:
    def __init__(self, guruh, **kw):
        self.guruh = guruh
        super().__init__(**kw)

    def tanish(self):
        print(f"Guruh: {self.guruh}")
        super().tanish()


class OqituvchiMixin:
    def __init__(self, fan, **kw):
        self.fan = fan
        super().__init__(**kw)

    def tanish(self):
        print(f"Fan: {self.fan}")
        super().tanish()


class Assistent(JSONMixin, LogMixin, TalabaMixin, OqituvchiMixin, Odam4):
    pass


a = Assistent(ism="Ali", guruh="2-kurs", fan="Python")
a.tanish()
print(a.to_json())
a.log("darsga tayyorlanmoqda")

for kl in Assistent.__mro__:
    print(kl.__name__)
print("Odam necha marta:", [k.__name__ for k in Assistent.__mro__].count("Odam4"))


class Kurs:
    def __init__(self, nom):
        self.nom = nom
        self.talabalar = []

    def qosh(self, odam):
        self.talabalar.append(odam)

    def royxat(self):
        print(f"{self.nom} kursida {len(self.talabalar)} ta o'quvchi:")
        for o in self.talabalar:
            print(" -", o.ism)


kurs = Kurs("Python asoslari")
kurs.qosh(a)
kurs.qosh(Assistent(ism="Laylo", guruh="1-kurs", fan="Algoritmlar"))
kurs.qosh(Assistent(ism="Sardor", guruh="3-kurs", fan="Ma'lumotlar bazasi"))
kurs.royxat()