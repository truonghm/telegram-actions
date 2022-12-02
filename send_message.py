import requests
import os
from dotenv import load_dotenv
load_dotenv()

def send_msg(text):
	token = os.getenv("TELEGRAM_TOKEN")
	chat_id = os.getenv("TELEGRAM_TO")
	url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
	results = requests.get(url_req)
	print(results.json())



if __name__ == "__main__":
	message = """
	Good Morning! Don't forget these following items for the day:\n
	- [Leedcode 75](https://leetcode.com/study-plan/leetcode-75/?progress=xdaigrwd)\n
	- [Advent of Code 2022](https://adventofcode.com/)
	"""
	send_msg(message)
