import re
import argparse
def check_password_strength(password):
    # Checks the strength of a password 
    # Check length
    length_criteria = len(password) >= 8
    # check if is upper case
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    # check if is lower case
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    # check if is number (int)
    digit_criteria = bool(re.search(r'\d', password))
    # check if is special character
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # to check if the five criteria is present in password
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # appreciation marks
    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    feedback = {
        "At least 8 characters long": length_criteria,
        "Contains an uppercase letter": uppercase_criteria,
        "Contains a lowercase letter": lowercase_criteria,
        "Contains a digit": digit_criteria,
        "Contains a special character": special_char_criteria
    }

    missing_criteria = [desc for desc, met in feedback.items() if not met]
    feedback_message = " and ".join(missing_criteria) if missing_criteria else "Meets all criteria"

    return strength_levels[score], feedback_message

def main():
   
    parser = argparse.ArgumentParser(description="Password check tools")
    parser.add_argument("--pswd", help="The password to check")
    args = parser.parse_args()
    print("Welcome to the Password Complexity Checker")
    strength, feedback = check_password_strength(args.pswd)
    print(f"Password Strength: {strength}")
    print(f"Feedback: {feedback}")

    print("Thank you for using the Password Complexity Checker. Goodbye!")

if __name__ == "__main__":
    main()