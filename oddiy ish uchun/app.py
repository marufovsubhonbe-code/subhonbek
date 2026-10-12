# # 1
# def tashqi(fuck):
#     def ichki():
#         print("Boshladik")
#         fuck()
#         print("Tugadi")
#     return ichki

# @tashqi
# def keyin():
#     print("keyin")

# print(keyin())

# # 2
# import time
# def tashqari(funk):
#     def ichki():
#         boshlash = time.time()
#         natija = funk()
#         tugash = time.time()
#         print(f"ketgan vaqt {tugash - boshlash:.4f}")
#         return natija
#     return ichki

# @tashqari
# def hisoblash():
#     joyir = 0    
#     for i in range(1,100):
#         joyir += i
#     return joyir

# print(hisoblash())

# 3
def faqat_musbat(funksiya):
    def sonlar(*args ,  **kwargs):
        try:
            natija = funksiya(*args, **kwargs)
            if natija> 0:
                print("son musbat")
            else:
                print("musbat emas")
            return natija
        except ZeroDivisionError:
            print("0 ni kiritish mumkin emas")
        except TypeError:
            print("yozganinggizda xatolik bor")
    return sonlar

