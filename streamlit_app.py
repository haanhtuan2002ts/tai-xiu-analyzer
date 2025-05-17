import streamlit as st

st.title("Phân Tích Tài/Xỉu - AI")
st.write("Chào mừng bạn đến với ứng dụng phân tích Tài/Xỉu!")

# Ví dụ đơn giản để bắt đầu
so_lan = st.number_input("Nhập số lần quay gần nhất bạn muốn phân tích:", min_value=1, max_value=100, value=20)

if st.button("Phân tích"):
    st.success(f"Đang phân tích {so_lan} lượt gần nhất... (tính năng đang được nâng cấp)")
