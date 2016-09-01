"""
Accepts an input and prints each word and their number of occurrences (incompatible with punctuation, e.g. commas and
full stops)
"""
__author__ = 'Gareth'


def main():
    text = input("Text: ").lower()
    word_counts = calculate_the_number_of_occurrences(text)
    max_word_length, unique_words = find_the_length_of_the_longest_value_and_list_the_keys(word_counts)
    print_sorted_dictionary_in_column_format(max_word_length, unique_words, word_counts)


def print_sorted_dictionary_in_column_format(max_word_length, unique_words, word_counts):
    # Sorted() sorts the value in preparation of printing the values alphabetically
    for word in sorted(unique_words):
        if word != "":
            print("{:<{}} : {}".format(word, max_word_length, word_counts.get(word)))


def find_the_length_of_the_longest_value_and_list_the_keys(word_counts):
    max_word_length = 0
    unique_words = []
    for word in word_counts:
        # Find the longest word by going through each word, checking if it's the biggest so far
        if len(word) > max_word_length:
            max_word_length = len(word)
        # Add each word from the dictionary to the list unique_words
        try:
            unique_words += [word]
        except KeyError:
            unique_words = word
    return max_word_length, unique_words


def calculate_the_number_of_occurrences(text):
    """After splitting the words up, the number of occurrences of each word is calculated and entered into the
    dictionary word_counts"""
    word_counts = {}
    text_words = text.split(" ")
    for i in text_words:
        word_counts[i] = word_counts.get(i, 0) + 1
    return word_counts


if __name__ == "__main__":
    main()
