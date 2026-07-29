text = " helo world"
print(text.upper())
print(text.lower())
print(len(text))
print(text.replace("world","loki"))
print(text.split(" "))
print(text.count("l"))
print(text[0:5])
print(text[6:])
print(text[:5])


name = " loki sharma "
print(name.strip())
print(name.strip().upper())
print(name.find( "s"))


name = "loki"
print(name[::-1])
print(name[::2])

word = input("enter a word")
if word == word[::-1]:
    print("palindrome")
else:
    print("not palindrome")
    
word = input("enter a word")
count = 0
for letter in word:
    if letter in "aeiou" :
        count= count+1

print("vowels:",count)

sentence = input("enter a sentence :")
words = sentence.split(" ")
print("word count :", len (words))
