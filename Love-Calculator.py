name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lcname1 = name1.lower()
t = lcname1.count("t")
r = lcname1.count("r")
u = lcname1.count("u")
e = lcname1.count("e")
lcname2 = name2.lower()
t2 = lcname2.count("t")
r2 = lcname2.count("r")
u2 = lcname2.count("u")
e2 = lcname2.count("e")
true = t+r+u+e+t2+r2+u2+e2
sot = str(true)

lcname1 = name1.lower()
l = lcname1.count("l")
o = lcname1.count("o")
v = lcname1.count("v")
e = lcname1.count("e")
lcname2 = name2.lower()
l2 = lcname2.count("l")
o2 = lcname2.count("o")
v2 = lcname2.count("v")
e2 = lcname2.count("e")
love = l+o+v+e+l2+o2+v2+e2
sol = str(love)
store = sot+sol
score = int(store)

if score < 10 or score > 90 :
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50 :
    print(f"Your score is {score}, you are alright together.")
else :
    print(f"Your score is {score}.")