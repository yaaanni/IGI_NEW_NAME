# Purpose: Implementation of Task 4.  Analyzing a predefined text string.
# Lab: #3 - Standard Data Types, Collections, Functions, Modules.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 18.03.2026.

from utils.decorators import timer_decorator

SOURCE_TEXT = (
    "So she was considering in her own mind, as well as she could, "
    "for the hot day made her feel very sleepy and stupid, whether "
    "the pleasure of making a daisy-chain would be worth the trouble "
    "of getting up and picking the daisies, when suddenly a White "
    "Rabbit with pink eyes ran close by her."
)


def get_cleaned_words(text):
    """
    Cleans the text from commas and splits it into a list of words.

    Args:
        text (str): The raw string to process.

    Returns:
        list: A list of words without punctuation marks.
    """

    clean_text = text.replace(',', ' ')

    words = clean_text.split()

    return words


def find_longest_word(words):
    """
    Identifies the longest word and its 1-based index in the list.

    Args:
        words (list): The list of words to analyze.

    Returns:
        tuple: (longest_word, index) where index starts from 1.
    """

    longest = ""
    index = 0

    for i, word in enumerate(words):
        if len(word) > len(longest):
            longest = word
            index = i + 1

    return longest, index


@timer_decorator
def run_task_4():
    """
    Executes the business logic for Task 4.  Displays text analysis.

    This function performs three sub-tasks: counts words, finds the
    longest word with its position, and outputs every odd word.
    """
    print("\n--- Task 4: Alice in Wonderland Text Analysis ---")

    words = get_cleaned_words(SOURCE_TEXT)

    word_count = len(words)
    print(f"a) Total number of words: {word_count}.")

    long_word, pos = find_longest_word(words)
    print(f"b) Longest word: '{long_word}' (Position: {pos}).")

    odd_words = words[::2]
    print(f"c) Every odd word in the sequence:")
    print(", ".join(odd_words) + ".")
