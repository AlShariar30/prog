print("Program starting.")


word = input("\nInsert a closed compound word: ").strip()


if not word:
    print("You must insert a word.")
else:
    print(f"\nThe word you inserted is '{word}' and in reverse it is '{word[::-1]}'.")
    print(f"The inserted word length is {len(word)}")
    print(f"Last character is '{word[-1]}'")

    print("\nTake substring from the inserted word by inserting...")
    try:
        start_index = int(input("1) Starting point: "))
        end_index = int(input("2) Ending point: "))
        step_size = int(input("3) Step size: "))

        substring = word[start_index:end_index:step_size]
        print(f"\nThe word '{word}' sliced to the defined substring is '{substring}'.")
    except ValueError:
        print("Please enter valid integer values for indices and step size.")
    except IndexError:
        print("Index out of range. Please enter valid starting and ending points.")

print("Program ending.")
