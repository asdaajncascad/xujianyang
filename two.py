import streamlit as st
import pandas as pd
import numpy as np

# 模拟数据
data = {
    "餐厅名称": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "白妈螺狮粉"],
    "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
    "价格（元）": [15, 20, 25, 35, 50],
    "高峰时段订单量": [80, 70, 75, 60, 55],
    "经度": [108.2929, 108.2856, 108.2783, 108.2698, 108.2612],
    "纬度": [22.8428, 22.8355, 22.8282, 22.8197, 22.8111]
}
df = pd.DataFrame(data)

# 设置页面标题
st.title("南宁美食数据仪表盘")

# 餐厅评分 - bar_chart
st.header("餐厅评分")
bar_chart_data = df[["餐厅名称", "评分"]].set_index("餐厅名称")
st.bar_chart(bar_chart_data)

# 不同类型餐厅价格 - line_chart
st.header("不同类型餐厅价格")
line_chart_data = df[["餐厅名称", "价格（元）"]].set_index("餐厅名称")
st.line_chart(line_chart_data)

# 用餐高峰时段 - area_chart
st.header("用餐高峰时段订单量")
area_chart_data = df[["餐厅名称", "高峰时段订单量"]].set_index("餐厅名称")
st.area_chart(area_chart_data)

# 餐厅详情
st.header("餐厅详情")
selected_restaurant = st.selectbox("选择餐厅查看详情", df["餐厅名称"])
selected_df = df[df["餐厅名称"] == selected_restaurant]
st.write(f"评分：{selected_df.iloc[0]['评分']}/5.0")
st.write(f"价格：{selected_df.iloc[0]['价格（元）']}元")
# 当前拥挤程度
st.header（"当前拥挤程度"）
st.progress(94)
