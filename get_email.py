from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re
# with sync_playwright() as p:
if(True):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://clubhousedb.com/user/prophetessj")
    ua = page.query_selector("//section[@class='user-bio']/p");
    soup = BeautifulSoup(ua.inner_html(),'html.parser')

    desc = soup.get_text()
    email = match_objects = re.findall(r'\w+@\w+[\.\w+]+', desc)
    print(desc)
    print(email)
