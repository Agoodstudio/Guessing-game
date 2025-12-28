def check(score):
    if score < 50:
        print("fail")
    else:
        print("pass")

score = (int) (input("please enter a score:"))
while score >= 0:
    check(score)
    score = (int) (input("please enter the score:"))
