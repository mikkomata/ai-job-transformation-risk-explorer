
import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE CONFIGURATION
st.set_page_config(
    page_title="AI Job Risk Explorer",
    page_icon="📊",
    layout="wide"
)

# LOAD DATA
@st.cache_data
def load_data():
    return pd.read_csv(
        "AI_Job_Risk_Explorer.csv",
        encoding="utf-8-sig"
    )

df = load_data()

# HEADER
st.title("🌐 AI Job Transformation & Displacement Risk Explorer")
st.caption("Explore occupational risk classifications across 19 industries | 2026–2040")

st.info(
    "This project presents qualitative analytical assessments. "
    "Risk classifications are not probabilities of job loss."
)

# SIDEBAR FILTERS
st.sidebar.header("Explore the dataset")

industries = ["All Industries"] + sorted(
    df["Industry / Job Category"].unique().tolist()
)

selected_industry = st.sidebar.selectbox(
    "Select Industry",
    industries
)

risk_levels = ["All Risks", "Very High", "High", "Moderate", "Lower"]

selected_risk = st.sidebar.selectbox(
    "Select Risk Category",
    risk_levels
)

search = st.sidebar.text_input(
    "Search Occupation"
)

# FILTER DATA
filtered_df = df.copy()

if selected_industry != "All Industries":
    filtered_df = filtered_df[
        filtered_df["Industry / Job Category"] == selected_industry
    ]

if selected_risk != "All Risks":
    filtered_df = filtered_df[
        filtered_df["Risk Category"] == selected_risk
    ]

if search:
    filtered_df = filtered_df[
        filtered_df["Job / Occupation"].str.contains(
            search, case=False, na=False
        )
    ]

# KEY METRICS
c1, c2, c3 = st.columns(3)

c1.metric("Occupation Records", len(filtered_df))
c2.metric("Industry Categories", filtered_df["Industry / Job Category"].nunique())
c3.metric("Unique Occupation Titles", filtered_df["Job / Occupation"].nunique())

st.divider()

# RISK DISTRIBUTION
st.subheader("Risk Distribution")

risk_order = ["Very High", "High", "Moderate", "Lower"]

risk_counts = (
    filtered_df["Risk Category"]
    .value_counts()
    .reindex(risk_order, fill_value=0)
    .rename_axis("Risk Category")
    .reset_index(name="Occupation Count")
)

fig_risk = px.bar(
    risk_counts,
    x="Risk Category",
    y="Occupation Count",
    color="Risk Category",
    title="Occupation Distribution by Risk Category"
)

st.plotly_chart(fig_risk, use_container_width=True)

# INDUSTRY COMPARISON
st.subheader("Risk Assessment by Industry")

industry_risk = pd.crosstab(
    filtered_df["Industry / Job Category"],
    filtered_df["Risk Category"],
    normalize="index"
) * 100

industry_risk = industry_risk.reindex(
    columns=risk_order,
    fill_value=0
)

if not industry_risk.empty:
    industry_long = (
        industry_risk.reset_index()
        .melt(
            id_vars="Industry / Job Category",
            var_name="Risk Category",
            value_name="Percentage"
        )
    )

    fig_industry = px.bar(
        industry_long,
        x="Industry / Job Category",
        y="Percentage",
        color="Risk Category",
        barmode="stack",
        title="Risk Distribution Across Industries (%)"
    )

    fig_industry.update_layout(
        xaxis_tickangle=-55
    )

    st.plotly_chart(fig_industry, use_container_width=True)

# OCCUPATION TABLE
st.subheader("Occupation Explorer")

st.dataframe(
    filtered_df[
        [
            "Industry / Job Category",
            "Job / Occupation",
            "Description",
            "Risk Category"
        ]
    ],
    use_container_width=True,
    hide_index=True
)

# FOOTER
st.divider()
st.caption(
    "AI Job Risk Explorer | Independent analytical portfolio project | "
    "2026–2040. Assessments are qualitative and subject to revision."
)
