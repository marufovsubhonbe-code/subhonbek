class Uchuvchi:
    def harakat(self):
        return "uchyabdi"

class Suzuvchi:
    def harakat(self):
        return "suzyabdi"

class Goz(Uchuvchi, Suzuvchi):
    pass


o = Goz()
print(o.harakat())
for k in Goz.__mro__:
    print(k.__name__)
