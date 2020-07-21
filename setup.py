page_token = str(input("Please input your Facebook Graph ID token ")) + "\n"
apify_link = str(input("Please input the URL for the JSON file of parsed info from Apify  ")) + "\n"
facebook_ID = str(input("Please input the ID for the page you want to post to  ")) + "\n"
with open("setup.txt", "w") as file:
  file.write(page_token + apify_link + facebook_ID)