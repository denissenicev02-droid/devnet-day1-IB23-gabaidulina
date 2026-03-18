from flask import Flask
from flask import request
import hashlib, os

sample = Flask(__name__)

TOKEN_HASH8 = hashlib.sha256(os.environ.get("STUDENT_TOKEN", "").encode()).hexdigest()[:8]

@sample.route("/")
def main():
    return f"You are calling me from {request.remote_addr}\nTOKEN_HASH8={TOKEN_HASH8}\n"

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080, threaded=False)
