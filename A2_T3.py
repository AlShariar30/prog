print("Program starting.")

first_word = input("Insert first word: ")
second_word = input("Insert second word: ")

first_Word_length = len(first_word)
second_Word_length = len(second_word)

compound_word = first_word + second_word

print(f"1st word is {first_Word_length} characters long.")
print(f"2nd word is {second_Word_length} characters long.")
print(f"Words together makes one closed compound '{compound_word}'.")
print("Program ending.")
