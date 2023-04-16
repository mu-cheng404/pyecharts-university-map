import json, pickle

from pyecharts import options as opts
from pyecharts.render import make_snapshot
from pyecharts.charts import Geo
from pyecharts.globals import ThemeType
from snapshot_phantomjs import snapshot
from generate_coordinate import generate_coordinate

generate_coordinate()

city_undergraduate = []
with open("coordinates/city_undergraduate.pkl", 'rb') as f:
    city_undergraduate = pickle.load(f)
city_graduate = []
with open("coordinates/city_graduate.pkl", 'rb') as f:
    city_graduate = pickle.load(f)

geo = (
    Geo(
        # 初始化地图
        init_opts=opts.InitOpts(
            width="1000px",
            height="600px",
            theme=ThemeType.ESSOS,  # 地图主题
        ),
        is_ignore_nonexistent_coord=True
    )

    # 地图类型
    .add_schema(maptype='china',
                label_opts=opts.LabelOpts(is_show=False),
                zoom=1.5,
                center=[105.95, 34.27]
                )

)


def generate_graduate():
    geo.add(
        series_name='研究生',
        symbol_size=18,
        data_pair=city_graduate,
        type_="scatter",
        label_opts=opts.LabelOpts(is_show=True,
                                  formatter='{b}',
                                  font_size=20,
                                  font_style="normal",
                                  # font_family='monospace'
                                  ))
    # 先将图表渲染为 HTML 文件
    geo.render('html/graduate.html')
    print("渲染html完成")

    # 然后调用 make_snapshot() 方法进行截图
    make_snapshot(snapshot, 'html/graduate.html', 'image/graduate.png')
    print("渲染png完成")


def generate_undergraduate():
    geo.add(
        series_name='本科',
        symbol_size=18,
        data_pair=city_undergraduate,
        type_="scatter",
        color="auto",
        label_opts=opts.LabelOpts(is_show=True,
                                  formatter='{b}',
                                  font_size=20,
                                  font_style="normal",
                                  # font_family='monospace'
                                  ))

    # 先将图表渲染为 HTML 文件
    geo.render('html/undergraduate.html')
    print("渲染html完成")
    # 然后调用 make_snapshot() 方法进行截图
    make_snapshot(snapshot, 'html/undergraduate.html', 'image/undergraduate.png')
    print("渲染png完成")
if __name__ == "__main__":
    # generate_undergraduate()
    generate_graduate()