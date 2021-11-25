# counts the number of words in tom sawyer

# open the file
book=open("tomsawyer.txt")

# counts num words by splitting on spaces
num_words = len(book.read().split())
print(num_words)

book.close()

# another way to count
book=open("tomsawyer.txt")
count = 0
for x in book.read().split():
    count+=1
print(count)

book.close()
