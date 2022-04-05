import scrapy
from urllib import response


class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    allowed_domains = ['browse.gmarket.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&s=8']
    start_urls = ['https://browse.gmarket.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&s=8']

    def parse(self, response):
        print(response)

        for i in range(1,101):

            URL = response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]/div[1]/div[2]/div[1]/div[2]/span/a')
            div = response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]')

            if (URL != []):
                href = div.xpath('./div[1]/div[2]/div[1]/div[2]/span/a/@href')
                url = response.urljoin(href[0].extract())
    

            if(URL == []):
                href = div.xpath('./div[1]/div[2]/div[1]/div[1]/span/a/@href') 
                url = response.urljoin(href[0].extract())
            