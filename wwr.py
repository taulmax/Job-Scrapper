import requests
from bs4 import BeautifulSoup

base_URL = "https://weworkremotely.com/remote-jobs/search?term="

def get_jobs_info(html):
  try:
    title = html.find("span",{"class":"title"}).text
    company = html.find("span",{"class":"company"}).text
    link = html.find("a", recursive=False)["href"]
    link = f"https://weworkremotely.com{link}"
    if title and company and link:
      return {"title":title, "company":company, "link":link}
  except:
    pass



def extract_jobs(lang):
  jobs = []
  try:
    result = requests.get(f"{base_URL}{lang}")
    soup = BeautifulSoup(result.text, "html.parser")
    jobs_container = soup.find("div",{"class":"jobs-container"})
    jobs_sections = jobs_container.find_all("section",{"class":"jobs"})
    for section in jobs_sections:
      job_ul = section.find("ul")
      job_li = job_ul.find_all("li")
      for info in job_li:
        job = get_jobs_info(info)
        if job:
          jobs.append(job) 
        else:
          pass
    return jobs
  except:
    return None