import os

# Send Ping to Each Url inside urls.txt file
def ping_url(url):
    response = os.system(f"ping -c 1 {url.strip()}") 
    if response == 0:
        print(f"{url.strip()} is reachable")
    else:
        print(f"{url.strip()} is not reachable")

# Read URLs from urls.txt and ping each one
with open('urls.txt', 'r') as file:
    urls = file.readlines()
    for url in urls:
        ping_url(url)
