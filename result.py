name=input("enter name:").lower()
marks=int(input("enter marks:"))
if marks>=90:
    grade="a"
elif marks>80:
    grade="b"
elif marks>70:
    grade="c"
elif marks>40:
    grade="e"
elif marks<40:
    grade="fail"
print(f"name:{name}\nmarks:{marks}\ngrade:{grade}")
