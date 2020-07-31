import requests
from bs4 import BeautifulSoup

base_URL = "https://remoteok.io/"

def extract_jobs(lang):
  jobs = []
  try:
    result = requests.get(f"{base_URL}remote-dev+{lang}-jobs")
    soup = BeautifulSoup(result.text, "html.parser")
    container = soup.find("div",{"class":"container"})
    table = container.find("table",{"id":"jobsboard"})
    tr = table.find_all("tr",{"class":"job"})
    for info in tr:
      td_date = info.find("td",{"class":"time"}).text
      if ("mo" or "yr") in td_date:
        pass
      else:
        td_info = info.find("td",{"class":"company position company_and_position"})
        link = td_info.find("a",{"itemprop":"url"})["href"]
        link = f"https://remoteok.io{link}"
        title = td_info.find("h2",{"itemprop":"title"}).text
        company = td_info.find("h3",{"itemprop":"name"}).text
        jobs_dict = {"title":title, "company":company, "link":link}
        jobs.append(jobs_dict)
    return jobs
  except:
    return None