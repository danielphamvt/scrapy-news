# -*- coding: utf-8 -*-
import scrapy


class VnExpress(scrapy.Spider):
    name = 'vnexpress'
    start_urls = [
        'https://vnexpress.net/kinh-doanh',
        'https://vnexpress.net/the-thao'
    ]

    def parse(self, response, nb_page_limit=35):
        root_path = "//div[@class='width_common list-news-subfolder has-border-right']/article | " \
                    "//div[@class='item-news item-news-common']/article"
        count = 0
        for quote in response.xpath(root_path):
            vnexpress_url = quote.xpath('.//h2[@class="title-news"]/a/@href | .//h3[@class="title-news"]/a/@href').extract_first()
            title = quote.xpath('.//h2[@class="title-news"]/a/text() | .//h3[@class="title-news"]/a/text()').extract_first()
            count += 1
            if vnexpress_url is None:
                continue
            yield {
                'text': title,
                'url': vnexpress_url,
            }
        next_page_url = response.xpath("//a[contains(@class,'btn-page next-page')]/@href").extract_first()
        pages = ['/kinh-doanh/p'+str(i) for i in range(2, nb_page_limit+1)]
        if next_page_url is not None and next_page_url in pages:
            yield scrapy.Request(response.urljoin(next_page_url))

