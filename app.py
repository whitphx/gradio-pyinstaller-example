import logging

import webview

logger = logging.getLogger(__name__)

from gradio_app import demo
demo.launch(prevent_thread_lock=True)

gradio_url = "http://localhost:7860/"

logger.info("Starting webview")
webview.create_window('Hello world', gradio_url)
webview.start()

logger.info("Terminating Gradio app")
