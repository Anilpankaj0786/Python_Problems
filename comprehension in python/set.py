# creating a set of square 
square={x**2 for x in range(1,6)}
print(square)


# filtering even number
even={x for x in range(10) if x%2==0}
print(even)


# extracting unique vowels from a string 
sentence="hello world"
vowel={char for char in sentence if char in "aeiou"}
print(vowel)
