import psycopg2

class DB:
    def __init__(self) -> None:
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                user="shsn",
                password="Xn~Izpb91iEckYPPuC@umjhJ",
                database="mega-moga"   
            )
            self.connection.autocommit = True
        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)


    def create_db(self):
    
        with self.connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS config_list (
                    name    TEXT UNIQUE NOT NULL,
                    token   varchar(44) NOT NULL,
                    key     varchar(44) UNIQUE NOT NULL,
                    ref     varchar(8) NOT NULL
                );
                
                CREATE TABLE IF NOT EXISTS events (
                    id      serial PRIMARY KEY,
                    name    TEXT    NOT NULL,
                    command TEXT  NOT NULL,
                    tg_id   INTEGER NOT NULL
                );

                CREATE TABLE IF NOT EXISTS tg_user (
                    tg_id INTEGER NOT NULL,
                    ref   TEXT NOT NULL,
                    date  DATE
                );
    """
            )
            
            # connection.commit()
            print("[INFO] Table created successfully")
    
    def write(self, table: str, columns: str, values: str) -> bool:
        with self.connection.cursor() as cursor:
            cursor.execute(f"""INSERT INTO {table} ({columns}) VALUES ({values});""")
            return 1
        return 0

    def read(self, table: str, columns: str, requirement: str = ""):
        try:
            if requirement:
                requirement = "WHERE " + requirement
            query = f"""SELECT {columns} FROM {table} {requirement}"""
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except:
            return 0
    
    def read_one(self, table, param):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"""SELECT {param} FROM {table}""")
                return cursor.fetchone()
        except:
            return 0

    def delete(self, table, column, values):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM {table} WHERE {column} = '{values}'")
                return 1
        except:
            return 0

    def close(self):
        self.connection.close()
        print("[INFO] PostgreSQL connection closed")

    

db = DB()
db.create_db()
db.write('tg_user', 'tg_id,ref', '42,12345678')
print(db.read('tg_user','tg_id'))

import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('name', 'Alice')
name = r.get('name')
print(name)