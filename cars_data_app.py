import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Cars DataViz')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

df_cars.dropna(inplace=True)
numeric_columns = ['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60', 'year']



selected_region = st.sidebar.selectbox("Select a region",
                                       ('All regions', 'US', 'Europe', 'Japan'))


if selected_region == 'All regions':
    df_region = df_cars.copy()
    st.write('Data for all regions')
else:
    df_region = df_cars[df_cars['continent'].str.contains(selected_region)]
    st.write(f'Data for {selected_region} region ')



fig, ax = plt.subplots()
plt.figure(figsize=(10, 8))
sns.heatmap(df_region[numeric_columns].corr(),
            ax=ax, cmap='coolwarm',
            annot=True, fmt='.2f')
st.write(fig)


for col in numeric_columns:
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df_region[col], kde=True)
    plt.title(f'Distribution de {col} - {selected_region}')
    st.pyplot(fig)

for col in numeric_columns:
    fig = px.box(df_region, y=col)
    fig.update_layout(title=f'Boxplot de {col} - {selected_region}', yaxis=dict(title=f'{col}'))
    st.plotly_chart(fig)

