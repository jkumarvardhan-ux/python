age=int(input("enter age:"))
card=input("enter card:").lower()
if age>18 and card=="yes":
    print("eligible")
else:
    print("not eligible")
