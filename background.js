// using chrome api .tabs to create an extension and listen to changes on the browser

// creating a listener that reacts when a new tab is opened, connecting to my local server and sending it the website url
chrome.tabs.onActivated.addListener(function (new_tab) {
    chrome.tabs.get(new_tab.tabId, function (tab) {

        var request = new XMLHttpRequest();
        
        request.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
            }
        };
        request.open("POST", "http://192.168.1.87:5000/send_url");
        request.send(tab.url);
    });
});
// sending my url when the tab has already been created and the user switches back to it
chrome.tabs.onUpdated.addListener((tabId, change, tab) => {
    
    if (tab.active && change.url) {
        var request = new XMLHttpRequest();

        request.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
            }
        };
        request.open("POST", "http://192.168.1.87:5000/send_url");
        request.send(change.url);
    }
});
