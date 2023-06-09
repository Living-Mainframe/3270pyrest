import threading, configparser
from flask import Flask, jsonify, request
from functions.version import GetVersion
from functions.queue import GetQueue

app = Flask(__name__)
lock = threading.Lock()

functions = {"version": GetVersion, "queue": GetQueue}

config = configparser.ConfigParser()
config.read("config.ini")
hostname = config.get("connection", "hostname")
username = config.get("connection", "username")
password = config.get("connection", "password")

@app.route('/<page>')
def show(page):
    if page in functions.keys():
        with lock:
            try:
                emulator = functions[page](hostname, username, password)
                emulator.logon()
                result, status = emulator.run()
                emulator.logoff()
                return jsonify({"message": "Program executed successfully", "result": result}), 200
            except Exception as e:
                return jsonify({"message": "Program not executed successfully", "result": str(e)}), 500
    else:
        return jsonify({"message": "Program not executed successfully"}), 404

if __name__ == '__main__':
    app.run(debug=True)
