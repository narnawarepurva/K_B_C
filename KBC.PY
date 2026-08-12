# Quiz game (KBC)
questions =  [
    ["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Who is known as the Father of Computers?", "Charles Babbage", "Newton", "Einstein", "Tesla", 1],
    ["How many continents are there?", "5", "6", "7", "8", 7],
    ["Which language is used for Python programming?", "English", "C", "Java", "Python", 4]]


prize_money = [100, 2000, 5000, 10000, 20000]
total_amount = 0

for  i in range(len(questions)):
    q = questions[i]

    print(f"\nQuestions {i + 1} for ₹{prize_money[i]}")
    print(q[0])

    print("1", q[1])
    print("2", q[2])
    print("3", q[3])
    print("4", q[4])

    answer = int(input("Enter your answer (1-4):"))

    if answer == q[5]:
        total_amount = prize_money[i]
        print("Correct answer")
        print("you have won  ₹", total_amount)
    else:
        print("wrong answer")
        break

    print("Game over! You won ₹", total_amount)


