import streamlit as st

st.title("Search Pump using at least one condition:")

# Application Environment
st.subheader("Application Environment")
application_area = st.selectbox(
    "Application area",
    options=["Select application area..."],
    key="application_area"
)

# Size
st.subheader("Size")
col1, col2, col3 = st.columns(3)

with col1:
    size_l_col1, size_l_col2 = st.columns([3, 1])
    with size_l_col1:
        size_l = st.text_input("", key="size_l", placeholder="", label_visibility="collapsed")
    with size_l_col2:
        unit_l = st.selectbox("", options=["mm"], key="unit_l", label_visibility="collapsed")
    st.caption("(l)")

with col2:
    size_w_col1, size_w_col2 = st.columns([3, 1])
    with size_w_col1:
        size_w = st.text_input("", key="size_w", placeholder="", label_visibility="collapsed")
    with size_w_col2:
        unit_w = st.selectbox("", options=["mm"], key="unit_w", label_visibility="collapsed")
    st.caption("(w)")

with col3:
    size_h_col1, size_h_col2 = st.columns([3, 1])
    with size_h_col1:
        size_h = st.text_input("", key="size_h", placeholder="", label_visibility="collapsed")
    with size_h_col2:
        unit_h = st.selectbox("", options=["mm"], key="unit_h", label_visibility="collapsed")
    st.caption("(h)")

# Performance
st.subheader("Performance")

col1, col2 = st.columns(2)

with col1:
    flow_col1, flow_col2 = st.columns([3, 1])
    with flow_col1:
        flow_rate = st.text_input("Flow rate", key="flow_rate", placeholder="", label_visibility="collapsed")
    with flow_col2:
        flow_rate_unit = st.selectbox("", options=["l/s"], key="flow_rate_unit", label_visibility="collapsed")
    st.caption("Flow rate")

with col2:
    head_col1, head_col2 = st.columns([3, 1])
    with head_col1:
        head = st.text_input("Head", key="head", placeholder="", label_visibility="collapsed")
    with head_col2:
        head_unit = st.selectbox("", options=["h"], key="head_unit", label_visibility="collapsed")
    st.caption("Head")

# Brand
st.subheader("Brand")
brand = st.selectbox(
    "Brand",
    options=["No limited (Default)"],
    key="brand"
)

