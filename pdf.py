import json, requests, datetime, ConfigParser, urllib2
from requests.auth import HTTPBasicAuth



def get_auth():

	#Set location of python.properties file
	file = 'python.properties'
	config = ConfigParser.RawConfigParser()
	config.read(file)
	token = config.get('ModeSection', 'token')
	password = config.get('ModeSection', 'password')
	auth = (token, password)
	return auth

def get_response_json(url, auth, isAuthNeeded):
	if(isAuthNeeded):
		response = requests.get(url, auth=auth)
	else:
		response = requests.get(url)
	return response.json()

def get_pdf(url, auth):
	response = requests.get(url, auth=auth, stream=True)
	return response

def get_mode_json():

	mode_url = 'https://modeanalytics.com'
	#Set API URL for your report
	api_url = '/api/{{organization_username}}/reports/{{report_token}}'

	auth = get_auth()

	url = mode_url + api_url

	data = get_response_json(url, auth, True)

	links = data['_links']
	last_run = links['last_successful_run']
	run_url = last_run['href']

	
	url = mode_url + run_url 
	data = get_response_json(url, auth, True)
	links = data['_links']
	pdf_export = links['pdf_export']
	href = pdf_export['href']
	pdf_url = mode_url + href

	data = get_response_json(pdf_url, auth, True)

	links = data['_links']

	href = links['download']

	href = href['href']
	
	pdf_url = mode_url + href
	pdf = get_pdf(pdf_url, auth)

	print pdf

	
	file = open("document.pdf", 'w')
	file.write(pdf.content)
	file.close()

	

get_mode_json()






