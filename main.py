from random import choice
def get_bot_response(user_response):
  dog_resp, cat_resp =["Dogs are the best!", "I love dogs too!!", "You read my mind!"],["Cats are awesome, forget about dogs!", "Great minds think alike ;)","Friendly felines forever!"]
  print("\npet-bot:","Alrighty, bye!"if user_response=="done"else choice(dog_resp)if user_response=="dogs"else choice(cat_resp)if user_response=="cats"else"That wasn't an option","\n")
  return user_response!="done"
print("pet-bot: Hi, I'm pet-bot.\nDo you like dogs or cats better? Enter \"dogs\" or \"cats\"\n")
while get_bot_response(input("\nuser: ")):continue
#I know my function doesn't return the bot's response, 
#but I figured since it was a little higher level approach you'd be cool with it