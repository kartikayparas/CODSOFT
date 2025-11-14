import random

choices = ["rock", "paper", "scissors"]

def decide(a, b):
    if a == b: return "tie"
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    return "win" if wins[a] == b else "lose"

def main():
    print("Rock Paper Scissors - type 'exit' to quit")
    score = {"you":0, "comp":0, "ties":0}
    while True:
        you = input("Your move (rock/paper/scissors): ").strip().lower()
        if you == "exit": break
        if you not in choices:
            print("Invalid. Try again.")
            continue
        comp = random.choice(choices)
        result = decide(you, comp)
        if result == "win":
            score["you"] += 1
            print(f"You {result}! {you} beats {comp}.")
        elif result == "lose":
            score["comp"] += 1
            print(f"You {result}. {comp} beats {you}.")
        else:
            score["ties"] += 1
            print("Tie.")
        print("Score -> You:", score["you"], "Comp:", score["comp"], "Ties:", score["ties"])
    print("Final score:", score)

if __name__ == "__main__":
    main()
