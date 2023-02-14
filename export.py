import webbrowser
import os

urls = open("export_urls.txt").readlines()

for url in urls:
    webbrowser.open(url)

os.remove("export_urls.txt")
