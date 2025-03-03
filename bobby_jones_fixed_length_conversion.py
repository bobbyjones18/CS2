'''
Author: Bobby Jones
Date: 2/27/25
Description: Reads in data from a txt file and puts it into a csv file
Bugs: None
Sources: https://www.geeksforgeeks.org/split-and-parse-a-string-in-python/
'''
import csv

def fixed_length_to_csv(input_file, output_file):
    """
    Reads a fixed-length formatted text file, extracts fields using slicing,
    and writes the formatted data to a CSV file.

    Args:
        input_file (str): Path to the input fixed-length text file.
        output_file (str): Path to the output CSV file.

    """
    # Define column widths and their starting positions
    columns = [
        (0, 6), #ID
        (6, 21), #First Name
        (21, 36), #Last Name
        (36, 42),    #Grade
        (42, 46),      #GPA
        (48, 58), #Bday
        (60, 66),    #Gender
        (67, 76),#Class Rank
        (76, 86), #Attendance Parcentage
        (86, 93),    #Honors
        (93, 102),   #Sports
        (102, 112) #Club Count
    ]

    # Read the fixed-length text file
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header

        # Process each line in the file
        for line in infile:
            row = [line[col[0]:col[1]].strip() for col in columns]
            writer.writerow(row)

# File paths
input_path = r"C:\Users\bjones25\Downloads\student_data_cs2.txt"
output_path = r"C:\Users\bjones25\Downloads\fixed_length_conversion_bobby_jones.csv"

# Run the function
fixed_length_to_csv(input_path, output_path)

print(f"CSV file successfully created: {output_path}")
