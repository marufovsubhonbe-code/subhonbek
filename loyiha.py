from sre_constants import IN

import psycopg2

conn = psycopg2.connect(
    host = "127.0.0.1",
    database = "loyiha",
    password="20110915"     
)

asosiy = conn.cursor()

# asosiy.execute("""
# CREATE TABLE mijozlar(
#     id SERIAL PRIMARY KEY,
#     ism_familiya varchar(100),
#     telefon_raqam INTEGER UNIQUE)
# """)
# conn.commit()

# asosiy.execute("""
# CREATE TABLE mashinalar(

#     id SERIAL PRIMARY KEY,
#     Avtomobil_egasi varchar(100),
#     brend varchar(100),
#     model varchar(100),
#     davlat_raqam varchar(100) UNIQUE,
#     avtomobil_egasi_id integer REFERENCES mijozlar(id)
# )
# """)
# conn.commit()

# asosiy.execute("""
# CREATE TABLE ustalar(
#     id SERIAL PRIMARY KEY,
#     ism_familiya varchar(100),
#     staji integer)
# """)
# conn.commit()

# asosiy.execute("""
#     CREATE TABLE xizmatlar(
#     id SERIAL PRIMARY KEY,
#     xizmat_nomi varchar(100),
#     xizmat_narxi integer,
#     xizmatlar_id bigint REFERENCES mashinalar(id)
#     )
# """)

# asosiy.execute("""
#     ALTER TABLE xizmatlar
#     ADD COLUMN mashinalar_id BIGINT REFERENCES mashinalar(id);
# """)
# conn.commit()

# asosiy.execute("""
# CREATE TABLE tamirlash_buyurtmalari(
#     id SERIAL PRIMARY KEY,
#     tamirlanayotgan_avtomobil VARCHAR(100),
#     xizmat_korsatuvchi_ustasi VARCHAR(100),
#     korsatilgan_xizmat VARCHAR(100),
#     buyurtma_sanasi DATE,
#     tamirlash_holati VARCHAR(100),
#     tamirlanayotgan_avtomobil_id bigint REFERENCES mashinalar(id),
#     xizmat_korsatuvchi_ustasi_id bigint REFERENCES ustalar(id),
#     korsatilgan_xizmat_id bigint REFERENCES xizmatlar(id))
# """)
# conn.commit()

# asosiy.execute("""
# INSERT INTO mijozlar (ism_familiya, telefon_raqam) VALUES
# ('Marufov Subhonbek', 903685010);
# """)

# conn.commit()

# asosiy.execute("""
# INSERT INTO mashinalar(Avtomobil_egasi, brend, model, davlat_raqam) VALUES
# ('Marufov Subhonbek', 'BMW', 'M5', '40Z777ZZ'),
# ('Abdugafforov Muhammaddiyor','Mercedes-Benz','Los Angeles','02B112BB'),
# ('Umarov Alibek','Chevrolet','Nexia 3','03C223CC'),
# ('Alijonov Muhammadumar','Chevrolet','Malibu','04D334DD'),
# ('Saidov Shaxzod','Toyota','Camry','05E445KTEE'),
# ('Toshmatov Shoxrux','Toyota','Land Cruiser','06F556FF'),
# ('Abdullayev Shoxrux','Toyota','Camry','07G667GG'),
# ('Usmonjonov Asilbek','Toyota','Camry','08H778HH');
# """)

# conn.commit()



# asosiy.execute("""
#     INSERT INTO ustalar (ism_familiya, staji)
# VALUES
# ('Aliyev Akmal', 5),
# ('Valiyev Sardor', 8),
# ('Karimov Aziz', 3),
# ('Sodiqov Javohir', 6),
# ('Toshmatov Bekzod', 10);
# """)

# conn.commit()

# asosiy.execute("""
#     INSERT INTO xizmatlar (xizmat_nomi, xizmat_narxi)
# VALUES
# ('Motor ta''mirlash', 1500000),
# ('Moy almashtirish', 250000),
# ('Diagnostika', 150000),
# ('Tormoz ta''mirlash', 500000),
# ('Shina almashtirish', 200000);
# """)
# conn.commit()

