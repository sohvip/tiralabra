from run import Run

def main():
    run = Run()
    run.start()
    retry = True
    while retry == True:
        retry = run.again()

if __name__ == "__main__":
    main()