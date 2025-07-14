from watchgod import run_process


def run_with_reload() -> None:
    from .main import main
    run_process('src', lambda: main())


if __name__ == '__main__':
    run_with_reload()
