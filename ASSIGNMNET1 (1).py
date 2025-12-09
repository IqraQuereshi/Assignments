NAME-IQRA QURESHI
ENROLLMENT NO-0157EC231014
BATCH NO--6TH
TIMMING-12:10PM-1:50PM



BASIC IF ELSE PROBLEM

# Problem 1: Write a program to check whether a number is positive, negative, or zero.

def check_number_sign(num):
    """Checks if a number is positive, negative, or zero."""
    if num > 0:
        print(f"The number {num} is positive.")
    elif num < 0:
        print(f"The number {num} is negative.")
    else:
        print(f"The number {num} is zero.")

# Problem 2: Write a program to check whether a number is even or odd.

def check_even_odd(num):
    """Checks if a number is even or odd."""
    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")

# Problem 3: Write a program to check if a given year is a leap year or not.

def is_leap_year(year):
    """Checks if a given year is a leap year."""
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is NOT a leap year.")


# Problem 4: Write a program to find the greatest of two numbers.

def find_greatest(num1, num2):
    """Finds the greatest of two numbers."""
    if num1 > num2:
        print(f"The greatest number is {num1}.")
    elif num2 > num1:
        print(f"The greatest number is {num2}.")
    else:
        print("Both numbers are equal.")


# Problem 5: Write a program to check whether a person is eligible to vote (age >= 18).

def check_voting_eligibility(age):
    """Checks a person's eligibility to vote."""
    if age >= 18:
        print("The person is eligible to vote.")
    else:
        print("The person is NOT eligible to vote.")


# Problem 6: Write a program to check whether a given character is a vowel or consonant.

def check_vowel_consonant(char):
    """Checks if a character is a vowel or consonant."""
    # Convert to lowercase for case-insensitive check
    char_lower = char.lower()
    
    if char_lower in ('a', 'e', 'i', 'o', 'u'):
        print(f"The character '{char}' is a vowel.")
    elif 'a' <= char_lower <= 'z':
        # Check if it's a letter but not a vowel
        print(f"The character '{char}' is a consonant.")
    else:
        print(f"'{char}' is not a standard English alphabet character.")



# Problem 7: Write a program to check if a number is divisible by 5.

def is_divisible_by_five(num):
    """Checks if a number is divisible by 5."""
    if num % 5 == 0:
        print(f"The number {num} is divisible by 5.")
    else:
        print(f"The number {num} is NOT divisible by 5.")


# Problem 8: Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number.

def check_digit_count(num):
    """Checks if a number is single-digit (0-9), two-digit (10-99), or more."""
    num_abs = abs(num) # Works best with non-negative integers
    
    if 0 <= num_abs <= 9:
        print(f"The number {num} is a single-digit number.")
    elif 10 <= num_abs <= 99:
        print(f"The number {num} is a two-digit number.")
    else:
        print(f"The number {num} is a more than two-digit number (or negative/zero).")


# Problem 9: Write a program to check whether a student has passed or failed (passing marks = 40).

PASSING_MARKS = 40

def check_pass_fail(marks):
    """Checks if a student has passed or failed based on marks."""
    if marks >= PASSING_MARKS:
        print(f"The student PASSED with {marks} marks.")
    else:
        print(f"The student FAILED with {marks} marks.")


# Problem 10: Write a program to find whether the entered number is a multiple of both 3 and 7.

def check_multiple_of_3_and_7(num):
    """Checks if a number is a multiple of both 3 and 7."""
    # Check if remainder is 0 when divided by 3 AND remainder is 0 when divided by 7
    if num % 3 == 0 and num % 7 == 0:
        print(f"The number {num} is a multiple of both 3 and 7 (i.e., a multiple of 21).")
    else:
        print(f"The number {num} is NOT a multiple of both 3 and 7.")



LADDER IF AND NESTED IF

# Problem 1: Write a program to find the greatest among three numbers.

def find_greatest_three(num1, num2, num3):
    """Finds the greatest of three numbers."""
    if num1 >= num2 and num1 >= num3:
        greatest = num1
    elif num2 >= num1 and num2 >= num3:
        greatest = num2
    else:
        greatest = num3
    
    print(f"The greatest number among {num1}, {num2}, and {num3} is {greatest}.")


