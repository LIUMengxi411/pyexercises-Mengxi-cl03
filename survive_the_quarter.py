
# Final Project: Survive the Quarter - Version B
# Name: Mengxi LIU
# Group: B

# Q1: What goes in?
# My program reads scenarios_B.csv.
# The file uses semicolons (;) to separate 14 columns.
# Each row contains a scenario ID, a situation, and three choices.
# Each choice has text, budget change, reputation change,
# and feedback.
# The numbers are stored as text, so I need to convert
# them into integers before doing calculations.

# Q2: What happens?
# 1. Show the day number, budget, and reputation.
# 2. Show a random situation with three choices: A, B, and C.
# 3. Ask the player to choose one option.
# 4. If the input is invalid, ask again.
# 5. Update the budget and reputation based on the choice.
# 6. Show the feedback and save the choice in history.
# 7. Stop the game if budget or reputation reaches zero.
# 8. Continue until day 10 if the player survives.

# Q3: What comes out?
# At the end, the game shows the final budget and reputation.
# It tells the player if they are fired or survived.
# If they survive, it shows their final score and title.
# It also shows the best and worst moves.
# The results.csv file saves the player's name, budget,
# reputation, title, and date.

# Q4: What could go wrong?
# 1. The player enters an invalid choice.
#    The program asks again until they enter A, B, or C.
# 2. The budget or reputation becomes zero or negative.
#    The game stops immediately and the player is fired.
# 3. The CSV file is missing.
#    The program shows an error message.
# 4. The reputation becomes higher than 100.
#    The program limits it to 100.

# My chosen feature: Difficulty
# I chose this feature because I want players to choose
# how difficult the game will be.
# Easy mode starts with a budget of 15000 EUR.
# Hard mode starts with a budget of 6000 EUR.
# Both modes start with 50 reputation.


# Import the modules needed for the game.
import csv
import random
from datetime import date

# This function reads the scenarios from my CSV file.
def load_scenarios():
    scenarios = []

    try:
        with open("scenarios_B.csv", "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file, delimiter=";")
            print(reader.fieldnames)
            for row in reader:
                scenario = {
                    "id": row["Num"],
                    "situation": row["Situation"],
                    "A": (
                        row["A_Choice"],
                        int(row["A_Money"]),
                        int(row["A_Buzz"]),
                        row["A_Reaction"]
                    ),
                    "B": (
                        row["B_Choice"],
                        int(row["B_Money"]),
                        int(row["B_Buzz"]),
                        row["B_Reaction"]
                    ),
                    "C": (
                        row["C_Choice"],
                        int(row["C_Money"]),
                        int(row["C_Buzz"]),
                        row["C_Reaction"]
                    )
                }

                scenarios.append(scenario)

    except FileNotFoundError:
        print("Error: scenarios_B.csv was not found.")
        return []

    return scenarios


# Test if the scenarios can be loaded correctly.



# This function asks the player to choose a difficulty.
def choose_difficulty():
    while True:
        difficulty = input("Choose difficulty (easy/hard): ").strip().lower()

        if difficulty == "easy":
            return 15000
        elif difficulty == "hard":
            return 6000
        else:
            print("Please enter easy or hard.")


# This function starts the game and prepares the first day.
def start_game():
    print("Welcome to Survive the Quarter!")

    name = input("What is your name? ").strip()
    if not name:
        name = "Player"

    budget = choose_difficulty()
    reputation = 50

    scenarios = load_scenarios()
    if not scenarios:
        print("The game cannot start without scenarios.")
        return

    random.shuffle(scenarios)

    print("Hello,", name)
    print("Starting budget:", budget, "EUR")
    print("Starting reputation:", reputation, "/100")

  
    # Keep a record of each day's decision.
    history = []

    # Play up to ten days with different scenarios.
    for day, scenario in enumerate(scenarios[:10], start=1):
        print("\n--- Day", day, "---")
        print("Budget:", budget, "EUR")
        print("Reputation:", reputation, "/100")
        print(scenario["situation"])

        for letter in ("A", "B", "C"):
            print(letter + ":", scenario[letter][0])

        choice = get_choice()
        option = scenario[choice]

        budget, reputation = apply_choice(budget, reputation, option)

        # Save the day, choice text and reputation change.
        history.append((option[2], day, option[0]))

        # Stop immediately if either gauge reaches zero.
        if budget <= 0 or reputation <= 0:
            print("\nGame over! You are fired.")
            if budget <= 0:
                print("Reason: No budget left.")
            if reputation <= 0:
                print("Reason: Reputation reached zero.")
            break

        # Check whether the player survived all ten days.
    survived = budget > 0 and reputation > 0 and len(history) == 10

    # Show the summary and save the result.
    show_summary(name, budget, reputation, history, survived)



# This function asks for a valid choice.
def get_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()
        if choice in ("A", "B", "C"):
            return choice
        print("Please type A, B or C.")


# This function updates the two gauges after a choice.
def apply_choice(budget, reputation, option):
    text, money_change, rep_change, feedback = option

    budget = budget + money_change
    reputation = min(100, reputation + rep_change)

    print(feedback)
    print("Budget change:", money_change, "EUR")
    print("Reputation change:", rep_change)

    return budget, reputation


# This function saves the result of each game.
def save_result(name, budget, reputation, title):
    filename = "results.csv"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Name", "Budget", "Reputation", "Title", "Date"
            ])

        writer.writerow([
            name, budget, reputation, title, date.today()
        ])

    print("Game result saved to results.csv")


# This function shows the final result of the game.
def show_summary(name, budget, reputation, history, survived):
    print("\n===== GAME SUMMARY =====")

    if survived:
        print("Congratulations! You survived 10 days!")
    else:
        print("You are fired!")

    # Calculate the final score.
    # Calculate the score using the teacher's formula.
    score = reputation + budget // 200

    
# Give the player a title based on the final score.
    if not survived:
        title = "Fired"
    elif score < 95:
        title = "Eternal Intern"
    elif score < 120:
        title = "Growth Hacker"
    elif score < 140:
        title = "CMO Material"
    else:
        title = "Viral Legend"


    print("Player:", name)
    print("Final budget:", budget, "EUR")
    print("Final reputation:", reputation, "/100")
    print("Final score:", score)
    print("Title:", title)

    # Find the best and worst reputation changes.
    if history:
        best = max(history, key=lambda item: item[0])
        worst = min(history, key=lambda item: item[0])

        print("\nBest decision: Day", best[1], "-", best[2])
        print("Reputation change:", best[0])

        print("Worst decision: Day", worst[1], "-", worst[2])
        print("Reputation change:", worst[0])

    save_result(name, budget, reputation, title)

# Run the game.
start_game()
