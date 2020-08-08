from flask import Blueprint,request
from exts.socketio import socketio
from flask_socketio import emit, join_room
from exts.avatars import avatars

chat = Blueprint("chat", __name__, url_prefix="/chat")


room = "chat room demo"

# 监听 socket 连接
@socketio.on("connect", namespace="/chat")
def handle_connect():
    # 加入聊天室
    join_room(room)


# 接收前端 socket 发送的消息
@socketio.on("message", namespace="/chat")
def handle_message(data):
    message = data.get("message")
    nickname = data.get("nickname")
    # 根据昵称生成头像
    avatar = avatars.robohash(nickname)
    mes = {
        "nickname": nickname,
        "avatar": avatar,
        "message": message
    }
    # 发送消息到聊天室
    emit("message", mes, room=room)

