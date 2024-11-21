# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files

datas = []
datas += collect_data_files('gradio')  # The frontend files must be bundled.
datas += collect_data_files('gradio_client')  # `gradio_client/types.json` must be bundled.


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[
        './runtime_hooks/gradio_hook.py'
    ],
    excludes=[],
    noarchive=False,
    optimize=0,
    module_collection_mode={
        # `create_or_modify_pyi()` which is used in https://github.com/gradio-app/gradio/blob/29cfc03ecf92e459c538b0e17e942b0af4f5df4c/gradio/blocks_events.py#L20
        # reads `*.py` files in https://github.com/gradio-app/gradio/blob/29cfc03ecf92e459c538b0e17e942b0af4f5df4c/gradio/component_meta.py#L108,
        # so we must collect `gradio` package as source .py files.
        # TODO: Skip *.pyi file generation when the app is packaged with PyInstaller.
        'gradio': 'py',  # Collect gradio package as source .py files
    },
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
