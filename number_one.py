# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

for letter in st.split():
    if letter[0] == 's':
        print(letter)