# scraper-that-emails-data <br />
a python scraper that, using modules such as selenium, smtp, MIME and os: <br />
goes to a site and retrieves specific data, then takes a screenshot of that data and emails it to a recipient<br />


config.py - info for email, login info for account being used to send it, email for who it is being sent to <br />
\s\s\s\sws.py - gets stock availability of various retailers from site 'stocktrack.ca' <br />
\s\s\s\s\s\s\s\s\s\s- i use this to check if certain pools were in stock at walmarts in a specific location <br />
\s\ssend.py - sends email msg of scraped data, including a screenshot <br />
