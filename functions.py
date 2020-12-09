import requests as r
import json

def get_access_token(client_id, client_secret, username, password):

	url = "https://cloudsso.cisco.com/as/token.oauth2"

	payload = "client_id="+client_id+"&client_secret="+client_secret+ \
		"&grant_type=password&username=" +username+"&password="+password

	headers = {
  		"Content-Type": "application/x-www-form-urlencoded"
	}

	try:
		response = r.request("post", url, headers=headers, data=payload)

		if response.status_code == 200:
			response_dict = json.loads(response.text)
			access_token = response_dict["access_token"]
			return(access_token)
		else:
			return("Response Code: "+response.status_code+" - Token generation failed")
	except:
		raise



def get_auth_file(smartAccountDomain, virtualAccountName, access_token, hostname, serialNumber, reservationCode, tagList):

	url = "https://swapi.cisco.com/services/api/smart-accounts-and-licensing/v1/accounts/"+smartAccountDomain+ \
	      "/virtual-accounts/"+virtualAccountName+"/reserve-licenses"

	payload = {
		"reservationRequests":[
			{
			"reservationCode": reservationCode,
			"reservationType": "SPECIFIC",
			"licenses":[]
			}
		]
		}

	for entitlementTag in tagList:
		license = {
			"entitlementTag": entitlementTag,
			"quantity": 1,
			"precedence": "LONGEST_TERM_FIRST"
			}
		payload["reservationRequests"][0]["licenses"].append(license)

	payload = json.dumps(payload)

	headers = {
		"Content-Type": "application/json",
		"Authorization": "Bearer "+access_token
	}

	try:
		response = r.request("post", url, headers=headers, data=payload)

		if response.status_code == 200:
			response_dict = json.loads(response.text)
			auth_code = response_dict["authorizationCodes"][0]["authorizationCode"]

			filename = hostname+"_AuthorizationCode_SN_"+serialNumber+".txt"

			with open(filename, "w+") as file:
				file.write(auth_code)

			return("Authorization file generated: "+filename)
		else:
			return("Authorization file generation failed: "+str(response.status_code))
	except:
		raise