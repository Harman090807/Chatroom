from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# When a client sends a message
@socketio.on('send_message')
def handle_message(data):
    # Broadcast message to all clients
    emit('message', data, broadcast=True)

@app.route('/')
def index():
    return render_template('index.html')  # simple frontend

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
