# Challenge Task 1 of 2
# Create a function named square. It should define a single parameter named number.
# In the body of the function return the square of the value passed in.
# (A square is the value multiplied by itself. eg: The square of 5 is 25. 25 = 5 x 5)

def square(number):
    value = number * number
    return(value)

print(square(3))


#<------------------------------------------------------------------------------->#


# I need you to finish writing a function for me. The function disemvowel takes a single word as a parameter and then returns that word at the end.
# I need you to make it so, inside of the function, all of the vowels ("a", "e", "i", "o", and "u") are removed from the word. Solve this however you want, it's totally up to you!
# Oh, be sure to look for both uppercase and lowercase vowels!

# IDEA:  break word up into a list, remove letters, bring word back together as one 

def disemvowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter.lower() in vowels:
            word = word.replace(letter, "")
    return word

print(disemvowel("This is a test"))

