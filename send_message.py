import requests
import os
from dotenv import load_dotenv
load_dotenv()

def send_msg(text):
	token = os.getenv("TELEGRAM_TOKEN")
	chat_id = os.getenv("TELEGRAM_TO")
	parameters = {
		'chat_id':chat_id,
		'disable_web_page_preview':True,
		'parse_mode':'HTML',
		'text':text,
	}
	base_url = f"https://api.telegram.org/bot{token}/sendMessage?"
	full_url = base_url + "&".join([f"{k}={v}" for k, v in parameters.items()]) 
	results = requests.get(full_url)
	print(results.json())



if __name__ == "__main__":
	message = """
	<b>Good Morning</b> <a href="tg://user?id=hmtrg">Truong</a>! Don't forget these following items for the day:

	- <a href="https://leetcode.com/study-plan/leetcode-75/?progress=xdaigrwd">Leedcode 75</a>
	- <a href="https://adventofcode.com/">Advent of Code 2022</a>

	For news feeds:
	- <a href="https://news.ycombinator.com/news">HackerNews</a>
	- <a href="https://sports.yahoo.com/nba/scoreboard/">Today's NBA Games </a>
	"""
	send_msg(message)
