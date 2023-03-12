import sys
import threading
import webview
from flask_migrate import upgrade
from app import app


def start_server():
    app.run(host="0.0.0.0", port=8080, debug=False)


if __name__ == "__main__":
    with app.app_context():
        upgrade(directory="./migrations")

    thread = threading.Thread(target=start_server)
    thread.daemon = True
    thread.start()

    webview.create_window("French Learning Tool", "http://localhost:8080")
    webview.start()
    sys.exit()
