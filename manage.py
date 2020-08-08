from flask_script import Manager, Server
from apps import create_app


app = create_app(config_name="develop")

manager = Manager(app)

manager.add_command("runserver", Server(use_reloader=True,use_debugger=True,host="192.168.31.100", port=5000))

if __name__ == "__main__":
    manager.run()