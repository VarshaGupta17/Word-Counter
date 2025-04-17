def count_words(text):
    """
    Counts the number of words in the given text.
    """
    words = text.strip().split() # Split the text by spaces
    return len(words) # Return the number of words

def main():
    print("Welcome to the Word Counter Program!")

    # Prompt user input
    user_input = input("Please enter a sentence or paragraph: ")

    # Error Handling
    if not user_input.strip():
        print("Error: You entered an empty string. Please try again.")
        return

    # Count words
    word_count = count_words(user_input)

    # Output Display
    print(f"\nWord Count: {word_count}")

# Run the program
if __name__ == "__main__":
    main()
