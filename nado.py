# 파이썬 클래스
class House:
    locations = []
    house_types = []
    deal_types = []
    prices = []
    completion_years = []

    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.locations.append(location)
        self.house_types.append(house_type)
        self.deal_types.append(deal_type)
        self.prices.append(price)
        self.completion_years.append(completion_year)

    def show_detail(self):
        print(f'총 {len(self.locations)}대의 매물이 있습니다.')
        for i in range(0, len(self.locations)):
            print(f'{self.locations[i]} {self.house_types[i]} {self.deal_types[i]} {self.prices[i]} {self.completion_years[i]}')


house1 = House('강남', '아파트', '매매', '10억', '2010년')
house2 = House('마포', '오피스텔', '전세', '5억', '2007년')
house3 = House('송파', '빌라', '월세', '500/50', '2000년')
