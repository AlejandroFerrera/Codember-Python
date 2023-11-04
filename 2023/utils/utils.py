import requests

def get_text_data(url):
	"""
	Fetches the text data from the given URL.

	Args:
		url (str): The URL to fetch the text data from.

	Returns:
		str: The text data fetched from the URL.
	"""
	response = requests.get(url)
	return response.text

#Save text data to a local file
def save_text_data(text_data, file_name):
	"""
	Saves the given text data to a file with the given file name.

	Args:
		text_data (str): The text data to be saved.
		file_name (str): The name of the file to save the text data to.
	"""
	with open(file_name, 'w') as f:
		f.write(text_data)
	
