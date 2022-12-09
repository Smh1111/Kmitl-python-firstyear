# def time24hourTo12hour():
#     print()

def main():
    time = "23:00"

    hour = int(time[0] + time[1])
    
    if(hour > 12):
        print(f"{hour - 12}:{time[3]}{time[4]} PM")
    else:
        print(f"{hour}:{time[3]}{time[4]} AM")
        

main()