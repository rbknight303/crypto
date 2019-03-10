""" crypto.py
    Implements a simple substitution cypher
"""
#two list of characters that are encoded into another list
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"

#create main function and define
def main():
    #defining a condition
    keepGoing = True
    #loop starts while checking the condition
    while keepGoing:
        #create a variable for menu function
        response = menu()
        #create an if condition and state what to do if true
        if response == "1":
          #take user input and store in into a variable  
          plain = input("text to be encoded: ")
          #prints the encoded word
          print(encode(plain))
        #create second if condition and state what to do if true  
        elif response == "2":
          #take user input and store in into a variable
          coded = input("code to be decyphered: ")
          #prints the decoded word
          print (decode(coded))
        #create third if condition and state what to do if true
        elif response == "0":
          #print a response   
          print ("Thanks for doing secret spy stuff with me.")
          #end of loop after this condition is true
          keepGoing = False
        #create last condition and state waht to do if all of the above are false  
        else:
          #print a response  
          print ("I don't know what you want to do...")
          
#menu function created and defined 
def menu():
    print("Russian Decoder")
    print("\n0) Quit")
    print("1) Encode")
    print("2) Decode")
    answer =input("\n What do you need from me?")
    return answer

#create coding function that takes input and encodes it
def encode(plain):
    output = ""
    #convert plain letters to upper case
    plain = plain.upper()
    #create loop that checks if letters in plain are in alpha
    for letter in plain:
        if letter in alpha:
            #find letters in alpha and store in table
            table = alpha.find(letter)
            #find those letter translated in key and store in letterSwap
            letterSwap = key[table]
            output = output + letterSwap
    #return to menu and print secret        
    return output

#create decoded function that decodes the coded letter
def decode(coded):
    output = ""
    #convert coded letters to uppercase
    coded = coded.upper()
    #create for loop and look for letters in key and alpha
    for letter in coded:
        #create if condition and state look for the letters input in key
        if letter in key:
            #check if letters are in key and store in table
            table = key.find(letter)
            #check if letters are in alpha and store in letterSwap
            letterSwap = alpha[table]
            output = output + letterSwap
    #return back to menu and print output        
    return output
main()

