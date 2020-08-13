from litter_check import *
from os import environ
from flask import Flask
import threading

app = Flask(__name__)

port = int(environ.get('PORT', 5000))

if __name__ == "__main__":
    print("Starting server")

    checking_pup_thread = threading.Thread(target=checking_pup)
    checking_pup_thread.start()

    app.run(host='0.0.0.0', port=port)

