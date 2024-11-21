# This is the hook patching the `multiprocessing.freeze_support` function,
# which we must import before calling `multiprocessing.freeze_support`.
import PyInstaller.hooks.rthooks.pyi_rth_multiprocessing  # noqa: F401

if __name__ == "__main__":
    # This is necessary to prevent an infinite app launch loop.
    import multiprocessing
    multiprocessing.freeze_support()
