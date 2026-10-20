
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Cloud Insights",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Cloud Insights")
st.write("CSV 데이터를 업로드하고 핵심 지표를 분석하세요.")

uploaded_file = st.file_uploader(
    "CSV 파일을 업로드하세요",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("데이터 미리보기")
    st.dataframe(df.head(), use_container_width=True)

    st.subheader("핵심 지표")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "총 방문자 수",
        f"{df['visitors'].sum():,}명"
    )

    total_visitors = df["visitors"].sum()
    total_signups = df["signups"].sum()

    conversion_rate = (
        round(total_signups / total_visitors * 100, 2)
        if total_visitors > 0
        else 0
    )

    col3.metric(
        "가입 전환율",
        f"{conversion_rate:.2f}%"
    )

    st.subheader("날짜별 방문자 추이")
    chart_df = df.copy()
    chart_df["date"] = pd.to_datetime(chart_df["date"])
    chart_df = chart_df.sort_values("date")
    chart_df = chart_df.set_index("date")

    st.line_chart(chart_df["visitors"])

    st.subheader("날짜별 가입자 추이")
    st.line_chart(chart_df["signups"])
