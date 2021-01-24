from functions import get_access_token, get_auth_file
from datetime import datetime
import json
import os

with open("config.json") as config_json:
	config_dict = json.load(config_json)

client_id = config_dict["client_id"]
client_secret = config_dict["client_secret"]
username = config_dict["username"]
password = config_dict["password"]
smartAccountDomain = config_dict["smartAccountDomain"]
virtualAccountName = config_dict["virtualAccountName"]

with open("hosts.json") as hosts_json:
	host_dict = json.load(hosts_json)

access_token = get_access_token(client_id, client_secret, username, password)

filedir = "AuthFiles_"+datetime.today().strftime('%Y-%m-%d')

if not os.path.isdir(filedir):
	os.mkdir(filedir)

for serialNumber in host_dict.keys():
	hostname = host_dict[serialNumber][0]
	reservationCode = host_dict[serialNumber][1]
	tagList = host_dict[serialNumber][2]

	print("Processing "+hostname+" - SN:"+serialNumber)

	output = get_auth_file(smartAccountDomain, virtualAccountName, access_token, hostname, serialNumber, reservationCode, tagList, filedir)

	print(output)