from emoji import emojize


def main():
    # get the user input
    user_input = input("Input: ").strip()

    # print the user input with the given emoji
    print("Output: " + emojize(user_input, language="alias"))


if __name__ == "__main__":
    main()
