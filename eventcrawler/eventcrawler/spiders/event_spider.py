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

    def parse(self, response):
        yield from response.follow_all(
            response.xpath("//a[contains(@href, 'doka')]/@href").getall(),
            self.parse_event,
        )

    def parse_event(self, response):
        yield {
            "event_name": response.xpath(
                "//div[contains(@class, 'meta-container')]/h1/text()"
            ).getall(),
            "event_date": response.xpath(
                "//div[contains(@class, 'sidebar-block agenda-sidebar__information')]/div/table/tbody/tr/td/text()"
            ).getall(),
            "event_time": response.xpath(
                "//div[contains(@class, 'sidebar-block agenda-sidebar__information')]/div/table/tbody/tr/td/text()"
            ).getall(),
            "event_description": response.xpath(
                "//article[contains(@class, 'post flowing-text')]/div[contains(@class, 'excerpt')]/p/text()"
            ).getall(),
            "event_url": response.url,
            "event_ticket_url": response.xpath(
                "//div[contains(@class, 'sidebar-block buy-attend__wrapper')]/a/@href"
            ).get(),
        }


class Skatecafespider(scrapy.Spider):
    name = "skatecafe"

    def start_requests(self):
        url = "https://skatecafe.weticket.com/"

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield from response.follow_all(
            response.xpath(
                "//a[contains(@class, 'order-process-btn mt-auto')]/@href"
            ).getall(),
            self.parse_event,
        )

    def parse_event(self, response):
        yield {
            "event_name": response.xpath(
                "//div[contains(@class, 'col-12 brandcolor')]/h2/text()"
            ).getall(),
            "event_description": response.xpath(
                "//div[contains(@class, 'col-12 secondary-text-color')]/text()"
            ).getall(),
            "event_url": "https://skatecafe.weticket.com/" + response.url,
            "event_ticket_url": response.xpath(
                "//a[contains(@class, 'btn mgc-btns-fr-ppp brandbutton buttonTextColor w-100')]/@href"
            ).get(),
        }


class Clubatelierspider(scrapy.Spider):
    name = "clubatelier"

    def start_requests(self):
        url = "https://www.club-atelier.nl/agenda/"

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            # "event_names"
        }
