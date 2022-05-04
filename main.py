# import required libraries
import os, json, string, random, threading, ctypes
from os import system
from time import sleep

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



def setup(): # if creds.json doesn't exist then create it with a username and password
    if os.path.exists('creds.json'):
        return True
    else:
        print("No username or password file found. Please create a user")
        username = input("Username: ")
        password = input("Password: ")
        admin = input("Admin[yes/no]? ")
        if admin != 'yes':
            if admin != 'no':
                print("Please enter either 'yes' or 'no' next time!")
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
                with open('creds.json', 'w') as f:
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
        print(f"Artist: {play.artist}")
        print(f"First letter of the song is: ")
        for word in play.song_name.split():
            print(f"{word[0]}{'-'*int(len(word)-1) if len(word) >= 1 else ' '}", end=" ")
        print("")
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
                pass
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
    with open(f'creds.json', 'r') as f:
        cfg = json.load(f)
        try:
            cfg[Encryption.encrypt(username)][Encryption.encrypt('username')]
        except:
            stuff.login_tries += 1
            print("This user does not exist!")
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
        print("Password does not match user!")
        input()
        login()

def menu():
    print("hi")

setup()
login()
play.play()