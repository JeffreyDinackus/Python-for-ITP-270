import whois
from domain_validator import is_registered


domain_name = "google.com"
if is_registered(domain_name):
  whois_info = whois.whois(domain_name)
  #print(whois_info)
  # print the registrar
  print("Domain registrar:", whois_info.registrar)
  # print the WHOIS server
  print("WHOIS server:", whois_info.whois_server)
  # get the creation time
  print("Domain creation date:", whois_info.creation_date)
  # get expiration date
  print("Expiration date:", whois_info.expiration_date)
  print("Name Servers: ", whois_info.name_servers)
  # print all other info
  print(whois_info)



