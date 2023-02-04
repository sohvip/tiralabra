from run import Run


def main():
    """Starts the application.
    """
    run = Run()
    run.start()
    retry = True
    while retry is True:
        retry = run.again()


if __name__ == "__main__":
    main()
