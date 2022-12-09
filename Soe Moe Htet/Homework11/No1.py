set1 =  {
                "be": "b",
                "because": "cuz",
                "see": "c",
                "the": "da",
                "okay": "ok",
                "are": "r",
                "you": "u",
                "without": "w/o",
                "why": "y",
                "see you": "cu",
                "ate": "8",
                "great": "gr8",
                "mate": "m8",
                "wait": "w8",
                "later": "!8r",
                "tomorrow": "tmr",
                "for": "4",
                "before": "b4",
                "once": "1ce",
                "and": "&",
                "Your": "ur",
                "You're": "ur",
                "As far as I know": "afaik",
                "As soon as possible": "asap",
                "At the moment": "atm",
                "Be right back": "brb",
                "By the way": "btw",
                "For your information": "FYI",
                "In my humble opinion": "imho",
                "In my opinion": "imo",
                "Laughing out loud": "lol",
                "Oh my god": "omg",
                "Rolling on the floor laughing": "rofl",
                "Talking to you later": "ttyl",
            }

def textese(s):
    plain_text = s
    for key, value in set1.items():
        plain_text = plain_text.replace(key, value)
                
    return plain_text
       
def untextese(s):
    short_form = ""
    short_form = s.split(" ")

    i = 0
    while(i != len(short_form)):
        if ( short_form[i][ len(short_form[i]) -1 ] == ","):
            short_form[i] = short_form[i].strip(",")
            short_form.insert(i+1, ",")
            i += 2
    
        else:
            i += 1
    
    normal_form = ""
    for i in short_form:
        temp = ""

        for j in range(len(i)):
            temp += i[j]
            if (j == len(i) - 1):
                for key, value in set1.items():
                    if (temp == value):
                        temp = key

        if (temp == ","):
            normal_form = normal_form.strip()
            normal_form += temp + " "
        else:
            normal_form += temp + " " 
    return normal_form

def main():
    text = "In my opinion, Your hair looks okay and great, but you ate my food"
    
    short_form = textese(text)
    print(short_form)

    normal_form = untextese(short_form)
    print(normal_form)
main()