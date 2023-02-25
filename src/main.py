from run import Run


def main():
    """Starts the application.
    """
    run = Run()
    song = run.start()
    retry = True
    while retry is True:
        retry = run.again(song)


if __name__ == "__main__":
    main()