# asosiy.execute("""
# INSERT INTO tamirlash_buyurtmalari (
#     tamirlanayotgan_avtomobil,
#     xizmat_korsatuvchi_ustasi,
#     korsatilgan_xizmat,
#     buyurtma_sanasi,
#     tamirlash_holati,
#     tamirlanayotgan_avtomobil_id,
#     xizmat_korsatuvchi_ustasi_id,
#     korsatilgan_xizmat_id
# )
# VALUES
# ('BMW M5', 'Aliyev Akmal', 'Motor ta''mirlash', '2026-11-21', 'Jarayonda', 17, 1, 1),
# ('Mercedes-Benz', 'Valiyev Sardor', 'Moy almashtirish', '2026-11-20', 'Tugallangan', 18, 2, 2),
# ('Chevrolet Nexia 3', 'Karimov Aziz', 'Diagnostika', '2026-11-19', 'Kutilmoqda', 19, 3, 3),
# ('Chevrolet Malibu', 'Sodiqov Javohir', 'Tormoz ta''mirlash', '2026-11-18', 'Jarayonda', 20, 4, 4),
# ('Toyota Land Cruiser', 'Toshmatov Bekzod', 'Shina almashtirish', '2026-11-17', 'Tugallangan', 22, 5, 5);
# """)

# conn.commit()

# asosiy.execute("""
#     DELETE FROM tamirlash_buyurtmalari
#     WHERE id IN (16, 17, 18, 19, 20);
# """)

# conn.commit()



def avtomobil_tarixi():
    asosiy.execute("""
    SELECT davlat_raqam
    FROM mashinalar;
    """)

    natija = asosiy.fetchall()

    print("\n--- AVTOMOBILLAR DAVLAT RAQAMLARI ---")

    for qator,raqamalr in enumerate(natija, start=1):
        print(qator,raqamalr)

    mashinani_davlat_raqami = input("mashinangizni davlat raqamini kiriting: ").upper()
    asosiy.execute("""
    SELECT t.buyurtma_sanasi FROM mashinalar m
    
    join tamirlash_buyurtmalari t 
    
    on m.id = t.tamirlanayotgan_avtomobil_id
    
    WHERE m.davlat_raqam = %s;
    
    """, (mashinani_davlat_raqami,))
    
    natija = asosiy.fetchall()
    
    if natija:
        print(f"{mashinani_davlat_raqami} raqamli mashina uchun ta'mirlash buyurtmalari sanalari:")
        for qator, sana in enumerate(natija, start=1):
            print(f"{qator}. {sana[0]}")
    else:
        print(f"{mashinani_davlat_raqami} raqamli mashina  topilmadi")



    
    asosiy.execute("""
    SELECT t.tamirlash_holati FROM mashinalar m
    JOIN tamirlash_buyurtmalari t
    ON m.id = t.tamirlanayotgan_avtomobil_id
    WHERE m.davlat_raqam = %s;""", (mashinani_davlat_raqami,))

    qayerda = asosiy.fetchall()
    if qayerda:
        print(f"{mashinani_davlat_raqami} raqamli mashina uchun holati: {qator}, {qayerda[0][0]}")
        
    else:
        print(f"{mashinani_davlat_raqami} raqamli mashina topilmadi")

def ustalar_bajargan_ishlar_soni():
    asosiy.execute("""
    SELECT 
        u.ism_familiya AS usta,
        COUNT(t.id) AS ishlar_soni
    FROM ustalar u
    INNER JOIN tamirlash_buyurtmalari t
        ON u.id = t.xizmat_korsatuvchi_ustasi_id
    GROUP BY u.id, u.ism_familiya
    ORDER BY u.id;
    """)
    natija = asosiy.fetchall()
    print("---USTALAR BAJARGAN ISHLAR SONI---")
    for qator in natija:
        print(f"USTA: {qator[0]} Bajargan ishlar soni: {qator[1]}")


def eng_kop_xizmat_qilgan_usta():
    asosiy.execute("""
    SELECT 
        u.ism_familiya as usta,
        MAX(t.xizmat_korsatuvchi_ustasi_id) as kop_xizmat 
        FROM ustalar u 
        INNER JOIN tamirlash_buyurtmalari t
            ON u.id = t.xizmat_korsatuvchi_ustasi_id
        GROUP BY u.id, u.ism_familiya
        ORDER BY kop_xizmat DESC
        LIMIT 1;
            """)

    natija = asosiy.fetchall()
    print("---QAYSI USTA ENG KO'P ISHLAGAN YANI QUL BO'LIB ISHLADI---")
    for qator in natija:
        print(f"eng ko'p ishlagan usta: {qator[0]}")


