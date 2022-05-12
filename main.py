# import required libraries
import os, json, string, random, threading, ctypes, threading
from os import system
from time import sleep

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


def title(): # ugly animated title code ahhhhhhhhhh
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW("m")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("mu")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("mus")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("musi")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music ")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music g")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music gu")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music gues")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guess")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessi")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessing")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessing ")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessing g")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessing ga")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessing gam")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessing game")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessing gam")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessing ga")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessing g")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessing ")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessing")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessin")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guessi")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music guess")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music gues")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music gue")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music gu")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music g")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music ")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("music")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("musi")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("mus")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("mu")
        sleep(0.1)
        ctypes.windll.kernel32.SetConsoleTitleW("m")
        sleep(0.1)

threading.Thread(target=title).start()

# class holding both the encryption and decryption algorithim, they use a encryption method called caeser shift
# caeser shift takes each letter in the given string and replaces it with the next letter in the alphabet (after the given key(shift))
# e.g. with a shift of 4 places, "abc" would become "efg"
class Encryption:
    def encrypt(message, key=7): # key = shift
        message = message.upper()
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = "10987654321"
        result = ""

        for letter in message:
            if letter in alpha: 
                letter_index = (alpha.find(letter) + key) % len(alpha)

                result = result + alpha[letter_index]
            else:
                result = result + num[letter_index]

        return result

    def decrypt(message, key=7):
        message = message.upper()
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        for letter in message:
            if letter in alpha:
                letter_index = (alpha.find(letter) - key) % len(alpha)

                result = result + alpha[letter_index]
            else:
                result = result + letter

        return result.lower()

# a class to allow for any data that may need storing to be stored
class stuff:
    login_tries = 0
    username = ''
    guesses = 0
    score = 0
    admin = ''


def register():
    username = input("Username: ")
    password = input("Password: ")
    if stuff.admin == True:
        admin = input("Admin[yes/no]? ")
    else:
        admin = False
    data = {
        Encryption.encrypt(username): {
            Encryption.encrypt('username'): Encryption.encrypt(username),
            Encryption.encrypt('password'): Encryption.encrypt(password),
            Encryption.encrypt('admin'): Encryption.encrypt(admin)
        }
    }
    with open(f'creds/{Encryption.encrypt(username)}.json', 'a') as f:
        json.dump(data, f,indent=4)
    print(f"Created user {username} with password {password} and admin = {admin}")
        
    

def delete_user():
    username = input("User to delete: ")
    if username == stuff.username:
        print(f"{COLOR.RED}You cannot delete {username} as you are logged in as them!")
        sleep(3)
        menu()
    else:
        if os.path.exists(f'creds/{Encryption.encrypt(username)}.json'):
            try:
                os.remove(f'creds/{Encryption.encrypt(username)}.json')
                print(f"deleted user {username}")
            except Exception as e:
                print(e)


def setup(): # if creds.json doesn't exist then create it with a username and password
    if os.path.exists('creds'):
        return True
    else:
        os.mkdir('creds')
        print("No username or password file found. Please create a user")
        username = input("Username: ")
        password = input("Password: ")
        admin = input("Admin[yes/no]? ")
        if admin != 'yes':
            if admin != 'no':
                print(f"{COLOR.RED}Please enter either 'yes' or 'no' next time!")
                sleep(3)
                system('cls' if os.name == 'nt' else 'clear')
                login()
        print(f"""
username: {username}
password: {password}
admin: {admin}
""")
        confirm = input("Is this correct[yes/no]? ")
        if confirm != 'yes':
            if confirm != 'no':
                print("Please enter either 'yes' or 'no' next time!")
                sleep(3)
                system('cls' if os.name == 'nt' else 'clear')
                login()
            elif confirm == 'no':
                setup()
        elif confirm == 'yes':
            try:
                username = Encryption.encrypt(username)
                password = Encryption.encrypt(password)
                admin = Encryption.encrypt(admin)
                data = {
                    username: {
                        Encryption.encrypt('username'): username,
                        Encryption.encrypt('password'): password,
                        Encryption.encrypt('admin'): admin
                    }
                }
                with open(f'creds/{username}.json', 'w') as f:
                    json.dump(data, f, indent=4)
                    print("Successfully created a user account, re directing to the main menu is 3 seconds...")
                    sleep(3)
            except Exception as e:
                print(e)
                input()



