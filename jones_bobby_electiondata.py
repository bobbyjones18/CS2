"""
Author: Bobby Jones
Date: 10/29/24
Description: This program processes text files containing speeches, calculates the frequency of words, and saves the results as CSV files. 
Version Log: 1.1
Bugs: None
Features: None
Sources:https://www.py4e.com/html3/09-dictionaries, https://www.w3schools.com/python/python_ref_dictionary.asp
"""

from collections import defaultdict
import string
import csv

# Define file paths for the speech text files
harris_file = r"C:\Users\bjones25\Downloads\kamala_new.txt"
trump_file = r"C:\Users\bjones25\Downloads\cleaned_trump_speech_transcript.txt"

# List of common words (stop words) to exclude
stop_words = set(["a", "i", "the", "is", "and", "or", "in", "of", "him", "most", "get", "here", "put", "many", "lets",
                  "there", "those", "do", "how", "like", "been", "more", "every", "these", "make", "way", "any", "just", 
                  "into", "im", "new", "other", "same", "being", "take", "must", "very", "much", "back", "if", "want", 
                  "made","also", "which", "going", "know", "about", "because", "always", "what", "would", "out", "up", 
                  "let", "her", "where", "now", "were", "had", "your", "to", "it", "for", "on", "that", "this", "no", 
                  "with", "as", "by", "our", "we", "he", "are", "us", "an", "but", "was", "has", "have", "when", "you", 
                  "not", "she", "be", "will", "who", "my", "one", "their", "me", "all", "they", "his", "at", "so", 
                  "them", "am", "its", "can", "than", "from"])

def process_text(file_path):
    """
    Processes a text file to calculate the frequency of each word, excluding common stop words.

    Args:
        file_path (str): The file path to the text file containing the speech.

    Returns:
        dict: A dictionary where the keys are words and values are the frequency of each word.

    Example:
        word_freq = process_text('kamala_harris_speech.txt')
    
    """
    word_freq = defaultdict(int)
    with open(file_path, 'r') as f:
        for line in f:
            # Remove punctuation, convert to lowercase, and split into words
            words = line.translate(str.maketrans('', '', string.punctuation)).lower().split()
            for word in words:
                if word not in stop_words:
                    word_freq[word] += 1
    return word_freq

def save_to_csv(word_freq, filename):
    """
    Saves word frequency data to a CSV file, sorted by frequency in descending order.

    Args:
        word_freq (dict): A dictionary where the keys are words and values are the frequency of each word.
        filename (str): The name of the CSV file to save the word frequency data.

    Returns:
        None
    
    Example:
        save_to_csv(harris_word_freq, 'harris_word_freq.csv')
    
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Word", "Frequency"])  # CSV header
        for word, freq in sorted(word_freq.items(), key=lambda item: item[1], reverse=True):
            writer.writerow([word, freq])

# Process each file to get word frequencies
harris_word_freq = process_text(harris_file)
trump_word_freq = process_text(trump_file)

# Save word frequencies to CSV files
save_to_csv(harris_word_freq, 'harris_word_freq.csv')
save_to_csv(trump_word_freq, 'trump_word_freq.csv')
