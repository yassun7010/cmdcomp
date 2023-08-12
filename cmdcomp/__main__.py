from cmdcomp.app import App


def main() -> None:
    try:
        App.run()
    except Exception:
        exit(1)


if __name__ == "__main__":
    main()
