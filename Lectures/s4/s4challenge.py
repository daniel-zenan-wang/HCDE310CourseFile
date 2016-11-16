f = open("sherlock.txt",'r')
fstring = f.read()    #assign fstring long string with the whole file


# This is a function that will replace (most) punctuation
# you'll see it again in the homework
def stripWordPunctuation(word):
    return word.strip(".,()<>\"\\'~?!-;*/")

wordlist = fstring.split()

### Challenge 0: count the number of times the words
### elementary and obviously appear in Sherlock Holmes
### note that we have already opened, read, and split the
### file for you above

### fill in your code here
count_elem = 0
count_obviously = 0
for word in wordlist:
    word = stripWordPunctuation(word).lower()
    if word == 'elementary':
        count_elem += 1
    elif word == 'obviously':
        count_obviously += 1
print count_elem 
print count_obviously

### Challenge 1: modify the code below to print
### all of the words that appear more than 10 times
### and the number of times they appear
###
###
### Challenge 2: modify and add to your code
### to print the word that appears the most.
### Extra challenge 1: make all words lower case first.
### Extra challenge 2: remove punctuation using 
###                    stripWordPunctuation()

freqs = {}   #an empty dictionary to keep track of frequency
for word in wordlist: 
    word = stripWordPunctuation(word).lower()
    freqs[word] = freqs.get(word,0) + 1
print freqs


for k in freqs.keys():
    if freqs[k] > 10:
        print k + ' appears ' + str(freqs[k]) + ' times.'
    
max_so_far = 0
word = " "
for k in freqs.keys():
    v = freqs[k]
    if v > max_so_far: 
        max_so_far = v
        word = k
        
print "The most frequent word -" + word + "- appears " + str(max_so_far) + " times." 
# tally

# print tally
# printing only words appearing more than 10 times