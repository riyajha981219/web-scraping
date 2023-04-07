# necessary libraries
import requests
from bs4 import BeautifulSoup

#library for writing into a csv file
from csv import writer  

#the url to scrape
url = "https://delhi-ncr.mallsmarket.com/brands/decathlon"

#get html page
r = requests.get(url)

#get html content
htmlContent = r.content

#parse the html content
soup = BeautifulSoup(htmlContent, "html.parser")


#create a csv file and open as f
with open("stores.csv","w",encoding="utf8",newline="") as f:
  #writes into f
  thewriter = writer(f)
  
  #write column names
  header = ["Location","Place"]
  thewriter.writerow(header)
  
  #choose the content you need
  tbody=soup.find_all("tbody")
  for item in tbody:
    for loc in item.find_all("span",class_="views-field-field-location"):
      location = loc.get_text()
      for final in item.find_all("div", class_= "views-field-title"):
        if "Info" not in final.get_text():
          if "Decathlon" in final.get_text():
            text = final.get_text().replace("Decathlon","")
            if location in final.get_text(): 
              ftext = text.replace(location,"")
              info = [ftext,location] 
              thewriter.writerow(info)
  
