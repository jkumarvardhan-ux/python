score = 0
print("\n1. What is the output of print(5 + 3)?")
print("A) 53")
print("B) 8")
print("C) 15")
print("D) None")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("\n2. Which function is used to find the sum of a list?")
print("A) add()")
print("B) total()")
print("C) sum()")
print("D) calc()")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n3. What is the output of sum([1, 2, 3])?")
print("A) 6")
print("B) 123")
print("C) 5")
print("D) Error")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "A":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n4. What is the output of print(10 - 4)?")
print("A) 14")
print("B) 6")
print("C) 4")
print("D) 40")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n5. Which symbol is used for multiplication in Python?")
print("A) x")
print("B) *")
print("C) %")
print("D) #")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n6. What is the output of print(20 // 3)?")
print("A) 6")
print("B) 6.67")
print("C) 7")
print("D) Error")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "A":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n7. What is the output of len('Python')?")
print("A) 5")
print("B) 7")
print("C) 6")
print("D) Error")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n8. Which keyword is used to define a function?")
print("A) function")
print("B) define")
print("C) func")
print("D) def")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "D":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n9. What is the output of print(2 ** 3)?")
print("A) 6")
print("B) 8")
print("C) 9")
print("D) 23")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n10. Which data type stores True or False values?")
print("A) int")
print("B) str")
print("C) bool")
print("D) float")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQuiz Completed!")
print("Your Score:", score, "/ 10")