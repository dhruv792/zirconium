import html

import json
from lxml.etree import fromstring

import pymongo
from pymongo import MongoClient  
# The requests library
import requests
from bs4 import BeautifulSoup

  
class WholeFoodsScraper:
  
    API_url = 'https://www.99acres.com/do/quicksearch/getresults_ajax?new_srp=Y'
    scraped_stores = []

    def get_stores_info(self, page):
     
        # This is the only data required by the api 
        # To send back the stores info

        headers = {"Origin":"https://www.99acres.com",
            "X-DevTools-Emulate-Network-Conditions-Client-Id":"6cacbe26-d523-4463-ae3a-eaad44c9d055",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded",
            "Accept":"*/*",
            "Referer":"https://www.99acres.com/property-in-mumbai-ffid?check_cookie=1&search_location=BPHP",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"en-US,en;q=0.9",
            "Cookie":"99_FP_VISITOR_OFFSET=37; 99_suggestor=91; 99_trackIP=IN; 99NRI=1; _ss_v=RC+vBj4QL6KpuVHm; 99_defsrch=n; RES_COM=RES; src_city=0; 99_citypage=0; 99_city=; PROP_SOURCE=IP; cdClick=""; kwp_last_action_id_type=30705137%2CVSP_LOAD_B%2C546998216829374901; __atuvc=6%7C45; __atuvs=5a022795552fa969001; izDl=1; __utid=5; spd=%7B%22P%22%3A%7B%22a%22%3A%22R%22%2C%22b%22%3A%22S%22%2C%22d%22%3A%2212%22%7D%7D; res_com=RES; __utmt=1; 99zedoParameters=%7B%22city%22%3A%2212%22%2C%22locality%22%3A%225172%22%2C%22budgetBucket%22%3Anull%2C%22activity%22%3A%22SRP%22%2C%22rescom%22%3A%22RES%22%2C%22preference%22%3A%22BUY%22%2C%22nri%22%3Anull%7D; _ss_s=eyJsb2NhdGlvbiI6Ik11bWJhaSAtIE1haGFyYXNodHJhLCBJbmRpYSIsIklQIjoiMTA2LjIwOS4xMjkuMTQ2IiwiYnJvd3NlciI6IkNocm9tZSA2Mi4wLjMyMDIiLCJPUyI6Ik1hYyBPUyBYIDEwLjEyLjYiLCJyZWZlcnJlciI6IkRpcmVjdCIsInJlcGVhdCI6IlllcyJ9; newRequirementsByUser=0; JSESSIONID=84CC75D9D016EBB458AF9DEBDD76F2B8; 99_ab=2; GOOGLE_SEARCH_ID=546998216829374901; PROPLOGIN=0; LAST_LOGIN=0; DISP_NAME=0; GOOGLE_SEARCH_ID=546998216829374901; _sess_id=eIAZyI3vC9g0CEXF4vVvtP4E3BxYd9aCmt2UMeGyc0eQ97R2EYcJttOMYE9RkCweTzcsq%2B1rFV%2FD74uhx2ivkA%3D%3D; __utma=267917265.615129923.1509982170.1510084816.1510090644.8; __utmb=267917265.32.6.1510092450774; __utmc=267917265; __utmz=267917265.1509982170.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); markRequirementsWaivedOnLeave=0"
        }
        data = {
        'encrypted_input': 'UiB8IFFTIHwgUyB8IzMwIyAgfCAzMTQyMjA2MywzMzA4OTYwMSMxIyB8IDEyICM0NyN8ICB8IA==',
        'is_ajax': '1',
        'page': page,
        'src': '1',
        'is_ajax': '5',
        'static_search': '1',
        'lstAcn':'SEARCH',
        'lstAcnId': '9599864082912672'
        }
        # Making the post request
        response = requests.post(self.API_url, data=data, headers = headers)

        # The data that we are looking is in the second
        # Element of the response and has the key 'data', 
        # so that is what's returned
        return (response)


    def run(self):
        for page in range(50, 50):
            # Retrieving the data
            data = self.get_stores_info(page)
            # Parsing it
            self.parse(data)
            print('scraped the page' + str(page))


    def parse(self, response):
        client = MongoClient('52.66.174.199', 27017)
        zirconium = client.zirconium
        properties = zirconium.properties
        propertiesArray = []
        content = (response.content)
        
        soup = BeautifulSoup(content, 'lxml')
        filename = 'quotes222232.html'
        with open(filename, 'w') as f:
            f.write(str(soup))
        print("file saved")
        # for tag in soup.find_all('div',{'class':'srpttl'}):
        #     # print(tag)
        #     # break
        #     x = tag.find('span')
        #     print(x)
        #     # break
        #     y  = x.find_all('b')
        #     try:
        #         item = {
        #             'price':  y[1].string,
        #             'description': tag.a.string,
        #             'link': "https://www.99acres.com"+tag.a['href']
        #         }

        #         propertiesArray.append(item)
        #     except Exception:
        #         continue
            
        # # print((propertiesArray))
        # result = properties.insert(propertiesArray)
        # print("Result", result)

if __name__ == '__main__':
    scraper = WholeFoodsScraper()
    scraper.run()