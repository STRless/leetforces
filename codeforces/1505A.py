import sys


def main():
    while True:
        try:
            s = input()
        except EOFError:
            break
        print("no", flush=True)


if __name__ == "__main__":
    main()