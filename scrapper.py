from so import extract_jobs as extract_so_jobs
from wwr import extract_jobs as extract_wwr_jobs
from remote import extract_jobs as extract_remote_jobs

def get_jobs(lang):
  if extract_so_jobs(lang) and extract_wwr_jobs(lang) and extract_remote_jobs(lang):
    jobs = extract_so_jobs(lang) + extract_wwr_jobs(lang) + extract_remote_jobs(lang)
    return jobs
  else:
    return None