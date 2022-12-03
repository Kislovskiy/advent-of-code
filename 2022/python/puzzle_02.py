from utils import read_input_file

scores = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

win_scores = {
    "win": 6,
    "draw": 3,
    "lost": 0,
}

score = 0

for line in read_input_file("data/puzzle_02.txt"):
    player1, player2 = line.split()
    if player1 == "C":  # Scissors
        if player2 == "X":  # Rock
            score += scores.get("X") + win_scores.get("win")  # win
        if player2 == "Y":  # Paper
            score += scores.get("Y") + win_scores.get("lost")  # lost
        if player2 == "Z":  # Scissors
            score += scores.get("Z") + win_scores.get("draw")  # draw
    if player1 == "B":  # Paper
        if player2 == "X":  # Rock
            score += scores.get("X") + win_scores.get("lost")  # lost
        if player2 == "Y":  # Paper
            score += scores.get("Y") + win_scores.get("draw")  # draw
        if player2 == "Z":  # Scissors
            score += scores.get("Z") + win_scores.get("win")  # win
    if player1 == "A":  # Rock
        if player2 == "X":  # Rock
            score += scores.get("X") + win_scores.get("draw")  # draw
        if player2 == "Y":  # Paper
            score += scores.get("Y") + win_scores.get("win")  # win
        if player2 == "Z":
            score += scores.get("Z") + win_scores.get("lost")  # lost

print(f"part1 score: {score}")


scores_normal = {
    "Rock": 1,  # Rock
    "Paper": 2,  # Paper
    "Scissors": 3,  # Scissors
}

score = 0

for line in read_input_file("data/puzzle_02.txt"):
    player1, player2 = line.split()
    if player1 == "C":  # Scissors
        if player2 == "X":  # lose
            score += scores_normal.get("Paper") + win_scores.get("lost")
        if player2 == "Y":  # draw
            score += scores_normal.get("Scissors") + win_scores.get("draw")
        if player2 == "Z":  # win
            score += scores_normal.get("Rock") + win_scores.get("win")
    if player1 == "B":  # Paper
        if player2 == "X":  # lose
            score += scores_normal.get("Rock") + win_scores.get("lost")
        if player2 == "Y":  # drew
            score += scores_normal.get("Paper") + win_scores.get("draw")
        if player2 == "Z":  # win
            score += scores_normal.get("Scissors") + win_scores.get("win")
    if player1 == "A":  # Rock
        if player2 == "X":  # lose
            score += scores_normal.get("Scissors") + win_scores.get("lost")
        if player2 == "Y":  # draw
            score += scores_normal.get("Rock") + win_scores.get("draw")
        if player2 == "Z":  # win
            score += scores_normal.get("Paper") + win_scores.get("win")

print(f"part2 score = {score}")
