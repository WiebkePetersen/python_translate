# translate.py
# task: performs simple translations between German, English and Swedish words
#       and calculates the average similarity between the translations in a naive way
#       Demonstrates the use of .index(), the embedding of for-loops, and the use of functions    
# author: Wiebke Petersen (based on a script by Johanna Andrees)
# created: 12.5.2015
# last changed: 12.5.2015


##############################################################
# functions
##############################################################

def translate(word):
    '''string -> (string,string,string)
    takes a word and returns a triple consisting of the word in
    German
    English
    Swedish
    '''
    if word in list(DE_EN.keys()):
        return(word,DE_EN[word],DE_SV[word])
    if word in list(DE_EN.values()):
        word_index = list(DE_EN.values()).index(word)
        word_de = list(DE_EN.keys())[word_index]
        return(word_de,word,DE_SV[word_de])
    if word in list(DE_SV.values()):
        word_index = list(DE_SV.values()).index(word)
        word_de = list(DE_SV.keys())[word_index]
        return(word_de,DE_EN[word_de],word)
    else:
        return(False)

# Diese Funktion war nicht Teil der ursprünglichen Aufgabe
def aehnlichkeit(wordtuple):
    '''tuple -> float
    Takes a tuple of three strings and returns the average number of
    common characters between pairs of two strings
    >>>aehnlichkeit(("abc","ddd","efff"))
    0.0
    >>>aehnlichkeit(("abc","cdb","cad"))
    2.0

    Vorsicht: Reihenfolge der Elemente des Tupels beeinflusst Zählung:
    >>> aehnlichkeit(("aaa","aaa","a"))
    3.0
    >>> aehnlichkeit(("a","aaa","aaa"))
    1.6666666666666667

    Die Funktion dient primär der Veranschaulichung, wie man aus einem
    listenähnlichen Objekt (Liste, String, Tuple,...) alle Teilmengen mit
    zwei Elementen konstruieren kann.
    '''
    c=0  # Initialisierung des Counters
    for i in range(2):
        for j in range(i+1,3):
            for l in wordtuple[i]:
                if l in wordtuple[j]:
                    c=c+1
    return(c/3)

##############################################################
# executed part
##############################################################

# Definition der Wörterbücher
Deutsch = ["Tasche", "Fahrrad", "Haus", "Apfel"]
Englisch = ["bag", "bicycle", "house", "apple"]
Schwedisch = ["väska", "cykel", "hus", "äpple"]
DE_EN = dict(zip(Deutsch,Englisch))
DE_SV = dict(zip(Deutsch,Schwedisch))


# Initialisierung
anweisung = '''Bitte geben sie das zu übersetzende Wort ein (drücken sie Enter um das Programm zu stoppen): '''
user_in = input(anweisung)

# wiederholter Aufruf 
while not user_in == "":   # Abbruchbedingung 
    t = translate(user_in)
    if t==False:    # abfangen von Fehlern
        print("dies ist kein gültiges deutsches, englisches oder schwedisches Wort!")
    else:
        print("Deutsch: ",t[0])
        print("Englisch: ",t[1])
        print("Schwedisch: ",t[2],"\n")
        # Hier zum Spass noch ein völlig naiver Test auf Wortverwandtschaft:
        print("je zwei der Wörter stimmen im Schnitt in",aehnlichkeit(t), "Buchstaben überein.")
        if ((len(t[0])+len(t[1])+len(t[2])) / 3) / aehnlichkeit(t) < 2:
            print("Angesichts der Wortlängen, sind sie eher ähnlich")
        else:    
            print("Angesichts der Wortlängen, sind sie eher nicht ähnlich")  
    user_in = input(anweisung)

        
        
        


    

    

