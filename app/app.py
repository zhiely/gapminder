import streamlit as st
import pandas as pd

# Define a function to load data
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/zhiely/streamlit_gapminder/main/merged_df.csv'
    df = pd.read_csv(url)
    return df

# Main Streamlit code
def main():
    st.title('Gapminder')
    st.write("Unlocking Lifetimes: Visualizing Progress in Longevity and Poverty Eradication")

    year = st.slider("YEAR", 1800, 2100)
    st.write("Selected Year:", year)

    # Load data
    df_data = load_data()
    st.write(df_data)  # Output loaded data

if __name__ == "__main__":
    main()
