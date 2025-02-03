counts = dict()
line = input("Enter a line of text: ")      #input    
words = line.split()                        # Splitting the line into words
print("Words",words)
print("Counting...")
for word in words:
    counts[word] = counts.get(word,0)+1    #Counting words and storing it the keys 'Words'.....
print("Counts",counts)
#Printing dictionaries by going through it using 