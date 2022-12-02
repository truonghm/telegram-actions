import requests
import os
from dotenv import load_dotenv
load_dotenv()

def send_msg(text):
	token = os.getenv("TELEGRAM_TOKEN")
	chat_id = os.getenv("TELEGRAM_TO")
	url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}"
	results = requests.get(url_req)
	print(results.json())



if __name__ == "__main__":
	message = """
	<b>Good Morning</b> <a href="tg://user?id=hmtrg">Truong</a>! Don't forget these following items for the day:\n
	
	- <a href="https://leetcode.com/study-plan/leetcode-75/?progress=xdaigrwd">Leedcode 75</a>
	- <a href="https://adventofcode.com/">Advent of Code 2022</a>

	"""
	send_msg(message)