# Problem 2: Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).

def classify_age(age):
    """Classifies a person based on their age."""
    if age < 13:
        classification = "Child"
    elif age <= 19:  # Covers 13 to 19
        classification = "Teenager"
    elif age <= 59:  # Covers 20 to 59
        classification = "Adult"
    else:  # Covers 60 and above
        classification = "Senior"
    
    print(f"An age of {age} is classified as: {classification}.")



# Problem 3: Write a program to assign grades based on marks: 90-100: A, 75-89: B, 50-74: C, 35-49: D, <35: Fail.

def assign_grade(marks):
    """Assigns a grade based on marks."""
    if marks > 100 or marks < 0:
        grade = "Invalid Marks"
    elif marks >= 90:
        grade = "A"
    elif marks >= 75:  # Implies 75 to 89
        grade = "B"
    elif marks >= 50:  # Implies 50 to 74
        grade = "C"
    elif marks >= 35:  # Implies 35 to 49
        grade = "D"
    else:  # Implies < 35
        grade = "Fail"
        
    print(f"The marks {marks} correspond to grade: {grade}.")



# Problem 4: Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.

def check_triangle_type(s1, s2, s3):
    """Checks the type of triangle based on side lengths."""
    # Basic check for a valid triangle (sum of two sides > third side)
    if not (s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1):
        print("These side lengths do not form a valid triangle.")
        return
        
    if s1 == s2 and s2 == s3:
        triangle_type = "Equilateral"
    elif s1 == s2 or s1 == s3 or s2 == s3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
        
    print(f"The triangle with sides {s1}, {s2}, {s3} is a {triangle_type} triangle.")




# Problem 5: Write a program to check if a character is uppercase, lowercase, digit, or special symbol.

def check_char_type(char):
    """Checks the type of a single character."""
    if len(char) != 1:
        print("Please enter exactly one character.")
        return
        
    if char.isupper():
        print(f"'{char}' is an uppercase letter.")
    elif char.islower():
        print(f"'{char}' is a lowercase letter.")
    elif char.isdigit():
        print(f"'{char}' is a digit.")
    else:
        print(f"'{char}' is a special symbol.")


# Problem 6: Write a program to calculate electricity bill based on units:
# Up to 100 units: ₹5 per unit, 101–200 units: ₹7 per unit, Above 200 units: ₹10 per unit.

def calculate_bill(units):
    """Calculates the electricity bill based on consumption tiers."""
    total_bill = 0
    
    if units <= 100:
        total_bill = units * 5
    elif units <= 200:
        # First 100 units @ ₹5, remaining units @ ₹7
        base_charge = 100 * 5  # ₹500
        remaining_units = units - 100
        total_bill = base_charge + (remaining_units * 7)
    else:
        # First 100 units @ ₹5
        charge_100 = 100 * 5  # ₹500
        # Next 100 units (101-200) @ ₹7
        charge_200 = 100 * 7  # ₹700
        # Remaining units @ ₹10
        remaining_units = units - 200
        total_bill = charge_100 + charge_200 + (remaining_units * 10)
        
    print(f"For {units} units, the total bill is ₹{total_bill:.2f}.")



# Problem 7: Write a program to determine the largest of four numbers using nested if.

def largest_nested_if(n1, n2, n3, n4):
    """Determines the largest of four numbers using nested if."""
    
    if n1 >= n2:
        if n1 >= n3:
            if n1 >= n4:
                largest = n1
            else:
                largest = n4
        else: # n3 > n1
            if n3 >= n4:
                largest = n3
            else:
                largest = n4
    else: # n2 > n1
        if n2 >= n3:
            if n2 >= n4:
                largest = n2
            else:
                largest = n4
        else: # n3 > n2
            if n3 >= n4:
                largest = n3
            else:
                largest = n4
                
    print(f"The largest number is {largest}.")


# Problem 8: Write a program to check if a given year is a century year and also a leap year.