# the main game function
class play:
    with open('songs.json') as f:
        song = json.load(f)
    artist = random.choice(list(song.keys()))
    choices = ['song name', 'song name2']
    song_name = song[artist][random.choice(choices)]
    def play():
        system('cls' if os.name == 'nt' else 'clear')
        if stuff.guesses >= 5:
            print("Sorry, you ran out guesses")
            sleep(3)
            menu()
        print(f"Artist: {play.artist}")
        print(f"First letter of the song is: ")
        for word in play.song_name.split():
            print(f"{word[0]}{'-'*int(len(word)-1) if len(word) >= 1 else ' '}", end=" ")
        print("")
        print(f"You have {5-int(stuff.guesses)} guesses left")
        guess = input("Guess: ")
        if guess.lower() == play.song_name or guess.upper() == play.song_name:
            print("Congrats, you guessed correctly!")
            again = input("Play again[yes/no]? ")
            if again == 'yes':
                with open('songs.json') as f:
                    play.song = json.load(f)
                play.artist = random.choice(list(play.song.keys()))
                choices = ['song name', 'song name2']
                play.song_name = play.song[play.artist][random.choice(choices)]
                play.play()
            else:
                menu()
        else:
            print("Incorrect!")
            sleep(2)
            stuff.guesses += 1
            play.play()

def login(): # a login function that asks for a username and a password
    if stuff.login_tries >= 3:
        print("Maximum login tries exceeded, goodbye")
        sleep(3)
        os._exit(0)
    system('cls' if os.name == 'nt' else 'clear')
    username = input("Username: ")
    try:
        with open(f'creds/{Encryption.encrypt(username)}.json', 'r') as f:
            cfg = json.load(f)
            cfg[Encryption.encrypt(username)][Encryption.encrypt('username')]
    except FileNotFoundError:
        stuff.login_tries += 1
        print(f"{COLOR.RED}This user does not exist!{COLOR.RESET}")
        sleep(3)
        login()
    password = input("Password: ")
    passw = Encryption.decrypt(cfg[Encryption.encrypt(username)][Encryption.encrypt('password')])
    if password == passw:
        pass
        stuff.username = username
        if Encryption.decrypt(cfg[Encryption.encrypt(username)][Encryption.encrypt('admin')]) == 'yes':
            stuff.admin = True
        else:
            stuff.admin = False
    else:
        stuff.login_tries += 1
        print(f"{COLOR.RED}Password does not match user!")
        sleep(3)
        login()

def menu():
    system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{COLOR.CYAN}╔╦╗╔═╗╦╔╗╔  {COLOR.LIGHT_MAGENTA}╔╦╗╔═╗╔╗╔╦ ╦
{COLOR.CYAN}║║║╠═╣║║║║  {COLOR.LIGHT_MAGENTA}║║║║╣ ║║║║ ║
{COLOR.CYAN}╩ ╩╩ ╩╩╝╚╝  {COLOR.LIGHT_MAGENTA}╩ ╩╚═╝╝╚╝╚═╝
{COLOR.LIGHT_GREEN}====== music guessing game ======
{COLOR.YELLOW}1. play the game
2. logout
3. register a user (admin only)
4. delete a user (admin only)
5. exit{COLOR.RESET}
""")
    choice = input("Choice: ")
    if choice == "1":
        play.play()
    elif choice == "2":
        login()
        menu()
    elif choice == "3":
        if stuff.admin == True:
            register()
            sleep(2)
            menu()
        else:
            print(f"{COLOR.RED}This feature is for admin users only")
            sleep(2)
            menu()
    elif choice == "4":
        if stuff.admin == True:
            delete_user()
            sleep(2)
            menu()
        else:
            print(f"{COLOR.RED}This feature is for admin users only")
            sleep(2)
            menu()
    elif choice == "5":
        os._exit(1)
    else:
        print(f"{COLOR.RED}Please enter a valid option next time")
        sleep(2)
        menu()

setup()
login()
menu()

