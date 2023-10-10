import requests, json

url = "http://www.qlcoder.com/task/93/solve"
def once(n):
	if (n % 100 == 0):
		print(n)
	tel = str(n).zfill(8)
	payload = "answer=%7B%22name%22%3A%22%E6%B2%88%E6%AD%A3%E7%BF%94%22%2C%22tel%22%3A%22137" + tel + "%22%2C%22qq%22%3A%22447269857%22%2C%22marry%20him%22%3A%22yes%22%7D&_token=wVX7Fg1rtI156eFKa7J8WKSROmZOCh0BNDTZeeTr"
	headers = {
		'content-type': "application/x-www-form-urlencoded",
		'cookie': "remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6IitzSEFmYWVlbUo4SG4rSVQxSGpvNHc9PSIsInZhbHVlIjoiSHF2andYRXUxTmpjQ3pwWXdZb1wvNTlXdjRUTG5HRjlDa1M0dTdra0RFUXh1QkU3M3NrREJxSVdBSGc2WWs2RzkxTXU1eXB1ZGFFY3doT09VbU1iQzR2K1FxUE1zQkhBNVRvcUFkb0NZckNJPSIsIm1hYyI6ImJkMzhmYTk5OTdmNDBiOWJiY2UxZDhlNzI2ODk5ZWJiMzc4ZWNiZWU1NDA1Mjc1MTBjZGRiOTg2ZDljMzk4YTkifQ%3D%3D; uuid=58de07d0a2580; %E8%BF%99%E9%A2%98%E7%9A%84%E7%AD%94%E6%A1%88%E6%98%AForeo=eyJpdiI6IjE4K0xSU1lGZm1jZFpoaFFcLyswWUVBPT0iLCJ2YWx1ZSI6InNoK3ZFNGxFTDFuMGhrRmxOZFhQbVE9PSIsIm1hYyI6IjkyOGEzMWM4MTA1MTg0ZWY3MzBmMGZkYTE1YTBkMmU1YmE3NThkMGI3NmJhNGIzZTZlZDQ1MTU1NmYwMzI4ZjMifQ%3D%3D; XSRF-TOKEN=eyJpdiI6ImpKTEpqbnBSSDV4cjAzSFgyQ2xuMXc9PSIsInZhbHVlIjoiMlVSUVVFU0x1U0s2Zm9zUEZSaXhPMGJIRHl4TVVOeXY3b2s1dkltdUxRbDVJVHZBd0xNYWdjdVg4aGVVaURuU29oZnl0Zjg5RlVJN2xoUmowd2R4aHc9PSIsIm1hYyI6IjBmYzJlMzMxYjQ3OGU5ZTBhYzRlZGFjNzZmYmYyOGFiYTA0NDQyNWQ3YmFhNGM4NTljNTc4NGUxNDZjM2I2NDMifQ%3D%3D; laravel_session=eyJpdiI6ImJtd3pPMVFoRlFqOWNTVFwvTmxSWnFnPT0iLCJ2YWx1ZSI6InVabVRNdzdWUDg2a2xDRjRkNmpWcHZcL2M2WjVzTUR4VGhEeXBrWTA0Y2VrXC9hem9EZnkzdzA5aXZJeWhHaDZybFIwXC83RlFDMllJOG9FKzRKQnZlN21BPT0iLCJtYWMiOiJjNzg4NTNiM2FiNzgwNGM5MGZlOWU3YTAyNzE5OGI5MTIxODQ2MzhjNDdkZDU0MDM2ZGZjMzcyYjk5ZGY1NGIyIn0%3D",
		'cache-control': "no-cache"
	}

	response = requests.request("POST", url, data=payload, headers=headers)
	if (response.status_code != requests.codes.ok):
		print('error!', tel)
		quit(-1)
	data = response.json()
	if (data['success']):
		print('success!', tel)
		quit(0)

for x in range(1,100000000):
	once(x)