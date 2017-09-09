import feedparser
import urllib

url = "http://www.msnbc.com/feeds/latest"

feed = feedparser.parse(url)

# print(feed)

for x in feed.entries:
    print("Story::" + x.summary + "\n\tLink::" + x.id)
    page = urllib.request.urlopen(x.id)
    string = page.read().decode("utf8")
    page.close()
    print(string)

print("close")