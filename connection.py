import psycopg2

conn = psycopg2.connect(
    database = "EmployeeTable",
    user = "postgres",
    host = "localhost",
    password = "Shilpi@123"
)

print(conn)
