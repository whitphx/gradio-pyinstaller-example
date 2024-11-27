# gradio-pyinstaller-example

## General

After installing `gradio` and `pyinstaller` run the following commands to create a standalone executable.
```shell
$ pyinstaller app.py \
    --collect-data gradio \
    --collect-data gradio_client \
    --additional-hooks-dir=./hooks \
    --runtime-hook ./runtime_hooks/gradio_hook.py
```
The executable will be in the `dist` directory.
```shell
$ ./dist/app/app
```

* `runtime_hooks/gradio_hook.py` is a necessary runtime hook for `gradio` to work in the packaged executable. See its contents for more information.


## Development with `uv`

This sample repo uses `uv` to manage the project. To install the dependencies and run the command above through `uv`, run the following commands.
```shell
$ uv sync
$ uv run pyinstaller app.py \
    --collect-data gradio \
    --collect-data gradio_client \
    --additional-hooks-dir=./hooks \
    --runtime-hook ./runtime_hooks/gradio_hook.py
$ ./dist/app/app
```
