import string


def word_frequency(text):
    # Convert the text to lowercase
    text = text.lower()

    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words
    words = text.split()

    # Create a dictionary to store word frequencies
    word_freq = {}

    # Count the frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq


def display_word_frequencies(word_freq):
    print("Word Frequencies:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")


# Get text input from the user
user_input = input("Enter some text: ")

# Calculate word frequencies
word_freq = word_frequency(user_input)

# Display word frequencies
display_word_frequencies(word_freq)