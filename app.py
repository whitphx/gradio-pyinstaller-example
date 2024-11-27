import webview

from gradio_app import demo as gradio_app

gradio_app.launch(prevent_thread_lock=True)

webview.create_window("Gradio App", gradio_app.local_url)
webview.start()
