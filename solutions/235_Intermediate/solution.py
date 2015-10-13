def to_score(ball):
    return 10 if ball in ['X', '/'] else 0 if ball == '-' else int(ball)

def calculate_score(frames):
    balls = ''.join(frames)
    score = 0
    for i in range(len(balls)):
        if len(balls) - 3 <= i:
            if balls[i] == '/':
                score += 10 - to_score(balls[i-1])
            else:
                score += to_score(balls[i])
        elif balls[i] == '/':
            score += 10 - to_score(balls[i-1]) + to_score(balls[i+1])
        elif balls[i] == 'X':
            score += to_score(balls[i]) + to_score(balls[i+1])
            if balls[i+2] == '/':
                score += 10 - to_score(balls[i+1])
            else:
                score += to_score(balls[i+2])
        else:
            score += to_score(balls[i])
    return score

if __name__ == "__main__":
    with open("input/input1.txt", "r") as file:
        sheets = file.read().splitlines()
    for sheet in sheets:
        frames = sheet.split()
        print(calculate_score(frames))