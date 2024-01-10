#pip install flask

from flask import Flask, jsonify, request
import time

print("File is run")

app = Flask(__name__)
website_timestamp = {}
website_viewtime = {}
previous_website = ""
# cleaning the url, so only the name remains.
def url_strip(url):
    if "www" in url:
        url = url.split('.')[1].split('.')[0]
    if "//" in url:
        url = url.split('//')[1].split('.')[0]
    return url

@app.route('/send_url', methods=['POST'])
def track_urls():
    url = request.get_data().decode()
    website = url_strip(url) # cleaning website name
    print("currently viewing: " + website)

    global website_timestamp
    global website_viewtime
    global previous_website

    if website not in website_viewtime.keys(): # checking if website has been used before
        website_viewtime[website] = 0

    # keeping track of time spent on each website by comparing the start and end times
    if previous_website != '':
        time_spent = int(time.time() - website_timestamp[previous_website])
        website_viewtime[previous_website] = website_viewtime[previous_website] + time_spent

    # setting the start time and future previous website
    website_timestamp[website] = int(time.time())
    previous_website = website
    print("Time spent on websites: ", website_viewtime)
    return jsonify({'message': 'websites tracked success'}), 200

app.run(host='0.0.0.0', port=5000)