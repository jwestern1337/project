# import required libraries
import os, json, string, random, threading, ctypes, threading, sqlite3
from os import system
from time import sleep
from database import user_db, song_db


class COLOR: # color classes using ansi escape sequences, "borrowed" from https://github.com/sqlmapproject/sqlmap/blob/master/lib/core/enums.py
    BLUE = "\033[34m"
    BOLD_MAGENTA = "\033[35;1m"
    BOLD_GREEN = "\033[32;1m"
    BOLD_LIGHT_MAGENTA = "\033[95;1m"
    LIGHT_GRAY = "\033[37m"
    BOLD_RED = "\033[31;1m"
    BOLD_LIGHT_GRAY = "\033[37;1m"
    YELLOW = "\033[33m"
    DARK_GRAY = "\033[90m"
    BOLD_CYAN = "\033[36;1m"
    LIGHT_RED = "\033[91m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    LIGHT_MAGENTA = "\033[95m"
    LIGHT_GREEN = "\033[92m"
    RESET = "\033[0m"
    BOLD_DARK_GRAY = "\033[90;1m"
    BOLD_LIGHT_YELLOW = "\033[93;1m"
    BOLD_LIGHT_RED = "\033[91;1m"
    BOLD_LIGHT_GREEN = "\033[92;1m"
    LIGHT_YELLOW = "\033[93m"
    BOLD_LIGHT_BLUE = "\033[94;1m"
    BOLD_LIGHT_CYAN = "\033[96;1m"
    LIGHT_BLUE = "\033[94m"
    BOLD_WHITE = "\033[97;1m"
    LIGHT_CYAN = "\033[96m"
    BLACK = "\033[30m"
    BOLD_YELLOW = "\033[33;1m"
    BOLD_BLUE = "\033[34;1m"
    GREEN = "\033[32m"
    WHITE = "\033[97m"
    BOLD_BLACK = "\033[30;1m"
    RED = "\033[31m"


def setup():
    if os.path.isfile("users.db"):
        return
    else:
        print(f"No user database found.\nCreating one now.")
        user_db().create_table()
        user_db().add_user("admin", "admin", 0, True)
        print(f"User database created.\nAdmin account created (username: admin, password: admin)\n")
        sleep(1)
    if os.path.isfile("songs.db"):
        return
    else:
        print(f"No song database found.\nCreating one now.")
        song_db().create_table()
        print(f"Song database created.\nPlease add some songs once you have logged in.")
        sleep(1)

class user:
    score = 0
    username = ""

class Login:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.score = 0
        self.admin = False
    
    def login(self):
        users = user_db()
        username = input("Username: ")
        password = input("Password: ")
        if username == '' or password == '':
            print("Username or password cannot be empty!")
            return False
        if users.get_user(username) == None:
            print("Username does not exist!")
            return False
        if users.get_user(username):
            if users.get_user(username)[1] == password:
                self.username = username
                self.password = password
                self.score = users.get_player_score(self.username)
                user.score = self.score
                user.username = self.username
                self.admin = True if users.get_user(username)[3] == 1 else False
                return True
            else:
                print("Password is incorrect!")
                sleep(1.5)
                self.login()
    def register(self):
        users = user_db()
        username = input("Username: ")
        password = input("Password: ")
        is_admin = input("Admin (y/n): ")
        if is_admin == 'y':
            users.add_user(username, password, 0, True)
        else:
            users.add_user(username, password, 0, False)
    
    def logout(self):
        self.username = ''
        self.password = ''
        self.score = 0
        self.admin = False
        self.login()

def title(message):
    while True:
        for i in range(len(message)+1):
            ctypes.windll.kernel32.SetConsoleTitleW(message[:i])
            sleep(0.1)
        for i in range(len(message)+1):
            ctypes.windll.kernel32.SetConsoleTitleW(message[i:])
            sleep(0.1)


class Game:
    def __init__(self):
        self.songs = song_db()
        self.conn = sqlite3.connect("users.db")
        self.c = self.conn.cursor()

    def get_song(self):
        song = self.songs.get_random_song()
        return song[0], song[1]

    def add_score(self, username):
        cone = sqlite3.connect("users.db")
        c = cone.cursor()
        c.execute("UPDATE users SET score = score + 1 WHERE name = ?", (username,))
        cone.commit()
    
    def play(self):
        stop = False
        song = self.get_song()
        print(F"Artist: {song[1]}")
        print(F"Song:")
        for word in song[0].split():
            print(f"{word[0]}{'-'*int(len(word)-1) if len(word) >= 1 else ' '}", end=" ")
        if stop != True:
            guess = input("\nGuess: ")
            if guess.lower() == song[0].lower():
                user.score += 1
                self.add_score(user.username)
                print(f"Correct!\nScore: {user.score}")
                again = input("Play again? (y/n): ")
                if again.lower() == 'y':
                    self.play()
                else:
                    print("Thanks for playing!")
                    sleep(1)
                    return
            else:
                print("Incorrect!")

            

class Main:
    def __init__(self):
        self.login = Login()
        self.game = Game()
        self.db = user_db()
        self.login.login()

    def leaderboard(self):
        print("Leaderboard:")
        for user in self.db.get_high_scores():
            print(f"{user[0]}: {user[2]}")
        input("Press enter to continue...")
        
    def main(self):
        threading.Thread(target=title, args=(f"Music guessing game - Logged in as: {user.username} - Score: {user.score}",)).start()
        while True:
            try:
                system('cls' if os.name == 'nt' else 'clear')
                print(f"""{self.login.username}'s score: {user.score}
{COLOR.CYAN}╔╦╗╔═╗╦╔╗╔  {COLOR.LIGHT_MAGENTA}╔╦╗╔═╗╔╗╔╦ ╦
{COLOR.CYAN}║║║╠═╣║║║║  {COLOR.LIGHT_MAGENTA}║║║║╣ ║║║║ ║
{COLOR.CYAN}╩ ╩╩ ╩╩╝╚╝  {COLOR.LIGHT_MAGENTA}╩ ╩╚═╝╝╚╝╚═╝
{COLOR.LIGHT_GREEN}====== music guessing game ======
{COLOR.YELLOW}1. play the game
2. logout
3. leaderboard
4. register a user (admin only)
5. delete a user (admin only)
6. list all users (admin only)
7. add a song (admin only)
8. delete a song (admin only)
9. list all songs (admin only)
10. exit{COLOR.RESET}
            """)
                choice = input("Choice: ")
                if choice == '1':
                    self.game.play()
                elif choice == '2':
                    self.login.logout()
                elif choice == '3':
                    self.leaderboard()
                elif choice == '4':
                    if self.login.admin:
                        self.login.register()
                    else:
                        print("You are not an admin!")
                        sleep(1.5)
                elif choice == '5':
                    if self.login.admin:
                        username = input("Username: ")
                        self.db.delete_user(username if username != self.login.username else print("You cannot delete yourself!"))
                        sleep(1.5)
                    else:
                        print("You are not an admin!")
                        sleep(1.5)
                elif choice == '6':
                    if self.login.admin:
                        print(self.db.get_all_users())
                        sleep(1.5)
                    else:
                        print("You are not an admin!")
                        sleep(1.5)
                elif choice == '7':
                    if self.login.admin:
                        song = input("Song: ")
                        artist = input("Artist: ")
                        song_db().add_song(song, artist)
                        print("Song added!")
                        sleep(1.5)
                    else:
                        print("You are not an admin!")
                        sleep(1.5)
                elif choice == '8':
                    if self.login.admin:
                        song = input("Song: ")
                        song_db().delete_song(song)
                        print("Song deleted!")
                        sleep(1.5)
                    else:
                        print("You are not an admin!")
                        sleep(1.5)
                elif choice == '9':
                    if self.login.admin:
                        print(song_db().get_all_songs())
                        sleep(1.5)
                    else:
                        print("You are not an admin!")
                        sleep(1.5)
                elif choice == '10':
                    print("Thanks for playing!")
                    os._exit(0)
                else:
                    print("Invalid choice!")
                    sleep(1.5)
            except KeyboardInterrupt:
                print("Thanks for playing!")
                os._exit(1)

setup()
Main().main()
