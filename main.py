from time import sleep

import psycopg2

conn = psycopg2.connect(
    host = "127.0.0.1",
    database = "insta",
    user="postgres",
    password="20110915"
)

a = conn.cursor()



def menu():
    print("1-mahsulot kategoryasi")
    print("2-mahsulot qo'shish")
    print("3-mahsulotlarni ko'rish")
    print("4-narxini o'zgartirish")
    print("5-o'chirish")
    print("6-sotuv")
    print("0-chiqish")



def kategoriya():
    try:
        a.execute("SELECT * FROM products")
        b = a.fetchall()
        for i in b :
            print(i)
    except psycopg2.InterfaceError as e:
        print("Databazada ulanishda xatolik yuz berdi:", e)
    except psycopg2.DatabaseError as e:
        print("Databazada xatolik yuz berdi:", e)
    except Exception as e:
        print("Xatolik yuz berdi:", e)

    conn.cursor()



def qoshish():
    nomi = input("mahsulotni nomini kiriting: ")
    narxi = float(input("mahsulotni narxini kiriting: "))
    soni = int(input("sonini yozing: "))
    a.execute("""insert into products (name,price,soni) values (%s,%s,%s)""",(nomi,narxi,soni))
    print("sizning qo'shgan narsalaringiz mofuqiyatli qo'shildi bazada qo'shildi")
    conn.commit()   
    conn.cursor()


def korish():
    try:
        a.execute("SELECT * FROM products")
        chiqqanlar = a.fetchall()

        for i in chiqqanlar:
            print(i)
            pass
    except psycopg2.InterfaceError as e:
        print("Databazada ulanishda xatolik yuz berdi:", e)
    except psycopg2.DatabaseError as e:
        print("Databazada xatolik yuz berdi:", e)
    except Exception as e:
        print("Xatolik yuz berdi:", e)  
    finally:
        print("thanks 😇")

    conn.cursor()
    

def ozgartirish():
    nomi = input("mahsulotni nomini kiriting: ")
    narxi = float(input("mahsulotni yangi narxini kiriting:"))
    

    a.execute("""
    update products
    set price = %s
    where name = %s
    """,(narxi,nomi))
    conn.commit()
    conn.close()
    conn.cursor()


def ochirish():
    nomi = input("mahsulotni nomini kiriting: ")
    b = conn.cursor()
    a.execute("""delete from products where name = %s""",(nomi,))
    conn.commit()
    conn.cursor()


def sotuv():
    nomi = input("Mahsulot nomi: ")
    miqdor = int(input("Nechta sotildi: "))

    a.execute(
        "SELECT soni FROM products WHERE name = %s",
        (nomi,)
    )
    natija = a.fetchone()

    if natija is None:
        print("Bunday mahsulot mavjud emas!")
        

    qolgan = natija[0]

    if miqdor <= 0:
        print("Miqdor 0 dan katta bo'lishi kerak!")
    elif miqdor > qolgan:
        print(f"Omborda yetarli mahsulot yo'q! Qoldiq: {qolgan}")
    else:
        a.execute(
            "UPDATE products SET soni = soni - %s WHERE name = %s",
            (miqdor, nomi)
        )
        conn.commit()
        print(f"{nomi} dan {miqdor} ta sotildi!")
        print(f"Qolgan mahsulot: {qolgan - miqdor}")

    conn.cursor()

def hammasi():

    while True:

        menu()

        tanlash = int(input("tanlang:"))

        if tanlash == 1:

            kategoriya()

        

            sleep(3)

        elif tanlash == 2: 

            qoshish()

            sleep(3)

        elif tanlash == 3:

            korish()

            sleep(3)

        elif tanlash == 4:

            ozgartirish()

            sleep(3)

        elif tanlash == 5:  

            ochirish()

            sleep(3)
        elif tanlash == 6:

            sotuv()

            sleep(3)
        if tanlash == 0:
            
            print("dasturdan chiqish")

            break
        else:

            print("siz nito'g'ri raqam kiritdingiz")
hammasi()