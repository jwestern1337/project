import sqlite3,random


class song_db:
    def __init__(self):
        self.conn = sqlite3.connect("songs.db")
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS songs (
                        name text,
                        artist text)""")
        self.conn.commit()

    def add_song(self, name, artist):
        # add a song to the table
        self.c.execute("INSERT INTO songs VALUES (?, ?)", (name, artist))
        self.conn.commit()
    
    def get_all_songs(self):
        # get all songs from the table
        self.c.execute("SELECT * FROM songs")
        return self.c.fetchall()
    
    def get_random_song(self):
        # get a random song from the table
        self.c.execute("SELECT * FROM songs")
        songs = self.c.fetchall()
        return random.choice(songs)

    def delete_song(self, name):
        # delete a song from the table
        self.c.execute("DELETE FROM songs WHERE name = ?", (name,))
        self.conn.commit()



class user_db:
    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS users (
                        name text,
                        password text,
                        score integer,
                        admin boolean)""")
        self.conn.commit()
    
    def add_user(self, name, password, score, admin):
        # add a user to the table
        self.c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (name, password, score, admin))
        self.conn.commit()
        print("User added.")
    
    def get_all_users(self):
        # get all users from the table
        self.c.execute("SELECT * FROM users")
        return self.c.fetchall()

    def get_user(self, name):
        # return all the users data
        self.c.execute("SELECT * FROM users WHERE name = ?", (name,))
        return self.c.fetchone()
    
    def delete_user(self, name):
        # delete a user from the table
        self.c.execute("DELETE FROM users WHERE name = ?", (name,))
        self.conn.commit()
        print("User deleted.")
    
    def get_high_scores(self):
        # return the top 10 players and their scores in a list
        self.c.execute("SELECT * FROM users ORDER BY score DESC LIMIT 10")
        return self.c.fetchall()

    def get_player_score(self, name):
        self.c.execute("SELECT score FROM users WHERE name = ?", (name,))
        return self.c.fetchone()[0]

    def is_admin(self, name):
        # return whether a player is an admin
        self.c.execute("SELECT admin FROM users WHERE name = ?", (name,))
        return self.c.fetchone()[0]

    def get_password(self, name):
        # return the password of a player
        self.c.execute("SELECT password FROM users WHERE name = ?", (name,))
        return self.c.fetchone()[0]

    def add_score(self, name, amount):
        score = int(self.get_player_score(name)) + amount
        self.c.execute("UPDATE users SET score = ? WHERE name = ?", (score, name))
        self.conn.commit()
