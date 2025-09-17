# Welcome and Game Rules
Welcome = input("Welcome to Who wants to be a Millionaire? Quiz competition \nClick enter to continue\n")

# Game Rules
print("\n--- Game Rules ---")
print("1. You will be asked a series of 10 questions with increasing prize money.")
print("2. If you answer a question correctly, you win the prize for that question.")
print("3. After each correct answer, you can choose to 'walk away' with your current winnings.")
print("4. If you choose to continue and then get a question wrong, your winnings will be reset to the previous safe point.")
print("5. There are three safe points: after Question 1 ($100), after Question 4 ($500), and after Question 8 ($50,000).")
print("6. If you get Question 1 wrong, you win nothing.")
print("--------------------")
input("Click enter to continue...")

# Quiz data
questions = ("Question 1 ($100): How many elements are in the periodic table?: ",
             "Question 2 ($200): Which animal lays the largest eggs?: ",
             "Question 3 ($300): What is the most abundant gas in the earth's atmosphere?: ",
             "Question 4 ($500): How many bones are in the Human body?: ",
             "Question 5 ($1,000): Which planet in the solar system is the hottest?: ",
             "Question 6 ($5,000): What is the capital of France?: ",
             "Question 7 ($10,000): Which Shakespeare character famously declares, (Something is rotten in the state of Denmark)?: ",
             "Question 8 ($50,000): On which island is the majority of the population of the United Kingdom located?: ",
             "Question 9 ($100,000): Which of these was NOT an original member of the scientific inquiry group known as the X-Men?",
             "Question 10 ($1,000,000): What is the name of the largest natural harbor in the world?"
             )

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
           ("A. Berlin", "B. Rome", "C. Paris", "D. Madrid"),
           ("A. Hamlet", "B. Laertes", "C. Marcellus", "D. Horatio"),
           ("A. Ireland", "B. Great Britain", "C. New Zealand", "D. Iceland"),
           ("A. Cyclops", "B. Beast", "C. Iceman", "D. Wolverine"),
           ("A. Sydney Harbor", "B. The Bosphorus", "C. Manukau Harbor", "D. Port Jackson")
           )

answers = ("C", "D", "A", "A", "B", "C", "C", "B", "D", "B")

# New variables for the game
prizes = [100, 200, 300, 500, 1000, 5000, 10000, 50000, 100000, 1000000]
safe_points = {1: 100, 4: 500, 8: 50000}
money_won = 0

# Game loop
for question_num in range(len(questions)):
    print("\n---------------------")
    print(questions[question_num])
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D) or 'W' to walk away: ").upper()
    
    if guess == 'W':
        print(f"\nYou decided to walk away with ${money_won:,}!")
        break

    if guess == answers[question_num]:
        print("\nCORRECT!")
        money_won = prizes[question_num]
        print(f"You have won ${money_won:,}!")
        
        # Check for the top prize
        if question_num == len(questions) - 1:
            print("\nCongratulations! You have won a million dollars!")
            break
            
        # Ask to continue or walk away
        continue_playing = input("Would you like to continue to the next question? (yes/no): ").lower()
        if continue_playing in ('no', 'n'):
            print(f"\nYou decided to walk away with ${money_won:,}!")
            break
            
    else:
        print("\nINCORRECT")
        print(f"The correct answer was: {answers[question_num]}")
        
        # Check if the Player reached a safe point
        if question_num >= 8:
            money_won = safe_points[8]
        elif question_num >= 4:
            money_won = safe_points[4]
        elif question_num >= 1:
            money_won = safe_points[1]
        else:
            money_won = 0
            
        if money_won > 0:
            print(f"Your winnings are reduced to the safe point: ${money_won:,}")
        else:
            print("You have no winnings at this time.")
            
        print(f"Game over. Your final winnings are: ${money_won:,}")
        break

# Final message after the game loop
if question_num == len(questions) - 1 and guess == answers[question_num]:
    pass # Already handled inside the loop for the million dollar win
elif guess == 'W':
    pass # Already handled inside the loop for walking away
else:
    print("\nThank you for playing!")