def check_century_leap(year):
    """Checks if a year is both a century year and a leap year."""
    is_century = year % 100 == 0
    is_leap = (year % 400 == 0) # Only century years divisible by 400 are leap years
    
    if is_century and is_leap:
        print(f"The year {year} is both a century year AND a leap year.")
    elif is_century:
        print(f"The year {year} is a century year but NOT a leap year.")
    else:
        print(f"The year {year} is not a century year.")



# Problem 9: Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).

def classify_bmi(weight_kg, height_m):
    """Calculates and classifies BMI."""
    if height_m <= 0:
        print("Height must be greater than zero.")
        return
        
    # BMI Formula: weight (kg) / [height (m)]^2
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0: # 18.5 to 24.9
        category = "Normal"
    elif bmi < 30.0: # 25.0 to 29.9
        category = "Overweight"
    else: # 30.0 and above
        category = "Obese"
        
    print(f"BMI: {bmi:.1f}")
    print(f"Classification: {category}")



# Problem 10: Write a program to display the smallest number among three using nested if.

def smallest_nested_if(n1, n2, n3):
    """Determines the smallest of three numbers using nested if."""
    
    if n1 <= n2:
        if n1 <= n3:
            smallest = n1
        else: # n3 < n1 <= n2
            smallest = n3
    else: # n2 < n1
        if n2 <= n3:
            smallest = n2
        else: # n3 < n2 < n1
            smallest = n3
            
    print(f"The smallest number among {n1}, {n2}, and {n3} is {smallest}.")



FOR LOOP PROBLEM

# Problem 1: Write a program using a for loop to print all Armstrong numbers between 100 and 999.

def find_armstrong_numbers():
    """Prints all 3-digit Armstrong numbers using a for loop."""
    print("3-digit Armstrong numbers:")
    
    for num in range(100, 1000):
        original_num = num
        sum_of_cubes = 0
        temp = num
        
        # Calculate sum of cubes of digits
        # Using a while loop here to process digits, as the number of digits is fixed (3)
        # We could also convert to string and use a for loop for digits, but math is cleaner for fixed range
        while temp > 0:
            digit = temp % 10
            sum_of_cubes += digit ** 3
            temp //= 10
            
        if original_num == sum_of_cubes:
            print(original_num)


# Problem 2: Write a program to generate and display the first n prime numbers using a for loop.

def is_prime(k):
    """Helper function to check if a number k is prime."""
    if k <= 1:
        return False
    # Check divisibility from 2 up to the square root of k
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True

def generate_n_primes(n):
    """Generates the first n prime numbers."""
    if n <= 0:
        print("N must be a positive integer.")
        return
    
    count = 0
    number = 2
    primes = []
    
    while count < n:
        if is_prime(number):
            primes.append(number)
            count += 1
        number += 1
        
    print(f"The first {n} prime numbers are: {primes}")



# Problem 3: Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.

def sum_digits(num):
    """Calculates the sum of the digits of a number."""
    s = 0
    # Use a loop to handle the sum of digits
    while num > 0:
        s += num % 10
        num //= 10
    return s

def filter_numbers():
    """Finds numbers from 1 to 500 satisfying the conditions."""
    result = []
    for num in range(1, 501):
        if num % 3 == 0:
            if sum_digits(num) <= 10:
                result.append(num)
                
    print(f"Numbers (1-500) divisible by 3 with sum of digits <= 10:\n{result}")



# Problem 4: Write a program using a for loop to print a pyramid of stars (*) of height n.

def print_star_pyramid(height):
    """Prints a pyramid of stars."""
    for i in range(height):
        # Calculate number of spaces: height - (i + 1)
        spaces = " " * (height - i - 1)
        # Calculate number of stars: 2 * (i + 1) - 1
        stars = "*" * (2 * i + 1)
        print(spaces + stars)



# Problem 5: Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once) using a for loop.

import string

