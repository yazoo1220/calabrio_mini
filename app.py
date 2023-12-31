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
    st.title("Calabrio Mini")
    with st.sidebar:
        base_url = st.text_input("your_api_base_url")
        api_token = st.text_input("your_api_token")
        business_units_to_exclude = st.text_input("").split(',')  # Replace with your exclusion list
    if st.button("Run"):
        # Use a wrapper function to run asyncio code
        def run_async_code():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return loop.run_until_complete(fetch_people_data(base_url, api_token, business_units_to_exclude))

        # Call the wrapper function and display the result
        people_df = run_async_code()
        st.dataframe(people_df)

if __name__ == "__main__":
    main()
