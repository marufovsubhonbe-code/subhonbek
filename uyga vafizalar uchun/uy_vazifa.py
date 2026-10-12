def hisoblash(funk):
    def wrapper():
        print("Hisoblash boshlandi")     
        funk()
        print("Hisoblash tugadi")
        
    return wrapper

@hisoblash
def qoshish():
    print(10 + 20)

qoshish()