def check_pangram(text):
    """Checks if a string is a pangram using a for loop."""
    text_lower = text.lower()
    
    # Initialize a set to store unique letters found
    found_letters = set()
    
    # Iterate through the alphabet using a for loop (standard method would iterate through the string)
    # The prompt specifically asks to use a for loop, implying its use in the checking process.
    
    for char in text_lower:
        if 'a' <= char <= 'z':
            found_letters.add(char)
            
    # Check if the number of unique letters found is 26
    if len(found_letters) == 26:
        print(f"'{text}' is a pangram.")
    else:
        print(f"'{text}' is NOT a pangram. Missing letters: {set(string.ascii_lowercase) - found_letters}")




# Problem 6: Write a program using a for loop to find all twin primes between 1 and 100.

def is_prime_loop(k):
    """Helper function to check if a number k is prime (reusing is_prime logic)."""
    if k <= 1:
        return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True

def find_twin_primes():
    """Finds all twin primes between 1 and 100."""
    twin_primes = []
    
    # Iterate through numbers from 2 up to 98 (since the second number must be <= 100)
    for p in range(2, 99):
        # Check if p is prime
        if is_prime_loop(p):
            # Check if p+2 is also prime
            q = p + 2
            if q <= 100 and is_prime_loop(q):
                twin_primes.append((p, q))
                
    print(f"Twin primes between 1 and 100:\n{twin_primes}")




# Problem 7: Write a program that accepts a number from the user and prints whether it is a Harshad number (number divisible by the sum of its digits) using a for loop.

def is_harshad(num):
    """Checks if a number is a Harshad number."""
    if num <= 0:
        print("Harshad numbers are positive integers.")
        return
        
    num_str = str(num)
    sum_of_digits = 0
    
    # Use a for loop to calculate the sum of digits
    for digit_char in num_str:
        sum_of_digits += int(digit_char)
        
    if sum_of_digits == 0: # Should not happen for positive num
        print(f"{num} is not a Harshad number.")
        return

    if num % sum_of_digits == 0:
        print(f"The number {num} is a Harshad number (divisible by {sum_of_digits}).")
    else:
        print(f"The number {num} is NOT a Harshad number.")



# Problem 8: Write a program to generate Pascal's Triangle up to n rows using a for loop.

def generate_pascals_triangle(n):
    """Generates Pascal's Triangle up to n rows."""
    if n <= 0:
        print("Number of rows must be positive.")
        return

    triangle = []
    
    # Outer loop for rows
    for i in range(n):
        row = [1] # Start every row with 1
        if i > 0:
            last_row = triangle[-1]
            # Inner loop to calculate middle elements
            for j in range(len(last_row) - 1):
                # The element is the sum of the two elements directly above it
                row.append(last_row[j] + last_row[j+1])
            row.append(1) # End every row with 1
        
        triangle.append(row)
        
        # Print the row with centering
        print(" " * (n - i - 1), end="")
        print(" ".join(map(str, row)))



# Problem 9: Write a program using a for loop to display the sum of the series: 1^2 + 2^2 + 3^2 + ... + n^2

def sum_of_squares_series(n):
    """Calculates the sum of squares from 1^2 to n^2 using a for loop."""
    if n <= 0:
        print("N must be a positive integer.")
        return
        
    total_sum = 0
    series_str = ""
    
    for i in range(1, n + 1):
        square = i ** 2
        total_sum += square
        series_str += f"{square}"
        if i < n:
            series_str += " + "
            
    print(f"Series: {series_str}")
    print(f"The sum of the series up to {n}^2 is: {total_sum}")





# Problem 10: Write a program that accepts a number from the user and prints whether it is a Strong number (sum of factorials of digits = number itself) using a for loop.

# Pre-calculate factorials for digits 0-9
# This uses a dictionary to store factorials for quick lookup
FACTORIALS = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}

def is_strong_number(num):
    """Checks if a number is a Strong number."""
    if num <= 0:
        print("Strong numbers are positive integers.")
        return
        
    num_str = str(num)
    sum_of_factorials = 0
    
    # Use a for loop to iterate through the digits (as characters)
    for digit_char in num_str:
        digit = int(digit_char)
        # Look up the pre-calculated factorial
        sum_of_factorials += FACTORIALS[digit]
        
    if num == sum_of_factorials:
        print(f"The number {num} is a Strong number.")
    else:
        print(f"The number {num} is NOT a Strong number (Sum of factorials: {sum_of_factorials}).")




