import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="ردیاب طلا", layout="wide")

st.title("🏆 ردیاب قیمت طلا - ایران")
st.markdown("به‌روزرسانی لحظه‌ای قیمت طلا و سکه")

# داده نمونه (بعداً می‌توانی واقعی کنی)
price_data = {
    "date": pd.date_range(start="2025-01-01", periods=30, freq="D"),
    "price_18k": [3_450_000 + i*5000 for i in range(30)],
    "price_coin": [42_500_000 + i*25000 for i in range(30)]
}
df = pd.DataFrame(price_data)

col1, col2 = st.columns(2)

with col1:
    st.subheader("قیمت طلای ۱۸ عیار")
    fig1 = px.line(df, x="date", y="price_18k", title="تغییرات قیمت طلا")
    st.plotly_chart(fig1, use_container_width=True)
    
with col2:
    st.subheader("قیمت سکه امامی")
    fig2 = px.line(df, x="date", y="price_coin", title="تغییرات قیمت سکه")
    st.plotly_chart(fig2, use_container_width=True)

st.metric("قیمت لحظه‌ای طلای ۱۸ عیار", f"{df['price_18k'].iloc[-1]:,} تومان", 
          delta=f"{df['price_18k'].iloc[-1] - df['price_18k'].iloc[-2]:,}")

st.caption(f"آخرین به‌روزرسانی: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}") 
