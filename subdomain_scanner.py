import requests
# the domain to scan for subdomains
domain = "google.com"


# read all subdomains
with open("subdomains.txt") as file:
  # read all content
  content = file.read()
  # split by new lines
  subdomains = content.splitlines()