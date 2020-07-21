from urllib.request import urlopen
import json 
import facebook
import requests

with open('setup.txt', 'r') as file: ## Setup  access tokens
  contents = file.readlines()
  page_access_token = contents[0].replace("\n", "")
  url = urlopen(contents[1]).replace("\n", "") ## Gets the JSON file of parsed info from Apify
  facebook_page_id = contents[2].replace("\n", "") ## ID for the Facebook Page we are uploading to
url_additions = []

with open('URLfile.txt', 'r') as file: ## opens a list of alrady-posted images to prevent them from being posted again
    contents = file.readlines()

data = json.load(url) 
i = 0
while i < len(data) - 1:
  url = data[i]['url'] ##Extracting the data we need
  imageurl = data[i]['imageUrl']
  message =  data[i]['firstComment']
  ownerUsername= data[i]['ownerUsername']
  i = i + 1
  if url not in str(contents): ##checks to see if the URL has been posted before.
    img_data = requests.get(imageurl).content ## Gets image from Instagram
    with open(('image.jpg'), 'wb') as handler: ##Stores it
      handler.write(img_data)
    graph = facebook.GraphAPI(page_access_token)
    imageID = graph.put_photo(image=open('image.jpg', 'rb'), ## sends image to Facebook, returns ID
      album_path="/me/photos",
      message='Repost from @' + ownerUsername + ": \n " + message + "\n \n View the original post here: " + url)
    print(imageID)
    url_additions.append(url)
    print(url_additions)
  else:
      continue

with open("URLfile.txt", "a") as file: ## adds new URL links to file of already-posted links
  for x in url_additions:
    print(x)
    file.write(str(x) + "\n") 