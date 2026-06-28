import duckdb

conn = duckdb.connect("crypto_pipeline.db")
cursor = conn.cursor()

with open("schema.sql", "r") as file:
    schema_sql = file.read()

try:
    cursor.execute(schema_sql)
    print("Database initialised successfully.")
except Exception as e:
    print(f"Error executing schema script: {e}")

conn.close()
