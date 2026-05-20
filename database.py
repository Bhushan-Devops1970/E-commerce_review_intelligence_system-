import sqlite3 # here we have imported python library for database intigration

DB_NAME = "reviews.db" # file name


# Connect to database established connection with database
def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

# Create table if not exists
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        review TEXT,
        sentiment TEXT,
        category TEXT,
        rating INTEGER,
        confidence REAL,
        fake_status TEXT
    )
    """)

    conn.commit()
    conn.close()

# Insert new review into database
def insert_review(review, sentiment, category, rating, confidence, fake_status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO reviews (review, sentiment, category, rating, confidence, fake_status)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (review, sentiment, category, rating, confidence, fake_status))

    conn.commit()
    conn.close()

# Fetch all stored reviews
def fetch_reviews():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reviews")
    data = cursor.fetchall()

    conn.close()
    return data