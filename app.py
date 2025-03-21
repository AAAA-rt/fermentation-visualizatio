import streamlit as st
import plotly.graph_objects as go

# 标题
st.title("发酵阶段雷达图")

# 颜色和数据
categories = ["Fruit Aroma果香", "Vinegar Note醋", "Acidity酸", "Carbonation碳酸", "Sweetness甜"]
data = {
    "第一阶段 - 4天": [8, 3, 2, 5, 9],
    "第一阶段 - 7天": [6, 4, 3, 6, 7],
    "第二阶段 - 2天": [5, 6, 4, 6, 4],
    "第二阶段 - 4天": [3, 8, 5, 7, 2],
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

# 设置图表样式，禁用拖动
fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
    showlegend=True,
    dragmode=False  # 关闭拖动
)

# 显示雷达图，并禁用交互功能
st.plotly_chart(fig, use_container_width=oTrue, config={'staticPlot': True})
