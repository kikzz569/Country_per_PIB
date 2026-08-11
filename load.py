import sqlite3

def load_csv(df, file_path):
    df.to_csv(file_path, index=False)

def load_db(df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
