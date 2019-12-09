import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)
  
def extract_jobinfo(html):
  title = html.find("div", {"class": "-title"}).find("h2").find("a")["title"]
  return {"title": title}

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):    #range는 인자로 integer를 사용.
    pg = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(pg.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
      job = extract_jobinfo(result)
      jobs.append(job)
  return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs