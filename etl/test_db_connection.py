##This script is to test the database connection between the strava api and our database on pg admin
##If the connection is successful, a success message will print on our console
# import psycopg2

DB_NAME = "madeira_trails"   # change with the database name you set
DB_USER = "postgres"         # change with your username
DB_PASSWORD = "postgres"  # change with your password
DB_HOST = "localhost"
DB_PORT = "5432"

def main():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        print("Connected to database :)")
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM trails;")
        count = cur.fetchone()[0]
        print(f"Number of rows in trails table: {count}")
        cur.close()
        conn.close()
    except Exception as e:
        print("Error connecting to database:")
        print(e)

if __name__ == "__main__":
    main()
