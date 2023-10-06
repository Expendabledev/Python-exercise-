def total_sum():
    numbers = input("Enter numbers separated by spaces: ").split()
    try:
        numbers = [float(num) for num in numbers]
        total = sum(numbers)
        print(f"The sum of the numbers is: {total}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def word_search():
    text = input("Enter a sentence or text: ")
    word = input("Enter a word to search for: ")
    if word in text:
        print(f"The word '{word}' was found in the text.")
    else:
        print(f"The word '{word}' was not found in the text.")

while True:
    print("\nMain Menu:")
    print("choice1. Calculate Sum")
    print("choice2. Search for Word")
    print("choice3. Quit the program")

    choice = input("Enter your choice (choice.1/choice2/choice3): ")

    if choice == "1":
        total_sum()
    elif choice == "2":
        word_search()
    elif choice == "3":
        print("Goodbye! Thank you for using the program.")
        break
    else:
        print("Incorrect choice. Please select a valid option.")
