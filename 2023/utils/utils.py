import requests

def get_text_data(path:str, is_url:bool=True) -> str:
	"""
	Fetches the text data from the given path. If `is_url` is True, treats the path as a URL and fetches the data from there.
	Otherwise, treats the path as a local file path and reads the data from the file.

	Args:
		path (str): The path to fetch the text data from.
		is_url (bool, optional): Whether the path is a URL. Defaults to True.

	Returns:
		str: The text data fetched from the path.
	"""

	if is_url:
		try:
			response = requests.get(path)
			return response.text
		except:
			print('Error fetching data from URL')
			return ''
	else:
		with open(path, 'r') as f:
			return f.read()

#Save text data to a local file
def save_text_data(text_data:str, file_name:str) -> None:
	"""
	Saves the given text data to a file with the given file name.

	Args:
		text_data (str): The text data to be saved.
		file_name (str): The name of the file to save the text data to.
	"""
	with open(file_name, 'w') as f:
		f.write(text_data)	
