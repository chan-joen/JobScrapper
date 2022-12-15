from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, request, redirect
from extractors.wwr import extract_wwr_jobs
from extractors.remoteok import extract_remoteok_jobs

app = Flask("JobScrapper")

db = {
}

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword == None or len(keyword) == 0 or keyword.startswith(' '):
    return redirect("/")
  if keyword in db : 
    jobs = db[keyword]
  else:
    remoteok = extract_remoteok_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = remoteok + wwr
    db[keyword] = jobs
  return render_template("search.html", keyword = keyword, jobs=jobs)

app.run("0.0.0.0")
