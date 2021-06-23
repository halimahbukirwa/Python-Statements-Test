# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

lst = [word[0] for word in st.split() if len(word)%2 == 0]

print(lst)