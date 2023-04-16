from generate_undergraduate import generate_undergraduate
from generate_graduate import generate_graduate
from generate_coordinate import generate_coordinate
if __name__ == "__main__":
    #生成坐标数据
    generate_coordinate()
    #渲染本科城市分布图
    generate_graduate()
    #渲染研究生城市分布图
    generate_undergraduate()