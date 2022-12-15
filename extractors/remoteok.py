from bs4 import BeautifulSoup
import requests

def extract_remoteok_jobs(keyword):
  remoteok = f"https://remoteok.com/remote-{keyword}-jobs"
  request = requests.get(remoteok, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    results =[]
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all("tr", class_="job")
    for job in jobs:
        company = job.find('h3', itemprop = "name")
        position = job.find('h2', itemprop = "title")
        location = job.find("div", class_="location")
        anchors = job.find_all('a')
        anchor = anchors[0]
        link = (anchor['href'])
        job_data ={
          'company' : company.string.strip('\n').strip(),
          'region' : location.string.strip(),
          'position' : position.string.strip('\n'),
          'link' : f"https://remoteok.com{link}"
        }
        results.append(job_data)
    return results
      
  else:
    print("Can't get jobs.")