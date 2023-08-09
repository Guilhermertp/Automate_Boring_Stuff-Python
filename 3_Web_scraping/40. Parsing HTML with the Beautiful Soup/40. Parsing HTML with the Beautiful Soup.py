#make sure the module beautifull soup is intalled so the import don't give an error
import bs4

import requests

#downloads the html page
res = requests.get('https://www.ebay.com/itm/123502526300?var=&hash=item1cc152ff5c')

#check for errors when downloading the webpage
#res.raise_for_status()

#call the BeatifullSoup module and pass the hmtl that was downloaded
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#find elements in the html, in this case the price of the Samsung Galaxy S8 Active 
#to get only the price
print(elems[0].text.strip())
