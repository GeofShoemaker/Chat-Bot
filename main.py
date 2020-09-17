from random import choice

def get_bot_response(user_response):
  dog_resp, cat_resp =["I love dogs too!!", "I like cats, but I think dogs are better too.", "You read my mind!"],["Cats are adorable, forget about dogs.", "Great minds think alike ;)","Friendly felines forever!"]
  print("\npet-bot: ","Alrighty, bye!" if user_response=="done" else choice(dog_resp) if user_response=="dogs" else choice(cat_resp) if user_response=="cats"else "That wasn't an option","\n")
  return   user_response!="done"

print("pet-bot: Welcome to the pet lovers chat bot! Here we like to talk about our pets.\n")
while get_bot_response(input("Do you like dogs or cats better? Enter \"dogs\" or \"cats\"\nyou: ")):continue





  
