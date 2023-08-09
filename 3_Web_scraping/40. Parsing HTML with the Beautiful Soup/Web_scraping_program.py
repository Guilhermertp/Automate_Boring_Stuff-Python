import bs4, requests

def getEbayPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    return elems[0].text.strip()


price = getEbayPrice('https://www.ebay.com/itm/123502526300?var=&hash=item1cc152ff5c')
print('The price is ' + price)
