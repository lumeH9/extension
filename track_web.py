from flask import Flask, jsonify, request
import time

app = Flask(__name__)
website_timestamp = {}
website_viewtime = {}
previous_website = ""

# cleaning the url, so only the name remains.
# needs a little tweaking, but works well on most sites
def url_strip(url):
    if url.count(".") >= 2:
        url = url.split('.')[1].split('.')[0]
    else:
        url = url.split('//')[1].split('.')[0]
    return url

# receiving url that was sent by the chrome extension
@app.route('/send_url', methods=['POST'])
def track_urls():
    data = request.get_data()
    print('\n', 'requested json data: ', data, '\n')
    url = data.decode()
    print('decoded data: ', url, '\n')
    # when creating a new tab or switching between empty ones
    if url == '"chrome://newtab/"' or url == '""':
        website = 'newtab'
    else:
        website = url_strip(url) # cleaning website name
    print('currently viewing: ' + website, '\n')

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
    print('Time spent on websites: ', website_viewtime, '\n')
    return jsonify({'message': 'websites tracked success'}), 200

app.run(host='0.0.0.0', port=5000)