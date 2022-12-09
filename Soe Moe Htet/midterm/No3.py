print("Enter a time in 24 hour format.")

origin = eval(input("Hours: "))
minutes = eval(input("Minutes: "))
seconds = eval(input("Seconds: "))

hours = origin

if hours > 12:
    hours = hours - 12
else:
    hours = hours

if hours < 10:
    print(f"The time you just entered in 12 hour format is 0{hours}:", end = "")

else:
    print(f"The time you just entered in 12 hour format is {hours}:", end = "")
    
if minutes < 10:
    print(f"0{minutes}:", end="")

else:
    print(f"{minutes}:", end ="")

if seconds < 10:
    print(f"0{seconds}", end="")

else:
    print(f"{seconds}", end ="")

if origin > 12:
    print("PM.")
else:
    print("AM.")
