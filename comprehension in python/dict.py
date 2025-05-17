# create a dictionary of csquare{where key are number and values are square }
squ_dict={x:x**2 for x in range(1,9)}
print(squ_dict)

# create a dictionary with only even and their square
even_dict={x:x**2 for x in range(10) if x%2==0}
print(even_dict)

# create a dictionary with only odd and their square
odd_dict={x:x**2 for x in range(10) if x%2!=0}
print(odd_dict)


# reverse a dictionary
original={"a":1,"b":2,"c":3}
rev_dict={v:k for k,v in original.items()}
print(rev_dict)


# convert list to ditionary with lengths
words=["apple","banana","cheery"]
length_dict={word:len(word) for word in words}
print(length_dict)



# convert list to ditionary with lengths
words=["apple","banana","cheery"]
for word in words:
    length_dict={word:len(word)}
    print(length_dict)


# create a dictionary where keys are numbers and values are "even" or "odd" depending on the number  
evenodd_dict={x:('even'if x%2==0 else 'odd') for x in range(1,6)}
print(evenodd_dict)
