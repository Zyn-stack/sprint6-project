import streamlit as st
import pandas as pd
import plotly.express as px


st.header("Market of Used Cars")
st.write("""###Filter the data below to see the data by manufactuerer""")
df = pd.read_csv('cars_workshop.csv')
df = df.drop(df.columns[0], axis=1)
manufactures_choice = df['manufactuer_name'].unique()
make_choice_man = st.selectbox('Select manufacturer:' :manufacturer_choice)

df_filtered = df[df[‘manufacturer_name’] == make_choice_man]
min_year,max_year=int(df['year_produced'].min()),int(df['year_produced'].max())
year_range = st.slider("Choose years",value=(min_year,max_year), min_value=min_year,max_value=max_year)
actual_range = list(range(year_range[0],year_range[1]+1))


df_filtered = df[(df.manufactuerer_name==make_choice_man)&(df.year_produced.isin(list(actual_range)))]

st.table(df_filtered)

st.header('Price Analysis')
st.write("""###### Let's analyze what influences price the most. We will check how distribution of price varies depending on transmission, engine or body type and state""")

list_for_hist=['transmission', 'engine_type', 'body_type', 'state']
choice_for_hist = st.selectbox('Split for price distribution',list_for_hist)
fig1 = px.histogram(df, x="price_usd", color=choice_for_hist)
fig1.update_layout(title="<b> Split of price by {}</b>".format(choice_for_hist))
st.plotly_chart(fig1)

df['age']=2023-df['year_produced']
def age_category(x):
    if x<5: return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return'10-20'
    else: return '>20'
df['age_category']= df['age'].apply(age_category)

st.write("""###### Now lets check how the price is affected by odometer, engine capacity or number of photos in the adds""")
list_for_scatter=['odometer_value','engine_capacity', 'number_of _photos']
choice_for_scatter = st.selctbox('Price dependency on', list_for_scatter)
fig2 = px.scatter(df, x="price_usd", y=choice_for_scatter, color="age_category", hover_data=["year_produced"])
fig2.update_layout(title="<b> Price vs {}</b>",format(choice_for_scatter))
st.plotly_chart(fig2)
