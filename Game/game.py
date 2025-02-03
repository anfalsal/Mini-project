
wantplay = input(" Do you want to play ?  ")
if wantplay.lower() != "yes": #I want the code to always convert the letters to lowercase then read them
    quit()

print("lets start")

q1 = input("What color is the sky? ")
if q1.lower() == "blue":
    print("correct!")
else:
    print("Incorrect!")
    quit()

q2 = input("Who is the tallest animal? ")
if q2.lower() == "giraffe":
    print("correct!")
else:
    print("Incorrect!")
    quit()

q3 = input(" What is the capital of Indi?  ")
if q3.lower() == "delhi":
    print("correct!")
else:
    print("Incorrect!")
    quit()

# I can write more questions on the same system...
