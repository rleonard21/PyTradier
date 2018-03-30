import configparser
from .exceptions import ClientException

def get_auth(location):
	config = configparser.ConfigParser()
	config.read(location)

	settings = []

	try:
		auth = config['AUTH']
		settings.append([auth['Token'], auth['AccountID'], auth['Endpoint']])

	except KeyError:
		raise ClientException('Unable to parse [AUTH] section of ini file!')

	return settings[0]
