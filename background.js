// using chrome api .tabs to create an extension and listen to changes on the browser

// creating a listener that reacts when a new tab is opened, connecting to my local server and sending it the website url
chrome.tabs.onActivated.addListener(function (new_tab) {
    chrome.tabs.get(new_tab.tabId, function (tab) {

      console.log('new tab was opened');
            
      // API endpoint where your current url is sent and processed
      const apiUrl = 'http://192.168.1.87:5000/send_url';

      // POST request using Fetch API
      fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(tab.url)
      })
    });
});
// sending my url when the tab has already been created and the user switches back to it
// otherwise same function as above
chrome.tabs.onUpdated.addListener((tabId, change, tab) => {
    
    if (tab.active && change.url) {

         const apiUrl = 'http://192.168.1.87:5000/send_url';

         fetch(apiUrl, {
           method: 'POST',
           headers: {
             'Content-Type': 'application/json',
           },
           body: JSON.stringify(tab.url)
         })
    }
});
