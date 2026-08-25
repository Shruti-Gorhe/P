# Question 19 — Cricket Runs
# Problem Description

# A cricket team records the runs scored by different players. The program should store the total runs scored by each player and identify the player with the highest total runs.
# Function 1
# Function Name: record_runs

# Parameters:
# player_name, runs, scoreboard
# Requirements:
# Convert the player name to uppercase before storing it.
# If runs <= 0, do not add the runs to the dictionary.
# If the player already exists in the dictionary, add the new runs to the player's existing runs.
# If the player does not exist, create a new entry.
# Return the updated dictionary.

# Function 2
# Function Name: find_top_scorer
# Parameter:
# scoreboard
# Requirements:
# Return the player who has scored the highest total runs.
# If the dictionary is empty, return:
# ("", 0)

def record_runs(player_name,runs,scoreboard):
    player_name = player_name.upper()
    if runs<=0:
        return scoreboard
    if player_name in scoreboard:
        scoreboard[player_name]+=runs
    else:
        scoreboard[player_name]=runs
    return scoreboard

def find_top_scorer(scoreboard):
    if not scoreboard:
        return("",0)
    top_scorer = max(scoreboard,key=scoreboard.get)
    return top_scorer,scoreboard[top_scorer]

def main():

    scoreboard = {}

    n = int(input("Enter number of players: "))

    print("Enter player runs:")

    for i in range(n):

        name = input("Enter player name: ")

        runs = int(
            input(f"Enter {name}'s runs: ")
        )

        scoreboard = record_runs(
            name,
            runs,
            scoreboard
        )

    print("\nScoreboard:")

    for name, runs in scoreboard.items():
        print(f"{name}:{runs}")

    name, runs = find_top_scorer(scoreboard)

    print("\nTop Scorer")
    print(f"{name}:{runs}")


if __name__ == "__main__":
    main()