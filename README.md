# pyecharts-university-map
用pyecharts插件制作标记六个大学所在城市分布的中国地图高清图

# 文件目录说明
coordinates 与坐标有关的文件  
--city_coordinates.json (地名,坐标)对应关系 比如"赣州": [114.56,28.52]，从https://github.com/pyecharts/pyecharts/blob/master/pyecharts/datasets/city_coordinates.json中获取  
--city_graduate.pkl
--city_undergraduate.pkl
html 存放渲染的html
--graduate.html 本科城市分布图
--undergraduate.html 研究生城市分布图
image 存放渲染的图片文件
--graduate.png 本科城市分布图
--undergraduate.png 研究生城市分布图
generate_coordinate.py 根据目标城市，在`city_coordinates.json`中查找坐标，合成对应数据存储到`city_graduate.pkl`和`city_undergraduate.pkl`
generate_undergraduate.py 根据`city_undergraduate.pkl`坐标绘制地图并渲染png图片
generate_graduate.py 根据`city_graduate.pkl`坐标绘制地图并渲染png图片
main.py 绘图主函数

# 主函数
```python
if __name__ == "__main__":
    #生成坐标数据
    generate_coordinate()
    #渲染本科城市分布图
    generate_graduate()
    #渲染研究生城市分布图
    generate_undergraduate()
```

相关博客文章 https://blog.csdn.net/m0_52942489/article/details/130184900


