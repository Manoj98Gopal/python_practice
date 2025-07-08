

# A string is sequence of character , it can hold  letters,numbers,emoji and symbols
# String are  immutable -> they cannot be change in the place 


name = "Manoj"
message = "Hello  I am learning python"
emoji = "😊"


# Indexing : accessing sequence of characters
text = "Python"
print(text[0])   # P
print(text[-1])  # n
print(text[1])   # y


# Slicing
print(text[0:3])    # Pyt
print(text[1:-1])   # ython
print(text[:3])     # Pyt
print(text[3:])     # hon
print(text[:])      # Python
print(text[-3:])    # hon


# concatenation
first = "Hello"
second = "World"

result = first + " " + second
print(result)


# Repetition
laugh = "Ha" * 3
print(laugh)


# Membership  : checking letter is present in that word
word = "python"

print("p" in word)  # boolean value  True
print("x" in word)  # False


# string methods
text1 = "Hello World"

print(text1.upper())      # HELLO WORLD
print(text1.lower())      # hello world
print(text1.capitalize()) # Hello World
print(text1.swapcase())   #hELLO wORLD
print(text1.title())      #Hello world


# striping whitespace
line = "      Hello        "

print(line)            # "     Hello     "
print(line.strip())    # "Hello"
print(line.rstrip())   # "     Hello"
print(line.lstrip())   # "Hello     "



# finding and counting
sentence = "Python is easy, Python is powerful"

print(sentence.find("Python"))    #0
print(sentence.rfind("Python"))   #16
print(sentence.count("Python"))   #2



# replace text 
text2 = "Hello World!"
new_text = text2.replace("World","Python")

print("old text : ",text2)
print("new text : ",new_text)


# split and  join

data = "apple,banana,cherry"


result1 = data.split(",")
# split
print(result1)

# join
print(" & ".join(result1))



# check start and end
filename = "document.pdf"

print(filename.startswith("doc"))
print(filename.endswith("pdf"))


