# wordfreq.py

import os
def byFreq(pair):
    return pair[1]

def main():
    print("This program analyzes word frequency in a file")
    print("and prints a report on the n most frequent words.\n")
    
    # get the sequence of words from the file
    fnum = input("What folder do you want to analyze? ")

    fnames = os.listdir(fnum)
    os.chdir(fnum)
    

    for i in fnames:
        if i == ".DS_Store":
            fnames.remove(i)
            
    counts = {}
    print ("All files:")
    for i in range(len(fnames)):
        text = open(fnames[i],'r').read()
        text = text.lower()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            text = text.replace(ch, ' ')
        words = text.split()
        # construct a dictionary of word counts
        for w in words:
            counts[w] = counts.get(w,0) + 1
            
    # output analysis of n most frequent words.
    n = eval(input("Overall output analysis of how many words? "))
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))

    print("")
    for i in range(len(fnames)):
        readfile(fnames[i], n)


    
#read file
def readfile(file, n):
    text = open(file,'r').read()
    print(file + ":")
    
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text = text.replace(ch, ' ')
    words = text.split()
    #print("text split")
    # construct a dictionary of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1
    #print("dict created")
    # output analysis of n most frequent words.
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))
    print("")
        
main()
#if __name__ == '__main__':  main()
