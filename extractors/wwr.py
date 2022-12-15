import requests 
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
  response = requests.get(url)
  if response.status_code == 200:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']
        company, kind, region = anchor.find_all('span', class_="company")
        title = anchor.find('span', class_='title')
        job_data = {
          'company' : company.string,
          'region' : region.string,
          'position' : title.string,
          'link' : f"https://weworkremotely.com{link}"
        }
        results.append(job_data)
    return results
  else: 
    print("Can't get jobs.")