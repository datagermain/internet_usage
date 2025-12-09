import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config( layout="wide")

st.header("Internet Usage Analytics")

df=pd.read_csv("share-of-individuals-using-the-internet.csv")
print(df.head())
# get unique years
years = df['Year'].unique()
countries = df['Country'].unique()
selected_year = st.selectbox(label ="Select Year", options=years)

df_plot = df[df['Year']==selected_year]

col1, col2 = st.columns([3,1])
plot = px.choropleth(df[df['Year']==selected_year],
                     locations="Country",
                        locationmode='country names',
                        color="Individuals using the Internet (% of population)",
                        hover_name="Country",
                        title=f"Internet Usage in {selected_year}",)
histogram1 = px.histogram(df_plot, 
                        x="Individuals using the Internet (% of population)", 
                        nbins=20,
                        title=f"Distribution of Internet Usage in {selected_year}",
                        labels={"Individuals using the Internet (% of population)": "Internet Usage (% of population)"})
col1.plotly_chart(plot, use_container_width=True) 
col2.plotly_chart(histogram1)

sidebar = st.sidebar.subheader('Country level')
form = st.sidebar.form("form")
selected_country = form.selectbox("Select Country", options = countries, index=0)
submitted = form.form_submit_button("Submit")
if submitted:

   st.subheader("Country Level Analytics for {}".format(selected_country))
   df_country = df[df['Country']==selected_country]
   line_plot = px.line(df_country,
                       x='Year',
                         y='Individuals using the Internet (% of population)',
                           title=f"Internet Usage Over Years for {selected_country}")
   st.plotly_chart(line_plot)
                       
