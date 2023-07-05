
import argparse
import hashlib
from stegano import lsb
import random
import string
import codecs
from pyfiglet import Figlet
import praw
import json

# Initializing banner

custom_fig = Figlet(font='isometric3')
print(custom_fig.renderText('META'))
print("=================== With <3 by Ch3atk0d3 =====================         ")
print("\n")


# Login function is used while extracting the message from stego file

def login():
    hash = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f" # SHA256 hash of the pre-determined password (Here: password123)
    password = input("[+] Enter password: ")
    password = hashlib.sha256(password.encode()).hexdigest() # hashing the entered password to SHA256 hash
    if password == hash:        # Checking if entered password matches the predetermined password.
        print("[+] Correct password !!!")
        return 1
    else:
        print("[-] Incorrect password. Try again !!!")
        return 0


# Encrypt function is used to hide the message in the image file

def encrypt(message, len1 = 10, len2 = 10):     # function take three arguments out of which length for the random strings is already specilized
    rot = codecs.encode(message, "rot-13")      # encoding the message with rot-13 algorithm
    letters = string.ascii_lowercase
    salt1 = ''.join(random.choice(letters) for i in range(len1))
    salt2 = ''.join(random.choice(letters) for i in range(len2))
    final = salt1 + rot + salt2
    return final    # returns the encoded message along with the two random salt in front and back.



# Decrypt function is used to extract the message from the image file

def decrypt(decrypted):
    decrypted = decrypted[10:-10]   # slices the salt from the message
    final_decrypted = codecs.decode(decrypted, "rot-13")        # decoding the rot-13 algorithm
    return final_decrypted      # returns the decoded string

# Upload function use reddit API to upload the encoded image to specified subreddit.
def upload(subr, title, image):
    credentials = 'clients_secret.json'     # importing credentials from clients_secret.json file
    with open(credentials) as f:
        creds = json.load(f)
    reddit = praw.Reddit(client_id=creds['client_id'],
                         client_secret=creds['client_secret'],
                         username=creds['username'],
                         password=creds['password'],
                         user_agent=creds['user_agent'])

    subreddit = reddit.subreddit(subr)
    subreddit.submit_image(title, image)    # Uploading image to reddit




parser = argparse.ArgumentParser()      # initializing command line arguments using argparse

parser.add_argument("-i", "--input", help="input file", default=None)
parser.add_argument("-o", "--output" ,help="output file", default=None)
args = parser.parse_args()

file_in = args.input
file_out = args.output


if file_in is None:   # This executes for extracting secret message from stego file
    try:
        login_check = login()
        if login_check == 1:
            msg = lsb.reveal(file_out)
            decoded = decrypt(msg)
            print("\n")
            print(f"[+] Secret Message: {decoded}")
        else:
            print("\n")
            print("[-] Unable to decrypt message")
    except Exception as e:
        print(e)

else:       # This executes for embedding secret message in stego file and uploading it to twitter
    message = input("Enter your message: ")
    encoded = encrypt(message)
    secret = lsb.hide(file_in, encoded)
    secret.save(file_out)
    print("[+] Message encrypted")
    print("\n")
    ask_upload = input("[+] Do you want to upload the secret image to reddit ?. Type Y or N: ")
    print("\n")
    print("[+] Please specify the required creds in clients_secret.json file. If Done, Please continue.")
    print("\n")
    if ask_upload == 'Y':
        subr = input("[+] Enter Subreddit: ")
        title = input("[+] Enter Title: ")
        image = input("[+] Enter image Name or path: ")
        upload(subr, title, image)
        print("[+] Image uploaded !!!")
    else:
        print("[-] Exiting without uploading!!!")


