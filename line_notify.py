import requests

def line_notify(message, token):
	url = "https://notify-api.line.me/api/notify"
	headers = {
		"Authorization": "Bearer " + token
	}
	payload = {"message": str(message)}
	response = requests.post(url, headers = headers, params = payload)
	return response.status_code