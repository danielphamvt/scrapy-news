# -*- coding: utf-8 -*-
import scrapy

urls = []


class VnExpress(scrapy.Spider):
    name = 'vnexpress'

    categories = [
        'kinh-doanh',
        'doi-song',
        # 'the-thao'
        # "du-lich",
        # 'oto-xe-may',
        # 'giao-duc',
        'suc-khoe',
        # 'tam-su',
        # 'phap-luat',
        # 'khoa-hoc'
        # 'tuyen-dau-chong-dich'
    ]
    start_urls = ['https://vnexpress.net/' + category for category in categories]

    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'data/vnexpress.json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'FEED_EXPORT_INDENT': 4,
    }

    def parse(self, response, nb_page_limit=30):
        category = response.urljoin('').split('/')[3]
        for post in response.xpath("//article"):

            vnexpress_url = post.xpath('div/a/@href').extract_first()
            title = post.xpath('div/a/@title').extract_first()
            text = post.xpath('p/a/text()').extract_first()
            if vnexpress_url is None:
                continue
            yield {
                'title': title,
                'text': text,
                'url': vnexpress_url,
                'category': category
            }

        next_page_url = response.xpath("//a[contains(@class,'btn-page next-page')]/@href").extract_first()
        pages = [f'/{category}/p'+str(i) for i in range(2, nb_page_limit+1)]
        if next_page_url is not None and next_page_url in pages:
            yield scrapy.Request(response.urljoin(next_page_url))

