def greet(lang):
    if lang=='en':
        return 'Hello'      #Here return ends the function execution and returns 'Hello'.
    elif lang=='es':
        return 'Hola'       #Similarly , returns 'Hola'
    elif lang=='fr':
        return 'Bonjour'    #and'Bonjour'
Name = input("Enter Your name: ")
lang =input("What lang do you speak en,es,fr? ")
print(greet(lang),Name)