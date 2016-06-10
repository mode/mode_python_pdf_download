import json, requests, datetime, ConfigParser, argparse
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


	if __name__ == '__main__':
	    parser = argparse.ArgumentParser()
	    parser.add_argument('-token', '--token')
	    parser.add_argument('-password', '--password')
	    args = parser.parse_args()

	    if(args.token is not None and args.password is not None):
	    	auth = (args.token, args.password)
	    else:
	    	auth = get_auth()


	mode_url = 'https://modeanalytics.com'
	#Set API URL for your report
	api_url = '/api/modeanalytics/reports/287cb906e6bd'


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


	try:

		filename = data['filename']

		href = links['download']

		href = href['href']
		
		pdf_url = mode_url + href

		pdf = get_pdf(pdf_url, auth)

		
		file = open(filename, 'w')
		file.write(pdf.content)
		file.close()

	except:
		print 'We had trouble getting your PDF.  Please make sure you have a download link at: '
		href = links['self']
		href = href['href']
		print mode_url + href
		print 'If not, you may have a download link you may have to re-export a PDF version of your report.'
	

get_mode_json()






