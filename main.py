from random import choice

def get_bot_response(user_response):
  if(user_response=="done"):
    return "done"
  bot_responses1=["I love dogs too!!", "I like cats, but I think dogs are better too.", "You read my mind!"]
  bot_responses2= ["Cats are adorable, forget about dogs.", "Great minds think alike ;)","Friendly felines forever!"]
  print(choice(bot_responses1) if user_response=="dogs" else choice(bot_responses2) if user_response=="cats"else "That wasn't an option")
  return user_response
  
print("Welcome to the pet lovers chat bot! Here we like to talk about our pets.")
while(True):
  response = get_bot_response(input("Do you like dogs or cats better? "))
  if(response=="done"):
    break
  
