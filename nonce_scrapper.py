import json
from typing import Iterable

from scrapy import Spider, Request


class NonceScrapper(Spider):
    name = 'nonce_scrapper'
    allowed_domains = ['blockchain.com']
    start_urls = ['https://www.blockchain.com/explorer/blocks/btc?page={}']

    def start_requests(self):
        for page in range(1, 1000 + 1):
            yield Request(self.start_urls[0].format(page))

    def parse(self, response):
        nonce_data = response.css("script#__NEXT_DATA__ ::text").get("")
        nonce_data = json.loads(nonce_data)
        blocks = nonce_data['props']['pageProps']['latestBlocks']

        for block in blocks:
            del block['coinbaseTransaction']
            del block['fees']
            del block['weight']
            del block['version']
            del block['time']
            del block['subsidy']

            yield block
