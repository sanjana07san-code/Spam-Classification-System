import sqlite3

# Database file name
DATABASE = "history.db"


# ==========================================
# Create Database and Table
# ==========================================
def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT NOT NULL,
        prediction TEXT NOT NULL,
        confidence REAL NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


# ==========================================
# Save Prediction
# ==========================================
def save_prediction(message, prediction, confidence):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions
    (message, prediction, confidence)
    VALUES (?, ?, ?)
    """, (message, prediction, confidence))

    conn.commit()
    conn.close()


# ==========================================
# Get Prediction History
# ==========================================
def get_history():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        message,
        prediction,
        confidence,
        created_at
    FROM predictions
    ORDER BY id DESC
    """)

    history = cursor.fetchall()

    conn.close()

    return history


# ==========================================
# Clear Prediction History (Optional)
# ==========================================
def clear_history():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM predictions")

    conn.commit()
    conn.close()


# ==========================================
# Search Prediction History (Optional)
# ==========================================
def search_history(keyword):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        message,
        prediction,
        confidence,
        created_at
    FROM predictions
    WHERE message LIKE ?
    ORDER BY id DESC
    """, ('%' + keyword + '%',))

    results = cursor.fetchall()

    conn.close()

    return results