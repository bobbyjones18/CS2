How It Works:
1. determine_mail_class(): This function checks the mail dimensions to classify it into one of the categories like `REGULAR POST CARD`, `PACKAGE`, etc.
   
2. calculate_zones(): It determines how many postal zones the mail will travel through, based on the starting and ending zip codes.

3. calculate_postage(): This function uses the mail class and the number of zones to calculate the cost of postage, rounded to two decimal places.

4. main(): The main program loop, which asks the user to input dimensions and zip codes for five pieces of mail, calculates the postage, and prints the result.
 
Example Usage:
Input:
Enter length, height, thickness, start zip, end zip (space-separated): 4.0 5.0 0.008 10000 85000
Enter length, height, thickness, start zip, end zip (space-separated): 5.5 10.0 0.25 30000 64000
Output:
The cost of mailing is: 0.43
The cost of mailing is: 1.20
