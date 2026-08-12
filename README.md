# Python 可视化大屏聚合演示

一个基于 **Python + pyecharts + ECharts + Flask** 的可视化大屏案例集，包含智慧城市、影视数据、社交媒体舆情、房源和商业数据等 12 个主题。

本仓库用于在线效果展示，未开源 pyecharts 数据采集与生成代码；部分页面使用历史公开数据样本，不代表实时数据。

## 在线演示

访问：[https://mashukui.github.io/visual-dashboard-demo2/](https://mashukui.github.io/visual-dashboard-demo2/)

## 技术栈

- Python / Flask
- pyecharts / ECharts
- GitHub Pages

## 案例主题

在线目录：[mashukui.github.io/visual-dashboard-demo2](https://mashukui.github.io/visual-dashboard-demo2/)

包含 LOL 比赛、智慧城市、微博舆情、豆瓣电影、腾讯影视、公司收入、抖音销售、58 同城房源、微博热搜和淄博烧烤评论等大屏。

## 本地运行

Flask 方式：

```bash
pip install flask
python app.py
```

静态预览：

```bash
python -m http.server 8000 --directory docs
```

## 说明

`templates/` 为 Flask 本地演示页面，`docs/` 为 GitHub Pages 静态部署版本。建议电脑横屏查看各大屏；手机端会自动缩放以便浏览。
