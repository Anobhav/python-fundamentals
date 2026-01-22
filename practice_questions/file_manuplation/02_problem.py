highscore_new = 10

with open("practice_questions\\file_manuplation\\02_problem.txt", "r") as f:
    data = f.read().strip()
    highscore_old = int(data.split("=")[1])

with open("practice_questions\\file_manuplation\\02_problem.txt", "w") as f:
    if highscore_new > highscore_old:
        f.write(f"highscore={highscore_new}")
        print(f"New highscore is: {highscore_new}")
    else:
        f.write(f"highscore={highscore_old}")
        print(f"You did not beat the current highscore: {highscore_old}")


