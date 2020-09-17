#This is the pet-bot chat bot. This bot will ask whether you like dogs or cats better
# and will respond accordingly. To end the program the user must input 'done'. To choose dogs
#the user must input 'dogs', to choose cats the user must inout 'cats', otherwise the pet-bot chat breakpoint
#will notify the user that his/her input was invalid. Have fun, make a new friend!

#imports choice method from random class
from random import choice

#function definition for getting bot's response
def get_bot_response(user_response):

  #Declaration and initialization of dog responses and cat responses lists
  dog_resp, cat_resp =["Dogs are the best!", "I love dogs too!!", "You read my mind!"],["Cats are awesome, forget about dogs!", "Great minds think alike ;)","Friendly felines forever!"]

  #Decides what response to print based on user response and prints it.
  print("\npet-bot:","Alrighty, bye!"if user_response=="done"else choice(dog_resp)if user_response=="dogs"else choice(cat_resp)if user_response=="cats"else"That wasn't an option","\n")

  #Returns whether or not the user wants to quit
  return user_response!="done"

#Prints the welcome message and input instructions
print("pet-bot: Hi, I'm pet-bot.\nDo you like dogs or cats better? Enter \"dogs\" or \"cats\"\n")

#Continuously calls get_bot_response function until the user enters 'done'
while get_bot_response(input("\nuser: ")):continue

#I know my function doesn't return the bot's response, 
#but I figured since it was a little higher level approach you'd be cool with it