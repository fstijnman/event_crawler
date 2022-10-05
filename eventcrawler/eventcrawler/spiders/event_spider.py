import scrapy


class RadionSpider(scrapy.Spider):
    name = "radion"

    def start_requests(self):
        url = "https://radion.amsterdam/events"

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield from response.follow_all(
            response.xpath("//div[@class = 'col-md-10']/a/@href").getall(),
            self.parse_event,
        )

    def parse_event(self, response):
        yield {
            "event_name": response.xpath(
                '//div[@class = "col-md-12 content"]/h1/text()'
            ).getall(),
            "event_date": response.xpath('//div[@class = "date"]/text()').getall(),
            "event_time": response.xpath(
                '//div[@class = "date"]/small/text()'
            ).getall(),
            "event_description": response.xpath(
                '//div[@class = "event-description"]/p/text()'
            ).getall(),
            "event_url": response.url,
            "event_ticket_url": response.xpath(
                '//div[@class = "buy-tickets"]/a/@href'
            ).getall(),
        }


class ShelterSpider(scrapy.Spider):
    name = "shelter"

    def start_requests(self):
        url = "https://shelteramsterdam.nl/"

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield from response.follow_all(
            response.xpath("//div[@class = 'eventblok2']/a/@href").getall(),
            self.parse_event,
        )

    def parse_event(self, response):
        yield {
            "event_name": response.xpath(
                '//div[contains(@class,"artists")]/div/p/text()'
            ).getall(),
            "event_date": response.xpath(
                '//div[contains(@class,"datum")]/div/p/text()'
            ).getall(),
            "event_time": response.xpath(
                '//div[contains(@class,"datum")]/div/p/text()'
            ).getall(),
            "event_description": response.xpath(
                '//div[@class = "wpb_text_column wpb_content_element "]/div/p/span/text()'
            ).getall(),
            "event_url": response.url,
            "event_ticket_url": response.xpath(
                '//div[@class="wpb_text_column wpb_content_element  links"]/div/p/a/@href'
            ).getall(),
        }


class DokaSpider(scrapy.Spider):
    name = "doka"

    def start_requests(self):
        url = "https://www.volkshotel.nl/nl/agenda/doka/"

        yield scrapy.Request(url=url, callback=self.parse)

    def parse_event(self, response):
        yield {"event_name"}
