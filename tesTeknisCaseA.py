sentence = '''Since 1995, Java has changed our world . . . and our expectations.. 
Today, with technology such a part of our daily lives, we take it for granted that we 
can be connected and access applications and content anywhere, anytime. Because of Java, 
we expect digital devices to be smarter, more functional, and way more entertaining.
 In the early 90s, extending the power of network computing to the activities of everyday
 life was a radical vision. In 1991, a small group of Sun engineers called the "Green Team"
 believed that the next wave in computing was the union of digital consumer 
 devices and computers. Led by James Gosling, the team worked around the clock 
 and created the programming language that would revolutionize our world – Java.
 The Green Team demonstrated their new language with an interactive,
 handheld home-entertainment controller that was originally targeted at the digital
 cable television industry. Unfortunately, the concept was much too advanced for
 the them at the time. But it was just right for the Internet, which was just starting
 to take off. In 1995, the team announced that the Netscape Navigator Internet browser
 would incorporate Java technology. Today, Java not only permeates the Internet,
 but also is the invisible force behind many of the applications and devices that
 power our day-to-day lives. From mobile phones to handheld devices, games and navigation
 systems to e-business solutions, Java is everywhere!'''

sentenceList = list(sentence.split(" "))

def wordCounter():
    words = len(sentence.split())
    print('Total words = ' + str(words))
    
def eachWordCounter():
    from collections import Counter
    count = Counter(sentenceList)
    print(count)

def once():
    from collections import Counter

    count = Counter(sentenceList)
    leastOccuredWord = set(k for k,v in count.items() if v==1)
    jmlkata = len(leastOccuredWord)

    print('Jumlah kata yang muncul 1x : ' + '%s' %jmlkata)

def mostWord():
    from collections import defaultdict
    from collections import Counter
    
    sentenceList = list(sentence.split(" "))
    temp = defaultdict(int)

    for sub in sentenceList:
       for wrd in sub.split():
            temp[wrd] += 1

    res = max(temp, key=temp.get)
    count = Counter(sentenceList)
    most_ouc = count.most_common(1)
    leastOccuredWord = set(k for k,v in count.items() if v==most_ouc[0][1])
    jmlkata = len(leastOccuredWord)
    print('Jumlah kata yang paling banyak muncul : ' + str(jmlkata))
    print("Kata yang paling banyak muncul : " + str(res))

def leastWord():
    from collections import Counter

    count = Counter(sentenceList)
    leastOccuredWord = set(k for k,v in count.items() if v==1)
    jmlkata = len(leastOccuredWord)

    print('Jumlah kata yang paling sedikit muncul : ' + str(jmlkata))
    print('Kata yang paling sedikit muncul adalah : ' + str(leastOccuredWord))

wordCounter()
eachWordCounter()
once()
mostWord()
leastWord()
