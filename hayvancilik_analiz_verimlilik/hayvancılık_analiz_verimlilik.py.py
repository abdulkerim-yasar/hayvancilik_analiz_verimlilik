import datetime
import sqlite3

# Veritabanı bağlantısı oluştur
conn = sqlite3.connect('farm.db')
cursor = conn.cursor()

# Tablo oluştur
cursor.execute('''
CREATE TABLE IF NOT EXISTS daily_stats (
    id INTEGER PRIMARY KEY,
    date TEXT,
    animal_id INTEGER,
    food_intake FLOAT,
    milk_yield FLOAT,
    fertility_status TEXT,
    mood TEXT
)
''')

# Veri ekleme fonksiyonu (varsa güncelleme)
def add_daily_stat(date, animal_id, food_intake, milk_yield, fertility_status, mood):
    cursor.execute('''
    SELECT id FROM daily_stats
    WHERE date = ? AND animal_id = ?
    ''', (date, animal_id))
    data = cursor.fetchone()
  
    if data:
        cursor.execute('''
        UPDATE daily_stats
        SET food_intake = ?, milk_yield = ?, fertility_status = ?, mood = ?
        WHERE id = ?
        ''', (food_intake, milk_yield, fertility_status, mood, data[0]))
        print("Veri güncellendi.")
    else:
        cursor.execute('''
        INSERT INTO daily_stats (date, animal_id, food_intake, milk_yield, fertility_status, mood)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (date, animal_id, food_intake, milk_yield, fertility_status, mood))
        print("Yeni veri eklendi.")
    conn.commit()

# Örnek veri ekleme
add_daily_stat(datetime.date.today().strftime('%Y-%m-%d'), 1, 5.5, 10.2, 'Gebelik yoK', 'Mutlu')
add_daily_stat(datetime.date.today().strftime('%Y-%m-%d'), 2, 4.5, 7.2, 'Gebelik var', 'Mutsuz')

# Verileri sorgulama ve gösterme
cursor.execute('SELECT * FROM daily_stats')
all_rows = cursor.fetchall()
for row in all_rows:
    print(row)

# Bağlantıyı kapatma
conn.close()
print("Veritabani bağlantisi kapatildi.")
def add_daily_stat(date, animal_id, food_intake, milk_yield, fertility_status, mood):
    cursor.execute('''
    SELECT id FROM daily_stats
    WHERE date = ? AND animal_id = ?
    ''', (date, animal_id))
    data = cursor.fetchone()

    if data:
        cursor.execute('''
        UPDATE daily_stats
        SET food_intake = ?, milk_yield = ?, fertility_status = ?, mood = ?
        WHERE id = ?
        ''', (food_intake, milk_yield, fertility_status, mood, data[0]))
        print("Veri güncellendi.")
    else:
        cursor.execute('''
        INSERT INTO daily_stats (date, animal_id, food_intake, milk_yield, fertility_status, mood)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (date, animal_id, food_intake, milk_yield, fertility_status, mood))
        print("Yeni veri eklendi.")
    conn.commit()
