import logging
import subprocess
import time

import webview

logger = logging.getLogger(__name__)


def wait_for_url(url: str, max_retries: int = 30, retry_interval: int = 1):
    import urllib.request
    import urllib.error

    for _ in range(max_retries):
        try:
            urllib.request.urlopen(url)
            break
        except urllib.error.URLError:
            time.sleep(retry_interval)
    else:
        raise Exception(f"Failed to connect to {url} after {max_retries * retry_interval} seconds")


app_script = "gradio_app.py"

if __file__ == app_script:
    exit("Please run this script from the main directory")

logger.info("Starting Gradio app. %s", app_script)
p = subprocess.Popen(['python', app_script])

gradio_url = "http://localhost:7860/"

wait_for_url(gradio_url)

logger.info("Starting webview")
webview.create_window('Hello world', gradio_url)
webview.start(debug=True)

logger.info("Terminating Gradio app")
p.terminate()
