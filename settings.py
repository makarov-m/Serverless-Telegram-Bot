#### reads credentials from global variable

import os

path = os.getcwd()

try:
    with open(f'.env', 'r') as file:
        # read all lines in file
        lines = file.readlines()
        # read fist row
        os.environ[lines[0].split(' = ')[0]] = lines[0].split(' = ')[1].replace('\n','')
        TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

except:
    print("You don't have .env file with credentials")



