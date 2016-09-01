"""
Accepts an input and prints each word and their number of occurrences (incompatible with punctuation, e.g. commas and
full stops)
"""
__author__ = 'Gareth'


def main():
    word_counts = {}
    unique_words = []
    max_word_length = 0
    text = input("Text: ").lower()
    """After splitting the words up, the number of occurrences of each word is calculated and entered into the
    dictionary word_counts"""
    text_words = text.split(" ")
    for i in text_words:
        word_counts[i] = word_counts.get(i, 0) + 1
    for word1 in word_counts:
        # Find the longest word by going through each word, checking if it's the biggest so far
        if len(word1) > max_word_length:
            max_word_length = len(word1)
        # Add each word from the dictionary to the list unique_words
        try:
            unique_words += [word1]
        except KeyError:
            unique_words = word1
    # Sorted() sorts the value in preparation of printing the values alphabetically
    for word3 in sorted(unique_words):
        if word3 != "":
            print("{:<{}} : {}".format(word3, max_word_length, word_counts.get(word3)))


if __name__ == "__main__":
    main()
