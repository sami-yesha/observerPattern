# app.py
from flask import Flask, render_template, request, jsonify

class Observer:
    def update(self, message: str):
        pass

class Subscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message: str):
        print(f"{self.name} received message: {message}")

class Subject:
    def __init__(self):
        self._observers = []

    def register(self, observer: Observer):
        self._observers.append(observer)

    def unregister(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

app = Flask(__name__)

publisher = Subject()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    name = request.json['name']
    subscriber = Subscriber(name)
    publisher.register(subscriber)
    return jsonify({"message": f"{name} subscribed successfully!"})

@app.route('/publish', methods=['POST'])
def publish():
    message = request.json['message']
    publisher.notify(message)
    return jsonify({"message": "Notification sent to all subscribers!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
