import time
from datetime import datetime as dt

# Hosts file path
#hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_path = r"E:\Temp\hosts1"
redirect = "127.0.0.1"
website_lists = ["www.facebook.com",
                 "www.yahoo.com"
                 ]
blockFrom = 8
blockTill = 16

redirect = '127.0.0.1'
while True:
    # Determine the state of firewall
    if dt(dt.now().year, dt.now().month, dt.now().day, blockFrom) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, blockTill):        
        # Open hosts file for blocking websites
        with open(hosts_path, 'r+') as file:
            content = file.read()            
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
        file.close()
    else:
        with open(hosts_path, 'r+') as file:
            # Open hosts file to unbloxk websites
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_lists):
                    file.write(line)
            file.truncate()        
        file.close()
    time.sleep(300)