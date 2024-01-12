urls = ["https://en.wikipedia.org/wiki/Julia_(programming_language)", 
        "https://fi.wikipedia.org/w/index.php?search=tomatoe&title=Toiminnot:Haku&profile=advanced&fulltext=1&ns0=1",
        "https://play.google.com/store/apps/details?id=org.wikipedia&hl=en_US",
        "https://medium.com/dev-genius/data-mining-with-python-8c8d9add1cf3",
        "https://www.hsl.fi/",
        "https://developer.chrome.com/docs/extensions/develop/migrate/to-service-workers#persist-states",
        "https://opas.peppi.utu.fi/fi/opintojakso/TKO_8001/92825?period=2022-2024"]

urls_cleaned = []

for url in urls:
    if url.count(".") >= 2:
        urls_cleaned.append(url.split('.')[1].split('.')[0])
    else:
        urls_cleaned.append(url.split('//')[1].split('.')[0])

print(urls_cleaned)