import streamlit as st
import plotly.graph_objects as go

# 标题
st.title("发酵阶段雷达图")

# 颜色和数据
categories = ["Fruit Aroma", "VinegarNote", "Acidity", "Carbonation", "Sweetness"]
data = {
    "第一阶段 - 4天": [8, 3, 5, 4, 9],
    "第一阶段 - 7天": [6, 4, 6, 5, 7],
    "第二阶段 - 2天": [5, 6, 6, 3, 4],
    "第二阶段 - 4天": [3, 8, 7, 2, 2],
}
colors = ["#FFA500", "#D2691E", "#DC143C", "#FF69B4"]

# 选择阶段
selected_stage = st.selectbox("选择发酵阶段", list(data.keys()))

# 生成雷达图
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=data[selected_stage] + [data[selected_stage][0]],  # 闭合雷达图
    theta=categories + [categories[0]],
    fill='toself',
    name=selected_stage,
    line=dict(color=colors[list(data.keys()).index(selected_stage)], width=2),
    opacity=0.7
))

# 设置样式
fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
    showlegend=True
)

# 显示图表
st.plotly_chart(fig)