WHILE LOOP PROBLEM



# Problem 11: Write a program using a while loop to find the reverse of a number and check if the reversed number is prime.

def is_prime_while(k):
    """Helper function to check if a number k is prime (using for loop)."""
    if k <= 1: return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0: return False
    return True

def reverse_and_check_prime(num):
    """Reverses a number and checks if the reversal is prime."""
    original_num = num
    reversed_num = 0
    temp = abs(num) # Handle negative input gracefully
    
    # While loop to reverse the number
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10
        
    print(f"Input: {original_num} -> Reverse: {reversed_num}")
    
    if is_prime_while(reversed_num):
        print(f"The reversed number {reversed_num} is Prime.")
    else:
        print(f"The reversed number {reversed_num} is NOT Prime.")




# Problem 12: Write a program that continues to accept numbers until the sum of digits of all numbers entered becomes greater than 100.

def sum_digits_loop(num):
    """Calculates the sum of the digits of a number."""
    s = 0
    temp = abs(num)
    while temp > 0:
        s += temp % 10
        temp //= 10
    return s

def aggregate_sum_check():
    """Accepts numbers until the total sum of their digits exceeds 100."""
    total_digit_sum = 0
    
    # While loop for continuous input
    while total_digit_sum <= 100:
        try:
            user_input = int(input("Enter a number: "))
            current_digit_sum = sum_digits_loop(user_input)
            total_digit_sum += current_digit_sum
            print(f"Current total sum of all digits entered: {total_digit_sum}")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"\nCondition met! The total sum of digits ({total_digit_sum}) is greater than 100.")




# Problem 13: Write a program using a while loop to check whether a number is a Duck number.

def is_duck_number(num_str):
    """Checks if a number (represented as a string) is a Duck number."""
    if not num_str.isdigit() or not num_str:
        print(f"'{num_str}' is not a valid positive integer string.")
        return
        
    # Check if the number starts with zero (not allowed)
    if num_str.startswith('0'):
        print(f"'{num_str}' is NOT a Duck number (starts with zero).")
        return
        
    has_zero = False
    i = 0
    
    # While loop to search for '0' in the rest of the string
    while i < len(num_str):
        if num_str[i] == '0':
            has_zero = True
            break # Exit loop once zero is found
        i += 1
        
    if has_zero:
        print(f"The number {num_str} is a Duck number.")
    else:
        print(f"The number {num_str} is NOT a Duck number (contains no zero).")



# Problem 14: Write a program using a while loop to accept a number and check if it is a Happy number.

def get_sum_of_squares_of_digits(num):
    """Helper function to calculate the sum of the squares of the digits."""
    s = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        s += digit ** 2
        temp //= 10
    return s

def is_happy_number(num):
    """Checks if a number is a Happy number."""
    seen = set()
    current_num = num
    
    # While loop runs until the number is 1 (Happy) or a cycle is detected (Unhappy)
    while current_num != 1 and current_num not in seen:
        seen.add(current_num)
        current_num = get_sum_of_squares_of_digits(current_num)
        
    if current_num == 1:
        print(f"The number {num} is a Happy number.")
    else:
        print(f"The number {num} is NOT a Happy number (stuck in a cycle).")




# Problem 15: Write a program using a while loop to find the largest prime factor of a given number.

def largest_prime_factor(n):
    """Finds the largest prime factor of a given number n."""
    if n <= 1:
        print("Input must be greater than 1.")
        return
        
    number = n
    largest_factor = 1
    i = 2
    
    # First, handle factor 2
    while number % 2 == 0:
        largest_factor = 2
        number //= 2
        
    # While loop checks for odd factors starting from 3
    i = 3
    while i * i <= number:
        if number % i == 0:
            largest_factor = i
            number //= i
        else:
            i += 2 # Only check odd numbers
            
    # If the remaining number is greater than 2, it is the largest prime factor
    if number > 2:
        largest_factor = number
        
    print(f"The largest prime factor of {n} is {largest_factor}.")






