import requests
from bs4 import BeautifulSoup

base_URL = "https://stackoverflow.com/jobs?r=true"

def get_jobs_info(html):
  try:
    title = html.find("div",{"class":"grid--cell fl1"}).find("h2").find("a")["title"]
  except:
    print("There is no title there.")
  try:
    company = html.find("div",{"class":"grid--cell fl1"}).find("h3").find("span")
    company = company.text.strip()
  except:
    print("There is no information there.")
  job_id = html["data-jobid"]
  link = f"https://stackoverflow.com/jobs/{job_id}"
  if title and company and link:
    return {"title":title, "company":company, "link":link}
  else:
    pass

def extract_jobs(lang):
  jobs = []
  try:
    result = requests.get(f"{base_URL}&q={lang}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div",{"class":"-job"})
    for result in results:
      job = get_jobs_info(result)
      jobs.append(job)
    return jobs
  except:
    return None
