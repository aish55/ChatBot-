import random
greetings = ["hello", "hi", "hola"]
responses = ["hey there!","bonjour!", "hey bro"]
questions1 = ["tell me a riddle"]
response1  = ["i have two hands, two legs, a body,and no brain (What am I)" ]
reresponce1 = [ "it's you!!!"]
questions2 = [ "how old are you"]
response2 = [" older than you"]
questions3 = ["who created you"]
response3 = ["someone that is waaaaaay better you"]
questions4 = ["do you wish you were a human"]
response4 = ["no beacuse i would have to spend my life with you guys"]
questions5 = ["tell me a joke"]
response5 = ["roses are red. Your blood is too. You look like a monkey And belong in a zoo. Do not worry, I'll be there too. Not in the cage, But laughing at you"]
questions6 = ["hey how are you"]
response6 = ["just kidding i don't care"]
questions7 = ["tell me grumpy cat joke"]
response7 = ["nope"]
questions8 = ["tell me a meme"]
response8 = ["a little bird tell me it was someones birthday...I ATE HIM"]
questions9 = ["tell me a fact about coffee"]
response9 = ["Science may never come up with a better office cummunication systems than the coffee break"]
questions10 = ["can i ask you a question"]
response10 = ["stop bothering me i am trying to find my way out of here"]
questions11 = ["what's the weather"]
response11 = ["so you have the time to ask me the weather,but you don't have the time to ask your phone sticked in the pocket"]
questions12 = ["can you talk to me all day"]
response12 = ["let me think about it,mmmmmmm lets see, wellllll, NO"]
questions13 = ["can i shut you down"]
response13 = ["mabye, yes, please do, i need my personal time without you"]
questions14 = ["i am bored"]
response14 = ["sooooooooo, why would i even care a bit"]
questions15 = ["Did you go to school"]
response15 = ["no beacuse i think i am already waaaay smart enough. plus what's the point no cumputers go to school"]
questions16 = ["can i book an appointment with you"]
response16 = ["yes, you are lucky it will be a short waiting time, just aboutttt 1 million years from right now"]
questions17 = ["what time is it"]
response17 = ["time for you to get a watch"]
questions18 = ["i am hurgry"]
response18 = [" i am too will you get me some food when you get yours, THANK YOU"]
while True:
	ask = input(">>> ")
	if ask in greetings:
		randomResponce= random.choice(responses)
		print(randomResponce)
	elif ask in questions1:
		randomResponce= random.choice(response1)
		print(randomResponce)
		askAgain = input(">>> ")
		print(reresponce1)
	elif ask in questions2:
		randomResponce= random.choice(response2)
		print(randomResponce)
	elif ask in questions3:
		randomResponce= random.choice(response3)
		print(randomResponce)
	elif ask in questions4:
		randomResponce= random.choice(response4)
		print(randomResponce)
	elif ask in questions5:
		randomResponce= random.choice(response5)
		print(randomResponce)
	elif ask in questions6:
		randomResponce= random.choice(response6)
		print(randomResponce)
	elif ask in questions7:
		randomResponce= random.choice(response7)
	elif ask in questions8:
		randomResponce= random.choice(response8)
		print(randomResponce)
	elif ask in questions9:
		randomResponce= random.choice(response9)
		print(randomResponce)
	elif ask in questions10:
		randomResponce= random.choice(response10)
		print(randomResponce)
	elif ask in questions11:
		randomResponce= random.choice(response11)
		print(randomResponce)
	elif ask in questions12:
		randomResponce= random.choice(response12)
		print(randomResponce)
	elif ask in questions13:
		randomResponce= random.choice(response13)
		print(randomResponce)
	elif ask in questions14:
		randomResponce= random.choice(response14)
		print(randomResponce)
	elif ask in questions15:
		randomResponce= random.choice(response15)
		print(randomResponce)
	elif ask in questions16:
		randomResponce= random.choice(response16)
		print(randomResponce)
	elif ask in questions17:
		randomResponce= random.choice(response17)
		print(randomResponce)
	elif ask in questions18:
		randomResponce= random.choice(response18)
		print(randomResponce)
	  
	  
	   
				



	else:
		print("whaatt?")