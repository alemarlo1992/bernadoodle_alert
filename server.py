from litter_check import *
from os import environ
from flask import Flask
# import schedule 
# import time 
# import logging
import threading

app = Flask(__name__)

port = int(environ.get('PORT', 5000))

if __name__ == "__main__":

    checking_pup_thread = threading.Thread(target=checking_pup)
    checking_pup_thread.start()
    print("After thread")

    app.run(host='0.0.0.0', port=port)
    print('After app ran')
