from lxml import html
import requests

page = requests.get('http://www.ego4u.com/en/cram-up/vocabulary/numbers/generator?param=123456789')
tree = html.fromstring(page.text)
