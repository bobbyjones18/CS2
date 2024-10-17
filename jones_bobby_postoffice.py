'''
Author: Bobby Jones
Date: 9/30/24
Description: This program asks the user for dimensions of an object being shipped and the starting and ending location and gives the user a cost for how expensive it will be to ship an object of that size that distance.
Log: 1.0
Bugs: Some bugs include edge case issues with the classification of packages at boundary values and the handling of "Unmailable" items
Features: None
Sources: https://www.geeksforgeeks.org/enumerate-in-python/
'''

def determine_mail_class(length, height, thickness):
    """
    Determines the class of mail based on its dimensions.

    Args:
        length (float): The length of the mail.
        height (float): The height of the mail.
        thickness (float): The thickness of the mail.

    Returns:
        str: The class of the mail ('REGULAR POST CARD', 'LARGE POST CARD', 
        'ENVELOPE', 'LARGE ENVELOPE', 'PACKAGE', 'LARGE PACKAGE', 'UNMAILABLE').
    """

    perimeter = 2 * height + 2 * thickness
    length_plus_perimeter = length + perimeter

    # Regular Post Card
    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and 0.007 <= thickness <= 0.016:
        return "REGULAR POST CARD"
    
    # Large Post Card
    elif 4.25 < length <= 6 and 6 < height <= 11.5 and 0.007 <= thickness <= 0.015:
        return "LARGE POST CARD"
    
    # Envelope
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and 0.016 <= thickness <= 0.25:
        return "ENVELOPE"
    
    # Large Envelope
    elif 6.125 < length <= 24 and 11 <= height <= 18 and 0.25 <= thickness <= 0.5:
        return "LARGE ENVELOPE"
    
    # Package
    elif length_plus_perimeter <= 84:
        return "PACKAGE"

    # Large Package
    elif 84 < length_plus_perimeter <= 130:
        return "LARGE PACKAGE"

    # Unmailable
    else:
        return "UNMAILABLE"

def calculate_zones(start_zip, end_zip):
    """
    Calculates the number of zones a package will travel through based on the zip codes.

    Args:
        start_zip (str): Starting zip code.
        end_zip (str): Ending zip code.

    Returns:
        int: The number of zones the mail must travel through.
    """
    zip_zones = [
        (1, 6999), (7000, 19999), (20000, 35999), 
        (36000, 62999), (63000, 84999), (85000, 99999)
    ]
    
    start_zone = next(i+1 for i, (low, high) in enumerate(zip_zones) if low <= int(start_zip) <= high)
    end_zone = next(i+1 for i, (low, high) in enumerate(zip_zones) if low <= int(end_zip) <= high)
    
    return abs(end_zone - start_zone)

def calculate_postage(mail_class, zones):
    """
    Calculates the postage cost based on the mail class and the number of zones.

    Args:
        mail_class (str): The class of the mail.
        zones (int): The number of postal zones the mail will travel through.

    Returns:
        float: The cost of mailing the piece, rounded to two decimal places.
    """
    if mail_class == "REGULAR POST CARD":
        return round(0.20 + 0.03 * zones, 2)
    elif mail_class == "LARGE POST CARD":
        return round(0.37 + 0.03 * zones, 2)
    elif mail_class == "ENVELOPE":
        return round(0.37 + 0.04 * zones, 2)
    elif mail_class == "LARGE ENVELOPE":
        return round(0.60 + 0.05 * zones, 2)
    elif mail_class == "PACKAGE":
        return round(2.95 + 0.25 * zones, 2)
    elif mail_class == "LARGE PACKAGE":
        return round(3.95 + 0.35 * zones, 2)
    else:
        return "UNMAILABLE"

def format_postage_cost(cost):
    """
    Formats the postage cost to remove the leading zero if it is a decimal value.

    Args:
        cost (float or str): The cost of mailing the piece, or "UNMAILABLE" if it is unmailable.

    Returns:
        str: The formatted cost as a string, with leading zero removed if applicable.
    """
    if isinstance(cost, float):
        formatted_cost = f"{cost:.2f}".lstrip('0')
        return formatted_cost
    return cost

def main():
    """
    Main function that takes user input, processes it, and outputs the postage cost.

    Input:
        Each input line contains: length (float), height (float), thickness (float),
        starting zip code (str), ending zip code (str).

    Output:
        Prints the cost of mailing each piece of mail. If the mail is unmailable, prints "UNMAILABLE".
    """
    # Input
    for _ in range(5):
        input_data = input("Enter length, height, thickness, start zip, end zip (comma-separated): ").split(',')
        length = float(input_data[0])
        height = float(input_data[1])
        thickness = float(input_data[2])
        start_zip = input_data[3]
        end_zip = input_data[4]
        
        # Determine mail class
        mail_class = determine_mail_class(length, height, thickness)
        
        # If mail is unmailable, print and continue to next item
        if mail_class == "UNMAILABLE":
            print("UNMAILABLE")
            continue
        
        # Calculate zones
        zones = calculate_zones(start_zip, end_zip)
        
        # Calculate postage
        postage_cost = calculate_postage(mail_class, zones)
        
        # Format the postage cost
        formatted_cost = format_postage_cost(postage_cost)
        
        # Output result
        print(formatted_cost)

if __name__ == "__main__":
    main()

