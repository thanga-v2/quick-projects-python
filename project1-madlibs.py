# based on user input, will create funny stories

def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}:")
    return user_input


noun1 = get_input("noun")
adjective = get_input("adjective")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")


# print(noun1, noun2, verb1, verb2)
# Enter a noun:thanga
# Enter a adjective:drowsy
# Enter a verb:playing
# Enter a noun:guru
# Enter a verb:watching



story = f"""
Once upon a time, there lived a {adjective}{noun1}, he was {verb1} by then.


Wanna party hard? {noun2} is {verb2}

{noun1}: hey hi what are you doing?
{noun2}: why are you {verb1}
{noun1}: Oh glad i knew that.
{noun2}: Ok lets catch up. Im {verb2}
{noun1}: I almost forgot. I am {adjective} now.

"""""

print(story)