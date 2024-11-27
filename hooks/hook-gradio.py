module_collection_mode = {
    # `create_or_modify_pyi()` which is used in https://github.com/gradio-app/gradio/blob/29cfc03ecf92e459c538b0e17e942b0af4f5df4c/gradio/blocks_events.py#L20
    # reads `*.py` files in https://github.com/gradio-app/gradio/blob/29cfc03ecf92e459c538b0e17e942b0af4f5df4c/gradio/component_meta.py#L108,
    # so we must collect `gradio` package as source .py files.
    # TODO: Skip *.pyi file generation when the app is packaged with PyInstaller.
    'gradio': 'py',  # Collect gradio package as source .py files
}
