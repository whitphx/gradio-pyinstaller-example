import webview

from gradio_app import demo


demo.launch(prevent_thread_lock=True)

webview.create_window("Gradio App", demo.local_url)
webview.start()
