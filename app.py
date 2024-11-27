import logging

import webview

logger = logging.getLogger(__name__)

WINDOW_TITLE = "Gradio App"

logger.info("Starting Gradio app")
from gradio_app import demo
demo.launch(prevent_thread_lock=True)

logger.info("Starting webview")
webview.create_window(WINDOW_TITLE, demo.local_url)
webview.start()
