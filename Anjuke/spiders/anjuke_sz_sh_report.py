import matplotlib.pyplot as plt
import pymysql
import numpy as np

class AjukeSZSHReport():
    def __init__(self):
        self.db = pymysql.connect('127.0.0.1', 'root', 'root', 'anjuke', charset='utf8')
        self.cursor = self.db.cursor()

    def export_result_piture(self):
        district = ['南山','宝安','福田','罗湖','光明','龙华','龙岗','坪山','盐田','大鹏','深圳','惠州','东莞']
        x =  np.arange(len(district))
        house_price_avg = []
        for district_temp in district:
            if district_temp == '深圳':
                sql = "select house_price from sz_sh_house_info where house_location not like '%周边%'"
            else:
                sql = "select house_price from sz_sh_house_info where house_location like '%" + district_temp + "%'"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            house_price_sum = 0
            house_num = 0
            for result in results:
                house_price_dict = result[0].split(' ')
                house_price_sum += int(house_price_dict[0])
                house_num += 1
            house_price_avg.append(house_price_sum/house_num)
        bars = plt.bar(x, house_price_avg)
        plt.xticks(x, district)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        i = 0
        for bar in bars:
            plt.text((bar.get_x()+bar.get_width()/2),bar.get_height(),'%d'%house_price_avg[i],ha='center',va='bottom')
            i += 1
        plt.show()

        def __del__(self):
            self.db.close()

if __name__ == '__main__':
    anjukeSZReport = AjukeSZSHReport()
    anjukeSZReport.export_result_piture()