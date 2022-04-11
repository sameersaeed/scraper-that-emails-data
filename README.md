# scraper-that-emails-data
a python scraper that, using modules such as selenium, smtp, MIME and os: 
goes to a site and retrieves specific data, then takes a screenshot of that data and emails it to a recipient


config.py - info for email, login info for account being used to send it, email for who it is being sent to
    ws.py - gets stock availability of various retailers from site 'stocktrack.ca'
          - i use this to check if certain pools were in stock at walmarts in a specific location
  send.py - sends email msg of scraped data, including a screenshot 
