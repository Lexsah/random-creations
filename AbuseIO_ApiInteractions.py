import requests, json



# Set your API key, domain name and URL
api_key = "my-redacted-api-key"
domain = "https://my.domain.net"

headers = {
		"Content-Type": "application/json",
		"X-Requested-With": "XMLHttpRequest",
	    "X-API-TOKEN": api_key
	}



def openIncident(IP_ADDRESS, SOURCE_NAME, CLASS_NAME, TYPE_NAME):
	print("Creating Incidents...")

	# Define the data for the ticket

	api_url = domain + "/api/v1/incidents"
	data = {
	  "source":SOURCE_NAME,
	  "source_id":1,
	  "ip":IP_ADDRESS,
	  "domain":"redacted.fr",
	  "timestamp":0,
	  "class":CLASS_NAME,
	  "type":TYPE_NAME,
	  "information":'{"CVE":448, "testing":"ofTest", "testLongueurAffichage":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean lobortis nibh nec dolor euismod hendrerit. Nullam auctor facilisis leo. Praesent porttitor ipsum ut sem feugiat sollicitudin. Sed laoreet massa sit amet erat sagittis tempor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In hac habitasse platea dictumst. Morbi tortor nulla, lobortis vitae faucibus vel, cursus quis elit. Duis facilisis leo vel ligula pulvinar interdum. Duis cursus elit sit amet maximus maximus. Aenean vehicula dapibus malesuada. Etiam tempor porttitor enim, ac imperdiet ligula finibus vitae. Pellentesque tincidunt sit amet neque vel ultricies.  Sed vitae ligula tristique, vestibulum turpis vel, rutrum elit. Pellentesque nec urna mauris. Aliquam pharetra iaculis magna sed egestas. Fusce gravida id massa eu volutpat. Morbi quis lobortis sapien. Nam quis metus felis. Fusce facilisis sollicitudin nisi, at fermentum ligula tincidunt at. Proin porta dolor vitae urna vehicula fringilla.  Nunc non mattis libero. Aenean dapibus facilisis viverra. In id egestas orci. Aenean quis vulputate arcu. Aenean sed lorem viverra dolor venenatis efficitur. Nulla aliquet pretium ligula vel dapibus. Phasellus dictum tempor metus eget consectetur. Curabitur sit amet velit ut ante dictum volutpat. Aenean diam mauris, posuere ut dapibus eget, lobortis ut ipsum. Praesent commodo auctor ligula bibendum posuere. In non orci ut sapien venenatis elementum. Vestibulum finibus ipsum sed dui pellentesque, ut tempor arcu rhoncus. Proin euismod dignissim mollis. Cras varius sed dolor et mollis. Pellentesque rhoncus sapien id nunc gravida eleifend. Nullam eleifend sapien a nibh auctor, non feugiat odio facilisis. Vivamus viverra libero ut condimentum vehicula. Nunc at tincidunt arcu. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum at ipsum sed diam sodales sollicitudin. Nullam quis lorem sit amet nibh mattis dictum. Etiam pharetra elit eget sagittis ultrices. Curabitur placerat dictum felis, quis aliquet nunc tempor et. Sed facilisis, lectus fermentum scelerisque euismod, massa lectus pharetra metus, a scelerisque lacus ante id lectus. Vivamus quis fermentum enim, eu pulvinar ante. "}',
	  "remote_api_token":None,
	  "remote_api_url":None,
	  "remote_ticket_id":42,
	  "remote_ash_link":None,
	}

	
	

	# Send POST request to create ticket
	response = requests.post(api_url, json=data, headers=headers)

	# Print response status and content
	print(response.status_code)
	obj = json.loads(response.content.decode()
	print(json.dumps(obj), indent=4))
	return response.status_code, obj


def openTicket():
	print("Creating Ticket...")

	# Define the data for the ticket

	api_url = domain + "/api/v1/tickets"
	data = { 
		"ip": "127.0.0.1", 
		"class_id":"Generic message",
		"type_id": "INFO",
		"ip_contact_account_id": 1,
		"ip_contact_reference": "test_ref",
		"ip_contact_name": "test",
		"ip_contact_auto_notify": 0,
		"ip_contact_notified_count": 0,
		"domain_contact_account_id": 1,
		"domain_contact_reference": "test_reff",
		"domain_contact_name": "test_contact_name",
		"domain_contact_auto_notify": 0,
		"domain_contact_notified_count": 0,
		"status_id": "OPEN", 
		"last_notify_count": 0,
		"last_notify_timestamp": 0

	}


	# Send POST request to create ticket
	response = requests.post(api_url, json=data, headers=headers)

	# Print response status and content
	print(response.status_code)
	obj = json.loads(response.content.decode()
	print(json.dumps(obj), indent=4))
	return response.status_code, obj


def getTickets():
	print("Creating Ticket...")

	# Define the data for the ticket

	api_url = domain + "/api/v1/tickets"
	data = { 
		}
	# Send GET request to get ticket
	response = requests.get(api_url, json=data, headers=headers)

	# Print response status and content
	print(response.status_code)
	obj = json.loads(response.content.decode()
	print(json.dumps(obj), indent=4))
	return response.status_code, obj


def searchTickets(**kwargs):
	'''
	in: colomn[str]=value[*]  OR  colomn[str]=(operator[str], value[*])
	exemple: searchTickets(status_id="OPEN", id=('<=',24)) # give every open tickets with an id <= 24

	available operators : ’<’, ’>’, ’=’, ’!=’, ’<=’, ’>=’



	'''
	if len(kwargs.items()) <= 0:
		raise ValueError('searchTickets needs at least 1 argument')
	api_url = domain + "/api/v1/tickets/search"
	criterias = []

	for name, value in kwargs.items():
		if type(value) == tuple:
			criterias.append({
				"column":name,
				"operator":value[0],
				"value":value[1]
			})
		else:
			criterias.append({
      			"column":name,
      			"value":value
    		})

	data = {"criteria": criterias}

	# Send POST request to get ticket
	response = requests.post(api_url, json=data, headers=headers)

	# Print response status and content
	print(response.status_code)
	obj = json.loads(response.content.decode()
	print(json.dumps(obj), indent=4))
	return response.status_code, obj


#openTicket()
#getTickets()
#searchTickets(status_id="OPEN", id=('<=',24))

openIncident("1.1.1.1", "testting", "SPAM", "ABUSE")





