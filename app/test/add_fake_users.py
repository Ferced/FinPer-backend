# importing the requests library 
import requests 
  
# defining the api-endpoint  
import requests
import random
def add_user(username):
	url = "http://localhost:5000/user/"
	headers = {'Content-type': 'application/json'}
	data = {
		'email': username+'@gmail.com',
		'username': username,
		'password': 'test',
		'public_id':username
		} 
	r = requests.post(url = url,json=data,headers=headers) 
	# extracting response text  
	pastebin_url = r.text 
	print("The pastebin URL is:%s"%pastebin_url) 
	print ("------------------------------------------------------------------")

def add_fake_credit_cards(username):
	credit_card_network_list=["VISA","MASTERCARD","AMERICAN EXPRESS"]
	credit_card_bank_list=["Galicia","Macro","HSBC","Santander","ICBC","Nacion","City"]
	credit_card_bank_name = credit_card_bank_list[random.randint(0,len(credit_card_bank_list)-1)]
	credit_last_four_numbers = random.randint(1000,9999)
	credit_card_network_bank = credit_card_network_list[random.randint(0,len(credit_card_network_list)-1)]
	custom_name = "n/a"
	url = "http://localhost:5000/credit_card/details/"
	headers = {'Content-type': 'application/json'}
	data = {
		'email': username+'@gmail.com',
		'password': 'sarasa123',
		"credit_card_bank_name": credit_card_bank_name,
		"credit_last_four_numbers": credit_last_four_numbers,
		"credit_card_network_bank": credit_card_network_bank,
		"custom_name": custom_name
		} 
	r = requests.post(url = url,json=data,headers=headers) 
	# extracting response text  
	pastebin_url = r.text 
	print("The pastebin URL is:%s"%pastebin_url) 
	print ("------------------------------------------------------------------")

	if True:
		for i in range(random.randint(1,15)):
			add_fake_expenses(username,credit_card_bank_name,credit_last_four_numbers,credit_card_network_bank,custom_name)

def add_fake_expenses(username,credit_card_bank_name,credit_last_four_numbers,credit_card_network_bank,custom_name):
	product_list=["Audio Fusion","Audiovinyl","Austech","B Cool 2 School","Baby Donuts","Buddha Loops","Buddy Ebsen Salt","Buffalo Butter","Bug Eyes","Bug Pod","Bug’aBone","Bugabug","Buzz Kilt","Buzz Skill","Buzzmaker","Buzzy","Clem Clogs","Cognicode","Cola Cones","Cola Plex","COLAR","Coldshower Gearbox","Collar Magic","Collar","Combath","Combination Hand Cuffs","Combot","Comdomorts","Comnect","Compglass","Complete Meat","Complex Ports","Complimentia","Compo-bricks","ComposeTicker","ComprehendIT","CompuBooth","Computercate","Cubicide","Cubicle Machine","Cubicle Remover","Cubicoil","Cubix","Culture Squirrel","Cup of Hot Kafka","CUPID","Curb Appeal","Currency Net","Curt Ales","Cutter Claw","Cut-Throat Jeans","Cuzzles","Cycle Suave","Cyclone","Cyclovista","Cytrak","Cytrek","Cytrex","Cytrexaline","D. E. Light","D.E. Lightful","Dadbone","Daffodildo","Deal Light","Dearlescent","Deco Pube","DecodeIT","DecraPet","Dedicadence","Deep Anxietea"]
	cantidad_de_cuotas = random.choice([1,3,6,12,18])
	url = "http://localhost:5000/credit_card/expenses/"
	headers = {'Content-type': 'application/json'}
	data = {
		'email': username+'@gmail.com',
		'password': 'sarasa123',
		"credit_card_bank_name": credit_card_bank_name,
		"credit_last_four_numbers": credit_last_four_numbers,
		"credit_card_network_bank": credit_card_network_bank,
		"custom_name": custom_name,
		"amount_of_payments":cantidad_de_cuotas,
		"number_of_next_payment":random.randint(1,cantidad_de_cuotas),
		"price_of_expenditure":random.randint(6,25)*1000,
		"name_of_expenditure":random.choice(product_list),
		"currency_iso_code":"ARS",
		"continue_payment":True
		} 
	r = requests.post(url = url,json=data,headers=headers) 
	# extracting response text  
	pastebin_url = r.text 
	print("The pastebin URL is:%s"%pastebin_url) 
	print ("------------------------------------------------------------------")

def fill_database(list_of_usernames):
	for username in list_of_usernames:
		add_user(username)
		for i in range(random.randint(2,4)):
			add_fake_credit_cards(username)

list_of_usernames=["angel","bubbles","shimmer","angelic","bubbly","glimmer","baby","pink","little","butterfly","sparkly","doll","sweet","sparkles","dolly","sweetie","sprinkles","lolly","princess","fairy","honey","snowflake","pretty","sugar","cherub","lovely","blossom"]

fill_database(list_of_usernames)
