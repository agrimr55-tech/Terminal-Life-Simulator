import random

name = input("Enter Your Character's name? ")
print("Welcome to my 'Mini Life Simulator',", name)
print("I hope you have a nice day 😉")
input("Press Enter to start the game.")

# Stats
e = 100
h = 100
he = 100
mo = 10
d = 1
ma = 10
iq = 100
immortal = False


def cap():
    global he, e, h, iq
    he = max(0, min(he, 100))
    e = max(0, min(e, 100))
    h = max(0, min(h, 100))
    iq = max(0, min(iq, 200))


def stats():
    age = (d - 1) // 2 + 1
    print("\nDay", d)
    print("Money:", mo)
    print("Health:", he)
    print("Energy:", e)
    print("Happiness:", h)
    print("IQ:", iq)
    print("Age:", age)


while d <= ma:

    stats()
    age = (d - 1) // 2 + 1

    ev = random.randint(1, 5)
    ev2 = random.randint(1, 10)

    # ---------- Milestone Events ----------

    if d == 25:
        print("⭐ Special Event!")
        a = input("Risk ALL your money for Double or Nothing? (yes/no) ")

        if a.lower() == "yes":
            if ev2 == 1:
                print("You doubled your money!!")
                mo *= 2
            else:
                print("You lost everything.")
                mo = 0
            cap()

    if d == 50:
        print("🎉 Good Work Till Here!")
        b = input("Apply For A High Paying Job? (yes/no) ")

        if b.lower() == "yes" and iq >= 70:
            print("You got the job!")
            mo += 25
            h += 17
            cap()
        elif b.lower() == "yes":
            print("You were rejected. Not smart enough.")

    if d == 100:
        print("🎲 Lottery Event!")
        c = input("Buy a lottery ticket for $20? (yes/no) ")

        if c.lower() == "yes" and mo >= 20:
            mo -= 20
            if random.randint(1, 20) == 1:
                print("💰 You won $1000!")
                mo += 1000
            else:
                print("Better luck next time.")
            cap()

    # ---------- Ultra Legendary Events ----------

    if d > 10:
        f = random.randint(1, 200)

        if f == 1:
            print("☄️ LEGENDARY EVENT!")
            print("A massive meteor shower lights up the sky.")
            f1 = random.randint(1, 50)

            if f1 in [1, 50]:
                print("You found a meteor piece and sold it for $1,000,000!")
                mo += 1000000
            else:
                print("The sky looked beautiful tonight.")
                h += 50

        elif f == 101:
            print("⚫ Super Rare Dark Event")
            f2 = input("An evil group offers anime powers. Accept? (yes/no) ")

            if f2.lower() == "yes":
                print("You gained the powers of Yuji's mom...")
                immortal = True
            else:
                print("Smart choice.")

        cap()

    # ---------- Random Daily Event ----------

    if d >= 2:

        if ev == 1:
            print("You found $10!")
            h += 7
            mo += 10

        elif ev == 2:
            print("You caught a cold!")
            h -= 10
            he -= 17
            mo -= 10

        elif ev == 4:
            print("You made a new friend!")
            h += 10

        else:
            print("A normal start to the day.")

        cap()

    # ---------- Morning ----------

    c1 = input("Sleep more? (yes/no) ")

    if c1.lower() == "yes":
        print("You slept more.")
        he -= 10
        e += 14
        h += 9
        cap()

    elif c1.lower() == "no":

        c2 = input("Exercise or watch KNY? ")

        if c2.lower() == "exercise":
            print("You exercised.")
            h += 16
            e -= 9
            he += 10

        elif c2.lower() == "watch kny":
            print("You watched Demon Slayer.")
            h += 10
            e -= 10
            he -= 2

        else:
            print("Invalid choice")

        cap()

    # ---------- Afternoon ----------

    print("It's Afternoon.")

    c3 = input("Sleep / Watch meme / Study / Work? ")

    if c3.lower() == "sleep":
        print("You slept.")
        h -= 10
        e -= 17
        he -= 18

    elif c3.lower() == "watch meme":
        print("You watched memes.")
        he -= 10
        e -= 15
        h += 10

    elif c3.lower() == "study":
        print("You studied.")
        he -= 9
        e -= 10
        h -= 9
        iq += 19

    elif c3.lower() == "work":
        print("You worked.")
        he -= 7
        e -= 10
        h -= 8
        mo += 10

    else:
        print("Invalid choice")

    cap()

    # ---------- Night ----------

    print("It's night.")

    c5 = input("Play / Study / Eat? ")

    if c5.lower() == "play":
        print("You played.")
        he += 8
        e -= 10
        h += 9

    elif c5.lower() == "study":
        print("You studied.")
        he -= 8
        e -= 9
        h -= 10
        iq += 20

    elif c5.lower() == "eat":
        print("You ate.")
        e += 6
        he += 6
        h += 8

    else:
        print("Invalid choice")

    cap()

    print("You slept for the night.")

    # ---------- Death Check ----------

    if he <= 0:
        if immortal:
            print("💀 Your body died, but you jumped to a new one.")
            he = 50
            h -= 10
        else:
            print("💀 You collapsed and died.")
            print("Game Over on Day", d)
            break

    # ---------- Immortal Ending ----------

    if age >= 100 and immortal:
        print("You are now known by many names.")
        print("You are like Kenjaku now. No longer human.")

        f3 = input("Attack humanity or rest peacefully? (attack/rest) ")

        if f3.lower() == "attack":
            print("Your dark plan begins... but eventually your legend fades.")
        else:
            print("You finally rest after centuries.")

        break

    # ---------- Next Day ----------

    d += 1

    # ---------- Unlock More Days ----------

    if d > ma:
        n = input("Unlock 10 more days for $10? (yes/no) ")

        if n.lower() == "yes" and mo >= 10:
            mo -= 10
            ma += 10
            print("10 more days unlocked!")

        elif n.lower() == "yes":
            print("Not enough money!")
            break

        else:
            print("Game Over!")
            break


print("\nFinal Stats")
print("Health:", he)
print("Energy:", e)
print("Happiness:", h)
print("Money:", mo)
print("IQ:", iq)
