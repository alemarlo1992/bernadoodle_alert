from litter_check import puppy_alert, checking_pup
from os import environ
from flask import Flask

app = Flask(__name__)

port = int(os.environ.get('PORT', 5000)

puppy_alert()

if __name__ == "__main__":
    app.run(environ.get(host='0.0.0.0', port=port))
