
'''
Author: Bobby Jones
Date: 2/25/25
Description: This program provides various string manipulation functions, including vowel/consonant counting,
             string reversal, checking for hyphenated last names, and more.
Bugs: None
'''
import random

def reverse_string(word):
    """
    Reverses the given string.

    Args:
        word (str): The input string.

    Returns:
        str: The reversed string.
    """
    return word[::-1]

def count_vowels(word):
    """
    Counts the number of vowels in a string (case-insensitive).

    Args:
        word (str): The input string.

    Returns:
        tuple: (total count, dictionary with counts of each vowel).
    """
    vowels = "aeiou"
    vowel_count = {v: 0 for v in vowels}
    
    for char in word.lower():  # Convert to lowercase to treat uppercase and lowercase as the same
        if char in vowels:
            vowel_count[char] += 1

    total_vowels = sum(vowel_count.values())
    return total_vowels, vowel_count

def count_consonants(word):
    """
    Counts the number of consonants in a string (case-insensitive).

    Args:
        word (str): The input string.

    Returns:
        tuple: (total count, dictionary with counts of each consonant).
    """
    consonants = "bcdfghjklmnpqrstvwxyz"
    consonant_count = {c: 0 for c in consonants}
    
    for char in word.lower():  # Convert to lowercase to treat uppercase and lowercase as the same
        if char in consonants:
            consonant_count[char] += 1

    total_consonants = sum(consonant_count.values())
    return total_consonants, consonant_count

def extract_first_name(full_name):
    """
    Extracts the first name from a full name.

    Args:
        full_name (str): The full name.

    Returns:
        str: The first name.
    """
    return full_name.split()[0]

def extract_last_name(full_name):
    """
    Extracts the last name from a full name.

    Args:
        full_name (str): The full name.

    Returns:
        str: The last name.
    """
    return full_name.split()[-1]

def extract_middle_names(full_name):
    """
    Extracts the middle names from a full name.

    Args:
        full_name (str): The full name.

    Returns:
        str: The middle name(s) or an empty string if none exist.
    """
    name_parts = full_name.split()
    return " ".join(name_parts[1:-1]) if len(name_parts) > 2 else ""

def has_hyphenated_last_name(full_name):
    """
    Checks if the last name contains a hyphen.

    Args:
        full_name (str): The full name.

    Returns:
        bool: True if last name has a hyphen, False otherwise.
    """
    return "-" in extract_last_name(full_name)

def to_lowercase(word):
    """
    Converts a string to lowercase.

    Args:
        word (str): The input string.

    Returns:
        str: The lowercase version of the string.
    """
    return word.lower()

def to_uppercase(word):
    """
    Converts a string to uppercase.

    Args:
        word (str): The input string.

    Returns:
        str: The uppercase version of the string.
    """
    return word.upper()

def shuffle_name(word):
    """
    Creates a random permutation of the input string.

    Args:
        word (str): The input string.

    Returns:
        str: A randomized version of the string.
    """
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)

def is_palindrome(word):
    """
    Checks if the first name is a palindrome.

    Args:
        word (str): The input string.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    return word.lower() == word[::-1].lower()

def sort_characters(word):
    """
    Sorts the characters of the input string alphabetically.

    Args:
        word (str): The input string.

    Returns:
        str: A sorted version of the string.
    """
    return "".join(sorted(word))

def make_initials(full_name):
    """
    Creates initials from a full name.

    Args:
        full_name (str): The full name.

    Returns:
        str: The initials of the name.
    """
    return "".join(name[0].upper() for name in full_name.split())

def contains_title(full_name):
    """
    Checks if a name contains a title.

    Args:
        full_name (str): The full name.

    Returns:
        bool: True if the name contains a title, False otherwise.
    """
    titles = [
        'Dr', 'Doctor', 'Reverend', 'Sr', 'Senior', 'Prince', 'King', 'Professor', 'Private',
        'Private second class', 'Private first class', 'Specialist', 'Corporal', 'Sergeant',
        'Staff sergeant', 'Sergeant first class', 'Master sergeant', 'First sergeant',
        'Sergeant major', 'Command sergeant major', 'Second lieutenant', 'First lieutenant',
        'Captain', 'Major', 'Lieutenant colonel', 'Colonel', 'Brigadier general', 'Major general'
    ]
    return any(title in full_name for title in titles)

def menu():
    """Displays a menu for the user to select options and interact with the functions."""
    name = input("Enter your full name or a word: ")

    while True:
        print("\nMenu:")
        print("1. Reverse the string")
        print("2. Count vowels")
        print("3. Count consonants")
        print("4. Get first name")
        print("5. Get last name")
        print("6. Get middle name(s)")
        print("7. Check if last name is hyphenated")
        print("8. Convert to lowercase")
        print("9. Convert to uppercase")
        print("10. Shuffle name")
        print("11. Check if first name is a palindrome")
        print("12. Sort characters")
        print("13. Get initials")
        print("14. Check if name contains a title")
        print("15. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Reversed:", reverse_string(name))
        elif choice == "2":
            total_vowels, vowel_counts = count_vowels(name)
            print(f"Total vowels: {total_vowels}")
            print("Vowel subtotals:", vowel_counts)
        elif choice == "3":
            total_consonants, consonant_counts = count_consonants(name)
            print(f"Total consonants: {total_consonants}")
            print("Consonant subtotals:", consonant_counts)
        elif choice == "4":
            print("First name:", extract_first_name(name))
        elif choice == "5":
            print("Last name:", extract_last_name(name))
        elif choice == "6":
            print("Middle name(s):", extract_middle_names(name))
        elif choice == "7":
            print("Has hyphenated last name:", has_hyphenated_last_name(name))
        elif choice == "8":
            print("Lowercase:", to_lowercase(name))
        elif choice == "9":
            print("Uppercase:", to_uppercase(name))
        elif choice == "10":
            print("Shuffled name:", shuffle_name(name))
        elif choice == "11":
            print("Is first name a palindrome:", is_palindrome(extract_first_name(name)))
        elif choice == "12":
            print("Sorted characters:", sort_characters(name))
        elif choice == "13":
            print("Initials:", make_initials(name))
        elif choice == "14":
            print("Contains title:", contains_title(name))
        elif choice == "15":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
