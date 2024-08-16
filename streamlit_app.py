import streamlit as st

#Page setup
home = st.Page(
    page = "views/homepage.py",
    title = "Homepage",
    icon = ":material/home:",
    default = True,
)

summary = st.Page(
    page = "views/summary.py",
    title = "Summary",
    icon = ":material/summarize:",
)

category_analysis = st.Page(
    page = "views/category_analysis.py",
    title = "Category Analysis",
    icon = ":material/analytics:",
)

demand_forecasting = st.Page(
    page = "views/demand_forecasting.py",
    title = "Demand Forecasting",
    icon = ":material/monitoring:"
)

pg = st.navigation({
    "Info" : [home],
    "Analytics" : [summary, category_analysis, demand_forecasting]
})


st.logo("assets/ForeSight.png")

pg.run()
