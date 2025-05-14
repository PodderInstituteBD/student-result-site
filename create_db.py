import sqlite3

# ডেটাবেজ তৈরি বা সংযোগ
conn = sqlite3.connect('results.db')
c = conn.cursor()

# টেবিল তৈরি (results)
c.execute('''
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
''')

# ডেটা সংরক্ষণ ও বন্ধ করা
conn.commit()
conn.close()

print("results.db তৈরি হয়ে গেছে!")
