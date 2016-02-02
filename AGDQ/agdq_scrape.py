import requests
import pandas as pd

link = "http://gamesdonequick.com/schedule"
header = {"User-Agent":"Mozilla/5.0"}

# List of data frames becomes one DataFrame because of [0]
agdq = pd.read_html(requests.get(link, headers=header).text)[0]

agdq.columns = ["StartTime", "Name", "Runners",
                         "RunTime", "Category",
                         "SetupTime", "Description"]