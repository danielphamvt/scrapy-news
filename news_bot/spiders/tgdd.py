# -*- coding: utf-8 -*-
import scrapy


class SpiderTGDD(scrapy.Spider):
    name = 'thegioididong'
    start_urls = [
        'https://www.thegioididong.com/dtdd/samsung-galaxy-a21s/danh-gia',
    ]
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'data/tgdd.json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEED_EXPORT_INDENT': 4,
    }

    def parse(self, response):
        for comment in response.xpath('//div[@class="rc"]'):
            rating = comment.xpath('.//p/span').extract_first()
            if rating is None:
                rating = []
            if "iconcom-txtstar" in rating:
                ratings = rating.split('</i>')
                star = 0
                for i, value in enumerate(ratings):
                    if "iconcom-txtstar" in value:
                        star += 1
                rated = star
                yield {
                    'text': comment.xpath('.//p/i/text()').extract_first(),
                    'rating': rated,
                    'date': comment.xpath('//a[@class="cmtd"]/text()').extract_first(),
                    'url': response.urljoin('')
                }

        # for url in start_urls:
        #     yield scrapy.Request(response.urljoin(url))
        next_page_url = response.xpath("//div[@class='pagcomment']/span[@class='active']/text()").extract_first()
        if next_page_url is not None:
            next_page_url = 'https://www.thegioididong.com/dtdd/samsung-galaxy-a51/danh-gia'\
                            + '?p='+str(1+int(next_page_url))
            yield scrapy.Request(next_page_url)

