import sys
import threading
import webview
from app import app


def start_server():
    app.run(host='0.0.0.0', port=8080, debug=False)


if __name__ == '__main__':
    thread = threading.Thread(target=start_server)
    thread.daemon = True
    thread.start()

    webview.create_window("French Learning Tool", "http://localhost:8080")
    webview.start()
    sys.exit()
