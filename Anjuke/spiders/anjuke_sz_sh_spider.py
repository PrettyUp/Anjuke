import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from Anjuke.items import AnjukeSZSHItem


class AnjukeSpider(scrapy.spiders.CrawlSpider):
    name = 'anjuke_sz_sh'

    allow_domains = ["anjuke.com"]

    start_urls = [
        'https://shenzhen.anjuke.com/sale/p1',
    ]

    rules = [
        Rule(LinkExtractor(allow=("https://shenzhen\.anjuke\.com/sale/p\d{1,}"))),
        Rule(LinkExtractor(allow=("https://shenzhen\.anjuke\.com/prop/view/A\d{1,}")), follow=False, callback='parse_item')
    ]

    def get_house_item(self,response):
        house_nodes = {}
        house_nodes["house_title_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[3]/h3/text()')
        house_nodes["house_cost_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[1]/span[1]/em/text()')
        house_nodes["house_code_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/h4/span[2]/text()')
        house_nodes["house_community_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div/div[1]/div/div[1]/dl[1]/dd/a/text()')
        house_nodes["house_location_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div/div[1]/div/div[1]/dl[2]/dd/p')
        house_nodes["house_build_years_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div/div[1]/div/div[1]/dl[3]/dd/text()')
        house_nodes["house_kind_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div/div[1]/div/div[1]/dl[4]/dd/text()')
        house_nodes["house_layout_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div/div[1]/div/div[2]/dl[1]/dd/text()')
        house_nodes["house_size_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div/div[1]/div/div[2]/dl[2]/dd/text()')
        house_nodes["house_face_to_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div/div[1]/div/div[2]/dl[3]/dd/text()')
        house_nodes["house_point_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div/div[1]/div/div[2]/dl[4]/dd/text()')
        house_nodes["house_price_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div/div[1]/div/div[3]/dl[1]/dd/text()')
        house_nodes["house_first_pay_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div/div[1]/div/div[3]/dl[2]/dd/text()')
        house_nodes["house_month_pay_nodes"] = response.xpath('//*[@id="reference_monthpay"]/text()')
        house_nodes["house_decorate_type_nodes"] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div/div[1]/div/div[3]/dl[4]/dd/text()')
        house_nodes['house_agent_nodes'] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[1]/div/div/text()')
        house_nodes['house_agency_nodes'] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[5]/div/p[1]/a/text()')
        if not house_nodes['house_agency_nodes']:
            house_nodes['house_agency_nodes'] = response.xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[5]/div/p/text()')

        house_item = self.struct_house_item(house_nodes)
        return house_item


    def struct_house_item(self,house_nodes):
        house_item = AnjukeSZSHItem()
        if house_nodes['house_title_nodes']:
            house_item['house_title'] = house_nodes['house_title_nodes'].extract()[0].strip()
        else:
            house_item['house_title'] = ''
        if house_nodes['house_cost_nodes']:
            house_item['house_cost'] = house_nodes['house_cost_nodes'].extract()[0].strip()
        else:
            house_item['house_cost'] = ''
        if house_nodes['house_code_nodes']:
            temp_dict = house_nodes['house_code_nodes'].extract()[0].strip().split('，')
            house_item['house_code'] = temp_dict[0]
            house_item['house_public_time'] = temp_dict[1]
        else:
            house_item['house_code'] = ''
            house_item['house_public_time'] = ''
        if house_nodes['house_community_nodes']:
            house_item['house_community'] = house_nodes['house_community_nodes'].extract()[0].strip()
        else:
            house_item['house_community'] = ''
        if house_nodes['house_location_nodes']:
            house_item['house_location'] = house_nodes['house_location_nodes'].xpath('string(.)').extract()[0].strip().replace('\t','').replace('\n','')
        else:
            house_item['house_location'] = ''
        if house_nodes['house_build_years_nodes']:
            house_item['house_build_years'] = house_nodes['house_build_years_nodes'].extract()[0].strip()
        else:
            house_item['house_build_years'] = ''
        if house_nodes['house_kind_nodes']:
            house_item['house_kind'] = house_nodes['house_kind_nodes'].extract()[0].strip()
        else:
            house_item['house_kind'] = ''
        if house_nodes['house_layout_nodes']:
            house_item['house_layout'] = house_nodes['house_layout_nodes'].extract()[0].strip().replace('\t','').replace('\n','')
        else:
            house_item['house_layout'] = ''
        if house_nodes['house_size_nodes']:
            house_item['house_size'] = house_nodes['house_size_nodes'].extract()[0].strip()
        else:
            house_item['house_size'] = ''
        if house_nodes['house_face_to_nodes']:
            house_item['house_face_to'] = house_nodes['house_face_to_nodes'].extract()[0].strip()
        else:
            house_item['house_face_to'] = ''
        if house_nodes['house_point_nodes']:
            house_item['house_point'] = house_nodes['house_point_nodes'].extract()[0].strip()
        else:
            house_item['house_point'] = ''
        if house_nodes['house_price_nodes']:
            house_item['house_price'] = house_nodes['house_price_nodes'].extract()[0].strip()
        else:
            house_item['house_price'] = ''
        if house_nodes['house_first_pay_nodes']:
            house_item['house_first_pay'] = house_nodes['house_first_pay_nodes'].extract()[0].strip()
        else:
            house_item['house_first_pay'] = ''
        if house_nodes['house_month_pay_nodes']:
            house_item['house_month_pay'] = house_nodes['house_month_pay_nodes'].extract()[0].strip()
        else:
            house_item['house_month_pay'] = ''
        if house_nodes['house_decorate_type_nodes']:
            house_item['house_decorate_type'] = house_nodes['house_decorate_type_nodes'].extract()[0].strip()
        else:
            house_item['house_decorate_type'] = ''
        if house_nodes['house_agent_nodes']:
            house_item['house_agent'] = house_nodes['house_agent_nodes'].extract()[0].strip()
        else:
            house_item['house_agent'] = ''
        if house_nodes['house_agency_nodes']:
            house_item['house_agency'] = house_nodes['house_agency_nodes'].extract()[0].strip()
        else:
            house_item['house_agency'] = ''
        return house_item


    def parse_item(self, response):
        house_item = self.get_house_item(response)
        house_item['house_url'] = response.url
        return house_item
