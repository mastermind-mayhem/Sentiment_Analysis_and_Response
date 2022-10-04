# import os, time, math

feels = 5
fphrase = ""

while True:
    try:
        # for _ in range(30):
        #     print(" ")
        phrase = input("Enter Phrase: ")
        phrase = phrase.lower()
        phrase = phrase.split()

        with open("stopwords.txt", "r")as w:
            stops = w.readlines()
            # print(stops)
            known = False
            for phrases in phrase:
                outlier = False
                for stop in stops:
                    item = stop[:stop.index("\n")]
                    # print(item, phrases)
                    if item == phrases:
                        outlier = True
                if outlier == False:
                    with open("negative.txt", "r")as q:
                        negative = q.readlines()
                        for negate in negative:
                            negate = negate[:negate.index("\n")]
                            # print(negate, phrases)
                            if phrases == negate:
                                print("I recognized that as an insult")
                                feels = feels - 1
                                known = True

                    with open("positive.txt", "r")as q:
                        positive = q.readlines()
                        for posit in positive:
                            posit = posit[:posit.index("\n")]
                            # print(posit, phrases)
                            if phrases == posit:
                                print("I recognized that as a compliment")
                                feels = feels + 1
                                known = True

                                # continue

# Put in function to utilize continue properly
                    try:
                        if known == False:
                            print("--- ERROR ---")
                            print(phrases, "<- This word is unknown")
                            meaning = input("Negative, positive, or neither: ")
                            if "negative" in meaning:
                                with open("negative.txt","a")as r:
                                    r.writelines(phrases+"\n")
                                print("Negative - Added", phrases)
                                feels = feels - 1
                            elif "positive" in meaning:
                                with open("positive.txt","a")as r:
                                    r.writelines(phrases+"\n")
                                    print("Positive - Added", phrases)
                                    feels = feels + 1
                            elif "neither" in meaning:
                                with open("stopwords.txt","a")as r:
                                    r.writelines(phrases+"\n")
                                print("Neither - Added", phrases)
                    except KeyboardInterrupt:
                        print(' ')
                        print(' ')
                        continue
    except KeyboardInterrupt:
        exit()

# Feelings pre-process
    if feels > 10:
        feels = 10
    elif feels < 0:
        feels = 0
    # print('Feelings: '+str(feels))

# Feelings Processing
    phrases = {
        "10": "cheerful",
        "9": "joyful",
        "8": "some what joyful",
        "7": "happy",
        "6": "pleased",
        "5": "normal",
        "4": "slightly sad",
        "3": "sad",
        "2": "frustrated",
        "1": "angry",
        "0": "pissed",
    }

    for phrase, command in phrases.items():

        if int(phrase) == int(feels):
            fphrase = command

    print("I'm currently feeling "+fphrase)
    for _ in range(3):
        print("     ")
