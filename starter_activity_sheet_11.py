# program written by Sue Sentance


def check_answer(answer):
    # Declare a variable to hold the answer
    num = 1
    
    while True:
        try:
            # Get input from the user
            ans = input("Please enter a number between 1 and 10: ")
            
            # cast the input to an integer
            num = int(ans)
            
            # Check if the number is within the valid range
            if 1 <= num <= 10:
                break
            else:
                print("Number out of range. Try again.")
        except ValueError:
            print("That's not a valid number. Please try again.")
            continue
        
    print(f"You entered a valid number: {num}")
        
