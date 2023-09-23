import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts

df = pd.read_csv('data.csv')
china_map = (
    Map()
    .add("现有确诊", [list(i) for i in zip(df['area'].values.tolist(), df['curConfirm'].values.tolist())], 'china')
    .set_global_opts(
        title_opts=opts.TitleOpts(title='各地区确诊人数'),
        visualmap_opts=opts.VisualMapOpts(max_=100, is_piecewise=True)
    )
)
china_map.render("1.html")
