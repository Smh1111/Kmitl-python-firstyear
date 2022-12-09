def isAnagram(String1, String2):
    list1, list2 = [], []

    for i in String1:
        list1.append(i)
        
    for i in String2:
        list2.append(i)

    isAnagram = True
    for i in list1:
        if i in list2:
            continue
        else:
            isAnagram = False

    return isAnagram

def main():
    print(isAnagram("listen", "silent"))
    print(isAnagram("hi", "hello"))

main()