# Problem 16: Write a program to repeatedly accept a string from the user until the string entered is a palindrome.

def is_palindrome(text):
    """Checks if a string is a palindrome (case-insensitive, ignores spaces)."""
    clean_text = "".join(c.lower() for c in text if c.isalnum())
    return clean_text == clean_text[::-1]

def accept_until_palindrome():
    """Repeatedly accepts input until a palindrome is entered."""
    while True:
        user_input = input("Enter a string (Enter a palindrome to stop): ")
        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome. Program finished.")
            break
        else:
            print(f"'{user_input}' is NOT a palindrome. Try again.")



# Problem 17: Write a program using a while loop to compute the sum of digits of a number until the result becomes a single-digit number (Digital root).

def digital_root(num):
    """Computes the digital root of a number."""
    if num == 0:
        print("The digital root of 0 is 0.")
        return
        
    current_sum = num
    
    # Outer while loop runs until the sum is a single digit
    while current_sum >= 10:
        
        # Inner while loop to compute the sum of digits
        temp_sum = 0
        temp_num = current_sum
        while temp_num > 0:
            temp_sum += temp_num % 10
            temp_num //= 10
            
        print(f"  Sum of digits of {current_sum} = {temp_sum}")
        current_sum = temp_sum
        
    print(f"The digital root is: {current_sum}")





# Problem 18: Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even => n/2, if odd => 3n+1. Continue until n=1).

def generate_collatz_sequence(n):
    """Generates the Collatz sequence for a given number."""
    if n <= 0 or not isinstance(n, int):
        print("Input must be a positive integer.")
        return
        
    current_n = n
    sequence = [current_n]
    
    # While loop continues until the number reaches 1
    while current_n != 1:
        if current_n % 2 == 0:
            current_n //= 2
        else:
            current_n = 3 * current_n + 1
            
        sequence.append(current_n)
        
    print(f"Collatz sequence for {n}:\n{sequence}")




# Problem 19: Write a program using a while loop to accept a number and check whether it is a Kaprekar number.

def is_kaprekar(n):
    """Checks if a number is a Kaprekar number."""
    if n <= 0:
        print("Kaprekar numbers are positive integers.")
        return
        
    square = n * n
    square_str = str(square)
    n_digits = len(str(n))
    is_kap = False
    
    # We need to split the square_str. The split point i can range from 1 to len(square_str) - 1.
    i = 1
    
    # While loop iterates through all possible split points
    while i < len(square_str):
        part1_str = square_str[:i]
        part2_str = square_str[i:]
        
        # Convert to integer. part1 can be empty, in which case it is 0.
        part1 = int(part1_str) if part1_str else 0
        part2 = int(part2_str)
        
        if part1 + part2 == n:
            is_kap = True
            print(f"The number {n} is a Kaprekar number. ({square} splits into {part1} + {part2} = {n})")
            break
        
        i += 1
        
    if not is_kap:
        print(f"The number {n} is NOT a Kaprekar number.")



# Problem 20: Write a program to simulate an ATM machine using a while loop.

def atm_simulation():
    """Simulates a basic ATM machine."""
    balance = 10000.00
    
    # Main while loop to keep the ATM running
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print(f"Current Balance: ₹{balance:.2f}")
            
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount > 0:
                    balance += amount
                    print(f"Deposit successful. New Balance: ₹{balance:.2f}")
                else:
                    print("Deposit amount must be positive.")
            except ValueError:
                print("Invalid amount.")
                
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount > 0:
                    # Check for sufficient balance
                    if amount <= balance:
                        balance -= amount
                        print(f"Withdrawal successful. New Balance: ₹{balance:.2f}")
                    else:
                        print("Withdrawal failed: Insufficient balance.")
                else:
                    print("Withdrawal amount must be positive.")
            except ValueError:
                print("Invalid amount.")
                
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break  # Exit the while loop
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")













