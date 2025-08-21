import random
namn = input("Who are you?")
namn.strip().lower()
print(f"Hej, {namn}!)
antalfragor = input("How many questions do you want?")
for _ in range(antalfragor):
  villkenfraga = random.randint(1, 3)
    if vilkenfraga == 1:
      svar=input("Who wrote the book where 42 is the answer to the ultimate qustion?")
        svar.strip().lower()
        if svar == "douglas adams":
          print("Great!")
        else: 
        print("Wrong, the right answer is Douglas adams.)
  
