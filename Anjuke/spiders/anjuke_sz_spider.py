import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from Anjuke.items import AnjukeSZItem

class AnjukeSpider(scrapy.spiders.CrawlSpider):
    name = 'anjuke_sz'

    allow_domains = ["anjuke.com"]

    start_urls = [
        'https://sz.fang.anjuke.com/loupan/all/p1/',
    ]

    rules = [
        Rule(LinkExtractor(allow=("https://sz\.fang\.anjuke\.com/loupan/all/p\d{1,}"))),
        Rule(LinkExtractor(allow=("https://sz\.fang\.anjuke\.com/loupan/\d{1,}")), follow=False, callback='parse_item')
    ]

    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False

    def get_sellout_item(self,response):
        loupan_nodes = {}
        loupan_nodes['loupan_name_nodes'] = response.xpath('//*[@id="j-triggerlayer"]/text()')
        loupan_nodes['loupan_status_nodes'] = response.xpath('/html/body/div[1]/div[3]/div/div[2]/i/text()')
        loupan_nodes['loupan_price_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/span/text()')
        if loupan_nodes['loupan_price_nodes']:
            if self.is_number(loupan_nodes['loupan_price_nodes'].extract()[0].strip()):
                loupan_nodes['loupan_discount_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/text()')
                loupan_nodes['loupan_layout_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[3]/div/text()')
                loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[4]/span/text()')
                loupan_nodes['loupan_opening_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[3]/p[1]/span/text()')
                loupan_nodes['loupan_transfer_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[3]/p[2]/span/text()')
                loupan_nodes['loupan_type_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[1]/span/text()')
                loupan_nodes['loupan_age_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[2]/span/text()')
            else:
                loupan_nodes['loupan_price_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/p/em/text()')
                loupan_nodes['loupan_discount_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/text()')
                loupan_nodes['loupan_layout_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[3]/div/text()')
                loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/span/text()')
                loupan_nodes['loupan_opening_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[3]/p[1]/span/text()')
                loupan_nodes['loupan_transfer_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[3]/p[2]/span/text()')
                loupan_nodes['loupan_type_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[3]/div[1]/ul[1]/li/span/text()')
                loupan_nodes['loupan_age_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[2]/span/text()')
        else:
            loupan_nodes['loupan_price_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/p/em/text()')
            if loupan_nodes['loupan_price_nodes']:
                loupan_nodes['loupan_discount_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/text()')
                loupan_nodes['loupan_layout_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/div/text()')
                loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[3]/span/text()')
                loupan_nodes['loupan_opening_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[3]/p[1]/span/text()')
                loupan_nodes['loupan_transfer_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[3]/p[2]/span/text()')
                loupan_nodes['loupan_type_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[3]/div[1]/ul[1]/li/span/text()')
                loupan_nodes['loupan_age_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[2]/span/text()')
            else:
                loupan_nodes['loupan_price_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[1]/p/em/text()')
                if loupan_nodes['loupan_price_nodes']:
                    loupan_nodes['loupan_discount_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/text()')
                    loupan_nodes['loupan_layout_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[2]/div/text()')
                    loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[3]/span/text()')
                    loupan_nodes['loupan_opening_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[1]/span/text()')
                    loupan_nodes['loupan_transfer_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[2]/span/text()')
                    loupan_nodes['loupan_type_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[3]/div[1]/ul[1]/li/span/text()')
                    loupan_nodes['loupan_age_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[2]/span/text()')
                else:
                    loupan_nodes['loupan_price_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[2]/span/text()')
                    loupan_nodes['loupan_discount_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/text()')
                    loupan_nodes['loupan_layout_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[3]/div/text()')
                    loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[4]/span/text()')
                    loupan_nodes['loupan_opening_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[1]/span/text()')
                    loupan_nodes['loupan_transfer_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[2]/span/text()')
                    loupan_nodes['loupan_type_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[3]/div[1]/ul[1]/li/span/text()')
                    loupan_nodes['loupan_age_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[2]/span/text()')

        if not loupan_nodes['loupan_location_nodes']:
            loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[3]/span/text()')
        loupan_item = self.struct_loupan_item(loupan_nodes)
        return loupan_item


    def get_sellwait_item(self,response):
        loupan_nodes = {}
        loupan_nodes['loupan_name_nodes'] = response.xpath('//*[@id="j-triggerlayer"]/text()')
        loupan_nodes['loupan_status_nodes'] = response.xpath('/html/body/div[1]/div[3]/div/div[2]/i/text()')
        loupan_nodes['loupan_price_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/span/text()')
        if loupan_nodes['loupan_price_nodes']:
            loupan_nodes['loupan_discount_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/text()')
            loupan_nodes['loupan_layout_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[3]/div/text()')
            loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[4]/span/text()')
            loupan_nodes['loupan_opening_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[1]/text()')
            loupan_nodes['loupan_transfer_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[2]/text()')
            loupan_nodes['loupan_type_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[1]/span/text()')
            loupan_nodes['loupan_age_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[2]/span/text()')
        else:
            loupan_nodes['loupan_price_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[2]/span/text()')
            if loupan_nodes['loupan_price_nodes']:
                loupan_nodes['loupan_discount_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/text()')
                loupan_nodes['loupan_layout_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[3]/div/text()')
                loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[4]/span/text()')
                loupan_nodes['loupan_opening_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[5]/p[1]/text()')
                loupan_nodes['loupan_transfer_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[5]/p[2]/text()')
                loupan_nodes['loupan_type_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[1]/span/text()')
                loupan_nodes['loupan_age_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[2]/span/text()')
            else:
                loupan_nodes['loupan_price_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/p/em/text()')
                loupan_nodes['loupan_discount_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/text()')
                loupan_nodes['loupan_layout_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/div/text()')
                loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[3]/span/text()')
                loupan_nodes['loupan_opening_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[1]/text()')
                loupan_nodes['loupan_transfer_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[2]/text()')
                loupan_nodes['loupan_type_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li/span/text()')
                loupan_nodes['loupan_age_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[2]/span/text()')

        if not loupan_nodes['loupan_location_nodes']:
            loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[3]/span/text()')

        loupan_item = self.struct_loupan_item(loupan_nodes)
        return loupan_item


    def get_common_item(self,response):
        loupan_nodes = {}
        loupan_nodes['loupan_name_nodes'] = response.xpath('//*[@id="j-triggerlayer"]/text()')
        loupan_nodes['loupan_status_nodes'] = response.xpath('/html/body/div[1]/div[3]/div/div[2]/i/text()')
        loupan_nodes['loupan_price_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/p/em/text()')
        if loupan_nodes['loupan_price_nodes']:
            loupan_nodes['loupan_discount_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/text()')
            loupan_nodes['loupan_layout_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[3]/div/text()')
            loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[4]/span/text()')
            loupan_nodes['loupan_opening_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[1]/text()')
            loupan_nodes['loupan_transfer_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[2]/text()')
            loupan_nodes['loupan_type_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[1]/span/text()')
            loupan_nodes['loupan_age_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[2]/span/text()')
        else:
            loupan_nodes['loupan_price_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[1]/p/em/text()')
            if loupan_nodes['loupan_price_nodes']:
                loupan_nodes['loupan_discount_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[2]/a[1]/text()')
                loupan_nodes['loupan_layout_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[3]/div/text()')
                loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/dl/dd[4]/span/text()')
                loupan_nodes['loupan_opening_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[5]/p[1]/text()')
                loupan_nodes['loupan_transfer_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[5]/p[2]/text()')
                loupan_nodes['loupan_type_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[1]/span/text()')
                loupan_nodes['loupan_age_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[2]/span/text()')
            else:
                loupan_nodes['loupan_price_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/span/text()')
                loupan_nodes['loupan_discount_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[3]/text()')
                loupan_nodes['loupan_layout_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[4]/div/text()')
                loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[5]/span/text()')
                loupan_nodes['loupan_opening_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[1]/span/text()')
                loupan_nodes['loupan_transfer_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[2]/span/text()')
                loupan_nodes['loupan_type_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[1]/span/text()')
                loupan_nodes['loupan_age_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div/ul[1]/li[2]/span/text()')

        if not loupan_nodes['loupan_location_nodes']:
            loupan_nodes['loupan_location_nodes'] = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/dl/dd[3]/span/text()')

        loupan_item = self.struct_loupan_item(loupan_nodes)
        return loupan_item


    def struct_loupan_item(self,loupan_nodes):
        loupan_item = AnjukeSZItem()
        if loupan_nodes['loupan_name_nodes']:
            loupan_item['loupan_name'] = loupan_nodes['loupan_name_nodes'].extract()[0].strip()
        if loupan_nodes['loupan_status_nodes']:
            loupan_item['loupan_status'] = loupan_nodes['loupan_status_nodes'].extract()[0].strip()
        else:
            loupan_item['loupan_status'] = ''
        if loupan_nodes['loupan_price_nodes']:
            loupan_item['loupan_price'] = loupan_nodes['loupan_price_nodes'].extract()[0].strip()
        else:
            loupan_item['loupan_price'] = ''
        if loupan_nodes['loupan_discount_nodes']:
            loupan_item['loupan_discount'] = loupan_nodes['loupan_discount_nodes'].extract()[0].strip()
        else:
            loupan_item['loupan_discount'] = ''
        if loupan_nodes['loupan_layout_nodes']:
            loupan_item['loupan_layout'] = loupan_nodes['loupan_layout_nodes'].extract()[0].strip()
        else:
            loupan_item['loupan_layout'] = ''
        if loupan_nodes['loupan_location_nodes']:
            loupan_item['loupan_location'] = loupan_nodes['loupan_location_nodes'].extract()[0].strip()
        else:
            loupan_item['loupan_location'] = ''
        if loupan_nodes['loupan_opening_nodes']:
            loupan_item['loupan_opening'] = loupan_nodes['loupan_opening_nodes'].extract()[0].strip()
        else:
            loupan_item['loupan_opening'] = ''
        if loupan_nodes['loupan_transfer_nodes']:
            loupan_item['loupan_transfer'] = loupan_nodes['loupan_transfer_nodes'].extract()[0].strip()
        else:
            loupan_item['loupan_transfer'] = ''
        if loupan_nodes['loupan_type_nodes']:
            loupan_item['loupan_type'] = loupan_nodes['loupan_type_nodes'].extract()[0].strip()
        else:
            loupan_item['loupan_type'] = ''
        if loupan_nodes['loupan_age_nodes']:
            loupan_item['loupan_age'] = loupan_nodes['loupan_age_nodes'].extract()[0].strip()
        else:
            loupan_item['loupan_age'] = ''
        return loupan_item


    def parse_item(self, response):
        loupan_status_nodes = response.xpath('/html/body/div[1]/div[3]/div/div[2]/i/text()')
        if loupan_status_nodes.extract()[0].strip() == '售罄':
            loupan_item = self.get_sellout_item(response)
        elif loupan_status_nodes.extract()[0].strip() == '待售':
            loupan_item = self.get_sellwait_item(response)
        else:
            loupan_item = self.get_common_item(response)

        loupan_item['loupan_url'] = response.url
        return loupan_item