def umumiy_summa():
    asosiy.execute("""
    SELECT 
        m.ism_familiya,
        SUM(x.xizmat_narxi) AS jami_summa
    FROM mijozlar m
    JOIN mashinalar a 
        ON m.id = a.avtomobil_egasi_id
    JOIN tamirlash_buyurtmalari t  
        ON a.id = t.tamirlanayotgan_avtomobil_id
    
    JOIN xizmatlar x
        ON t.korsatilgan_xizmat_id = x.id
    
    GROUP BY m.ism_familiya;
    """)
    natija = asosiy.fetchall()
    print("JAMI SUMMA")
    for summa in natija:
        print(f"Mijoz: {summa[0]}  |  barcha summa {summa[1]} so'm")

def status_ozgartirish():
    asosiy.execute("""
        SELECT id, tamirlash_holati
        FROM tamirlash_buyurtmalari
    """)

    natija = asosiy.fetchall()

    print("\n--- BUYURTMALAR ---")

    for qator in natija:
        print("ID:", qator[0], "| Status:", qator[1])

    id = int(input("\nBuyurtma ID sini kiriting: "))

    status = input("Yangi statusni kiriting: ")

    asosiy.execute("""
        UPDATE tamirlash_buyurtmalari
        SET tamirlash_holati = %s
        WHERE id = %s
    """, (status, id))

    conn.commit()

    print("Status o'zgartirildi!")


def mashina():
    asosiy.execute("SELECT * FROM mashinalar")
    mashina = asosiy.fetchall()
    print("Mashinalar bo'limi")
    for i in mashina:
        print(i)

def mijozlar():
    asosiy.execute("SELECT * FROM mijozlar")
    mijoz = asosiy.fetchall()
    print("Mijozlar bo'limi")
    for i in mijoz:
        print(i)

def tamirlash_buyurtmalari():
    asosiy.execute("SELECT * FROM tamirlash_buyurtmalari")
    buyutma = asosiy.fetchall()
    print("tamirlash_buyurtmalari bo'limi")
    for i in buyutma:
        print(i)
tamirlash_buyurtmalari()
def ustalar():
    asosiy.execute("SELECT * FROM ustalar")
    usta = asosiy.fetchall()
    print("ustalar bo'limi")
    for i in usta:
        print(i)

def xizmatlar():
    asosiy.execute("SELECT * FROM xizmatlar")
    xizmat = asosiy.fetchall()
    print("xizmatlar bo'limi")
    for i in xizmat:
        print(i)

def menu():
    print("1. Avtomobilning ta'mirlash tarixini ko'rish")
    print("2. Ustalar bajargan ishlar soni")
    print("3. Eng ko'p xizmat ko'rsatgan ustani toping")
    print("4. sarflagan umumiy pulini hisoblang.")
    print("5. Ta'mirlash buyurtmasining statusini o'zgartiring")
    print("6. Mashinalar bo'limini ko'rish")
    print("7. Mijozlar bo'limini ko'rish")
    print("8. buyurtmalarni ko'rish")
    print("9. ustalar bo'limi ko'rish")
    print("10. xizmatlar bo'limi ko'rish")
    print("0. exit")


from time import sleep

def hammasi():
    while True:
        menu()
        tanlash = int(input("tanlang: "))
        if tanlash == 1:
            
            avtomobil_tarixi()
            
            sleep(3)

            
        elif tanlash == 2:
            
            ustalar_bajargan_ishlar_soni()

            sleep(3)
            
           
        elif tanlash == 3:

            eng_kop_xizmat_qilgan_usta()

            sleep(3)
            
            
        elif tanlash == 4:
            
            umumiy_summa()
            
            sleep(3)

            
        elif tanlash == 5:
            
            status_ozgartirish()
            
            sleep(3)

        elif tanlash == 6:
            
            mashina()
            
            sleep(3)
        
        elif tanlash == 7:
            
            mijozlar()

            sleep(3)

        elif tanlash == 8:
            
            tamirlash_buyurtmalari()

            sleep(3)

        elif tanlash == 9:
            
            ustalar()

            sleep(3)

        elif tanlash == 10:
            xizmatlar()

            sleep(3)

        elif tanlash == 0:
            print("dasturdan chiqdingiz va dastur to'xtadi")
            break
        else:
            print("siz kirtgan raqam buyerda yo'q")

if __name__ == '__main__':
    hammasi()