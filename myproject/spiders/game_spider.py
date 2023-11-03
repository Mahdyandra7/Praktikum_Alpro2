import scrapy


class GameSpiderSpider(scrapy.Spider):
    name = "game_spider"
    allowed_domains = ["bit.ly"]
    start_urls = ["https://bit.ly/scrapingtry"]

    def parse(self, response):
        # Use an XPath selector to find elements with the data-telemetry-meta attribute
        product_tiles = response.xpath('//a[@data-telemetry-meta]')

        for product_tile in product_tiles:
            data_telemetry_meta = product_tile.xpath('@data-telemetry-meta').get()
            self.log(data_telemetry_meta)  # You can log the data or process it further

            # You can parse the data as JSON to extract specific fields
            import json
            data_telemetry_meta_dict = json.loads(data_telemetry_meta)
            product_name = data_telemetry_meta_dict['name']
            product_price = data_telemetry_meta_dict['price']

            # Process or store the extracted data as needed
            yield {
                'product_name': product_name,
                'product_price': product_price,
            }
