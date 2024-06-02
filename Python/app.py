from flask import Flask, render_template, request, jsonify
import json
import os
import shutil

app = Flask(__name__)

CONFIG_FILE = "D:/CODING/Programming Languages/JSON/config.json"
BACKUP_FILE = CONFIG_FILE + ".bak"

def read_config():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

def write_config(config):
    with open(CONFIG_FILE, "w") as file:  # Corrected line
        json.dump(config, file, indent=4)

def backup_config():
    shutil.copy(CONFIG_FILE, BACKUP_FILE)

@app.route("/")
def index():
    config = read_config()
    return render_template("index.html", config=config)

@app.route("/update", methods=["POST"])
def update():
    data = request.json
    environment = data.get("environment")
    section = data.get("section")
    key = data.get("key")
    value = data.get("value")

    config = read_config()
    if environment in config and section in config[environment]:
        config[environment][section][key] = value
        backup_config()
        write_config(config)
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 400

@app.route("/backup", methods=["GET"])
def backup():
    backup_config()
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
