import requests
import os
from dotenv import load_dotenv
load_dotenv()

def send_msg(text):
	token = os.getenv("TELEGRAM_TOKEN")
	chat_id = os.getenv("TELEGRAM_TO")
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
	results = requests.get(url_req)
	print(results.json())



if __name__ == "__main__":
	send_msg("Hello there!")