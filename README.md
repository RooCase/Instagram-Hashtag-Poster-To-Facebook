# Instagram-Hashtag-Poster-To-Facebook

This project allows you to share all posts using a specific hashtag to a Facebook business page using an Apify script and Facebook's Graph API.

# Requirements

  - A Facebook Business Page (Personal Profile won't work.)
  - [This Apify actor](https://apify.com/jaroslavhejlek/instagram-scraper)
  - Access to the Facebook Graph API, connected to the Facebook Page.
    - The Graph API token expires every 30 days, unless you manually extend the expiry date (the absolute maximum is 90 days, I believe.)
    - You'll need these permissions on your API Key:
        - pages_show_list
        - publish_to_groups
        - pages_read_engagement
        - pages_read_user_content
        - pages_manage_posts
        - public_profile
 - To run these python scripts, you'll need to install these packages:
    - urllib
    - json
    - facebook
    - requests

