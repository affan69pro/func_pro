def shut(down):
    if down=="yes":
        return print("Shutting down⚡")
    else:
        return print("Not shutting down...")

num=(input("enter yes or no : "))
sum=shut(num)
print(sum)