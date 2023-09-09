from calabrio_py.api import AsyncApiClient
from calabrio_py.manager import ConfigManager, PeopleManager
import os
import asyncio
import pandas as pd
import streamlit as st


# Import your AsyncApiClient and PeopleManager here

async def fetch_people_data(base_url, api_token, business_units_to_exclude):
    client = AsyncApiClient(base_url, api_token)
    people_mgr = PeopleManager(client)
    people_df = await people_mgr.fetch_all_people(with_ids=True, exclude_bu_names=business_units_to_exclude)
    return people_df

def main():
    st.title("My Streamlit App")
    with st.sidebar:
        base_url = st.input("your_api_base_url")
        api_token = st.input("your_api_token")
        business_units_to_exclude = st.input("").split(',')  # Replace with your exclusion list
    if st.button("Run"):      
        # Use asyncio to run the asynchronous code
        loop = asyncio.get_event_loop()
        people_df = loop.run_until_complete(fetch_people_data(base_url, api_token, business_units_to_exclude))

        st.dataframe(people_df)

if __name__ == "__main__":
    main()






