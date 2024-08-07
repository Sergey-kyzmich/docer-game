import sqlite3

class database():
    def __init__(self) -> None:
        pass


    def add_user(self, user):
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute(f'INSERT INTO user VALUES (?,?,?)', (user["name"], user["money"], user["level"]))
        db.commit()
        print(f"add {user}")

        db.close()



    def create_db(self):
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS user (
        name STRING PRIMARY KEY,
        money INTEGER,
        level STRING
        )
        ''')
        db.commit()
        db.close()
    
    
    def edit(self, data):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        for item in data:
            cursor.execute(f'''UPDATE user SET {item} = "{data[item]}" WHERE name = "{data["name"]}"''')
            db.commit()
        db.close()
    
    def get_all(self):
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        res = cursor.execute(f"SELECT * FROM user")
        a = []
        for item in res:
            a.append(item)
        return a

    def get_line(self, name):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        res = cursor.execute(f'SELECT * FROM user WHERE name = "{name}"')
        for i in res:
            
            db.close()
            return i
        
        
