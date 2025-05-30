import scrapy
from scrapy.utils.response import open_in_browser

import json
import re
import numpy as np
#from seloger_scraper.items import AppartmentItem

#from scrapy_splash import SplashRequest


# &page=2      -   333
class SelogerSpider(scrapy.Spider):
    name = "seloger"
    #allowed_domains = ["seloger.com"]
    
    #["www.logic-immo.com/"]

    #start_urls = ["https://www.seloger.com/classified-search?distributionTypes=Buy,Buy_Auction&estateTypes=Apartment&locations=AD08FR31096"]
    
    #["https://www.logic-immo.com/classified-search?distributionTypes=Buy,Buy_Auction&estateTypes=House,Apartment&locations=AD08FR31096&order=DateDesc"]

    #def get_all_apartments_ids(self, placeIds, pageNumber):


    # set a valid Cookie before start

    headers = {    
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/json; charset=utf-8",
        "Origin": "https://www.seloger.com",
        "DNT": "1",
        "Sec-GPC": "1",
        "Connection": "keep-alive",
        "Cookie": "_dd_s=aid=1450fec6-24b8-4bc9-8874-90b522229b85&logs=0&expire=1748535938541",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=0",
        "TE": "trailers",
    }



    
    async def start(self):

        placeIds = ["AD08FR31096"] # ID for Paris
        totalPageAvailable = 333

        #self.get_all_apartments_ids()

        for pageNumber in range(totalPageAvailable):

            searchCriteria = {
                "criteria": {
                    "distributionTypes": [
                        "Buy"
                    ],
                    "estateTypes": [
                        "Apartment"
                    ],
                    "location": {
                        "placeIds": placeIds
                    }
                },
                "paging": {
                    "page": pageNumber + 1,
                    "size": 30,
                    "order": "Default"
                }
            }
            yield scrapy.Request("https://www.seloger.com/serp-bff/search/", method='POST', headers=SelogerSpider.headers, body=json.dumps(searchCriteria), callback=self.parseApartmentsIds)

    def parseApartmentsIds(self, response):

        apartments_ids = [dict_id["id"] for dict_id in response.json()['classifieds']]
        apartments_ids_stringified = ",".join(apartments_ids)

        yield scrapy.Request("https://www.seloger.com/classifiedList/" + apartments_ids_stringified, headers=SelogerSpider.headers, callback=self.parseApartments)



    def parseApartments(self, response):
        #print(response)
        res = response.json()

        for apartment in res:

            if(len(apartment['hardFacts']['facts']) > 3):

                if re.search(r".RDC.", apartment['hardFacts']['facts'][3]['value']):
                    yield {
                        'numberOfRooms': apartment['hardFacts']['facts'][0]['splitValue'],
                        'numberOfBedrooms': apartment['hardFacts']['facts'][1]['splitValue'],
                        'livingSpace': apartment['hardFacts']['facts'][2]['splitValue'],
                        'apartmentFloor': floorNumber.group(1),
                        'zipCode': apartment['tracking']['zip_code'],
                        'price': apartment['tracking']['price']
                        }
            
                
                elif re.search(r"(\d+)\/\d+$", apartment['hardFacts']['facts'][3]['value']):
                    floorNumber = re.search(r"(\d+)\/\d+$", apartment['hardFacts']['facts'][3]['value'])
                    yield {
                        'numberOfRooms': apartment['hardFacts']['facts'][0]['splitValue'],
                        'numberOfBedrooms': apartment['hardFacts']['facts'][1]['splitValue'],
                        'livingSpace': apartment['hardFacts']['facts'][2]['splitValue'],
                        'apartmentFloor': floorNumber.group(1),
                        'zipCode': apartment['tracking']['zip_code'],
                        'price': apartment['tracking']['price']
                        }
                    


                    
                elif re.search(r"^(\d+)", apartment['hardFacts']['facts'][3]['value']):
                    
                    floorNumber = re.search(r"^(\d+)", apartment['hardFacts']['facts'][3]['value'])
        
                        
                    yield {
                        'numberOfRooms': apartment['hardFacts']['facts'][0]['splitValue'],
                        'numberOfBedrooms': apartment['hardFacts']['facts'][1]['splitValue'],
                        'livingSpace': apartment['hardFacts']['facts'][2]['splitValue'],
                        'apartmentFloor': floorNumber.group(1),
                        'zipCode': apartment['tracking']['zip_code'],
                        'price': apartment['tracking']['price']
                        }
                    
                else:
                    print(apartment['hardFacts']['facts'][3]['value'])


                
 

    
    
    """

    def parse(self, response):

        # https://www.seloger.com/serp-bff/search/

        open_in_browser(response)
        #deny_cookies = response.css("a.uc-deny-all::attrib(href)").get()
        #print(deny_cookies)
        #yield response.follow(deny_cookies, self.parseAppartments)


    def parseAppartments(self, response):

        #appartment_item = AppartmentItem()
        data_to_extract = response.css("div.css-79elbk a::attrib(title)").re(r"Appartement à vendre - Paris ([0-9]{2})ème - ([\d\s]+) € - (\d+) pièces, (\d) chambres, (\d+) m², Étage ([0-9]{1,2})/([0-9]{1,2})")
        self.logger.info(data_to_extract)
        #yield data_to_extract
        #regex to match: 

        
        # open_in_browser(response)
        # print(response.css("h1.css-1urtcje::text").get())
        # print("it works")
        
        #print(urls_to_scrap)
        #self.logger.info("Text", urls_to_scrap)

    """