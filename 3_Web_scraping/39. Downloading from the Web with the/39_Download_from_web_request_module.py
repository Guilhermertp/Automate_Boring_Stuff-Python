#import the module request to download files from the web, this module needs to be installed before importaed!!!
import requests

#download the file passint he string of the url to download
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

#verifiy is the file exists use status code, by ex. 404 file not found if 200 ok
res.status_code

#check for an error downloading the file
try:
    badRes = requests.get('https://automatetheboringstuff.com/files/imaginary_file.txt')
    badRes.raise_for_status()
except:
    print('Error, imaginary_file.txt not found')

"""if the file not found is not a reason to stop the program we can wrap the raise_for_status line in a it in a try and except
statment"""

#save file to the hard drive
playFile = open('RomeoAndJuliet.txt', 'wb') #creates an empty file

for chunk in res.iter_content(100000): #iteration of one hundred thousand bytes per iteration
    playFile.write(chunk) #writes in the file RomeoAndJuliet.txt

playFile.close()

"""The Requests module is a third-party module for downloading web pages and files.
requests.get() returns a Response object.
The raise_for_status() Response method will raise an exception if the download failed.
You can save a downloaded file to your hard drive with calls to the iter_content() method."""

