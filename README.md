# gradio-pyinstaller-example

## How to package a Gradio app with PyInstaller and PyWebView

1. Assume that you have a Gradio app `demo` in a file named `gradio_app.py`. Make sure that `demo.launch()` is called in the `if __name__ == "__main__"` block so that it's not called when the app is imported when packaged as below.
    ```python
    import gradio as gr


    def greet(name):
        return "Hello " + name + "!!"


    demo = gr.Interface(fn=greet, inputs="text", outputs="text")

    if __name__ == "__main__":
        demo.launch()
    ```
2. Create `app.py` with the following content. This is an entry point for the packaged executable. **Change the import path and the imported object (`from gradio_app import demo`) to your Gradio app.**
    ```python
    import webview

    from gradio_app import demo as gradio_app  # CHANGE THIS LINE

    gradio_app.launch(prevent_thread_lock=True)

    webview.create_window("Gradio App", demo.local_url)  # Change the title if needed
    webview.start()
    ```
3. Add the following files:
    * `runtime_hook.py`
        ```python
        # This is the hook patching the `multiprocessing.freeze_support` function,
        # which we must import before calling `multiprocessing.freeze_support`.
        import PyInstaller.hooks.rthooks.pyi_rth_multiprocessing  # noqa: F401

        if __name__ == "__main__":
            # This is necessary to prevent an infinite app launch loop.
            import multiprocessing
            multiprocessing.freeze_support()
        ```
    * `hooks/hook-gradio.py` - A directory containing PyInstaller hooks for Gradio.
        ```python
        module_collection_mode = {
            # `create_or_modify_pyi()` which is used in https://github.com/gradio-app/gradio/blob/29cfc03ecf92e459c538b0e17e942b0af4f5df4c/gradio/blocks_events.py#L20
            # reads `*.py` files in https://github.com/gradio-app/gradio/blob/29cfc03ecf92e459c538b0e17e942b0af4f5df4c/gradio/component_meta.py#L108,
            # so we must collect `gradio` package as source .py files.
            # TODO: Skip *.pyi file generation when the app is packaged with PyInstaller.
            'gradio': 'py',  # Collect gradio package as source .py files
        }
        ```
4. Install dependencies: `pyinstaller` and `pywebview` for packaging. `gradio` and other dependencies are also required for runtime.
    ```shell
    $ pip install pyinstaller pywebview gradio
    ```
5. Package the app with PyInstaller with the following command:
    ```shell
    $ pyinstaller app.py \
        --collect-data gradio \
        --collect-data gradio_client \
        --additional-hooks-dir=./hooks \
        --runtime-hook ./runtime_hook.py
    ```
    You can add more options to the command as needed. For example, `--onefile` to create a single executable file and/or `--windowed` to hide the console window.
6. The executable will be in the `dist` directory. Run it to see the Gradio app in a PyWebView window.
    ```shell
    $ ./dist/app/app
    ```

## Development with `uv`

This sample repo uses `uv` to manage the project. To install the dependencies and run the command above through `uv`, run the following commands.
```shell
$ uv sync
$ uv run pyinstaller app.py \
    --collect-data gradio \
    --collect-data gradio_client \
    --additional-hooks-dir=./hooks \
    --runtime-hook ./runtime_hook.py
$ ./dist/app/app
```
