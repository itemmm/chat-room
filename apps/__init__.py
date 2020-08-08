from flask import Flask, render_template
from exts.cors import cors
from exts.avatars import avatars
from exts.socketio import socketio
from apps.config import config


def create_app(config_name):
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    app.config.from_object(config[config_name])

    cors.init_app(app)
    avatars.init_app(app)
    socketio.init_app(app)

    @app.route("/", methods=["GET"], endpoint="index")
    def index():
        return render_template("index.html")

    from apps.chat.views import chat
    app.register_blueprint(chat)


    return app