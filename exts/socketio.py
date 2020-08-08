from flask_socketio import SocketIO


# cors_allower_origins="*" 用于处理 socketio 跨域
socketio = SocketIO(cors_allower_origins="*")