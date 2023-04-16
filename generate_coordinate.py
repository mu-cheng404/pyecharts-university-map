import json
import pickle

def generate_coordinate():
    city_c = []
    with open("coordinates/city_coordinates.json", 'r', encoding='utf-8') as f:
        city_c = json.load(f)

    # 大学城市
    city1 = ['上海', '济南', '长春', '赣州市', '南昌', '湛江']
    university = ['上海应用技术大学', '济南大学', '吉林工商学院', '赣南师范大学', '东华理工大学', '广东海洋大学']
    city_undergraduate = []
    for idx, item in enumerate(city1):
        city_undergraduate.append((item, city_c[item] + [100]))

    with open("coordinates/city_undergraduate.pkl", 'wb') as f:
        pickle.dump(city_undergraduate, f)

    # 研究生城市
    city2 = ['上海', '北京', '成都', '厦门', '西安', '杭州']
    university = ['上海电力大学', '北京邮电大学', '西南财经大学', '集美大学', '长安大学', '自然资源部第二海洋研究所']
    city_graduate = []
    for idx, item in enumerate(city2):
        city_graduate.append((item, city_c[item] + [100]))

    with open("coordinates/city_graduate.pkl", 'wb') as f:
        pickle.dump(city_graduate, f)


generate_coordinate()