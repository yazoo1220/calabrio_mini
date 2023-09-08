from calabrio_py.api import AsyncApiClient
from calabrio_py.manager import ConfigManager, PeopleManager, PersonAccountsManager
import os
from dotenv import load_dotenv
import asyncio
from tqdm import tqdm
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
    
    if st.button("Run"):
        base_url = "your_api_base_url"
        api_token = "your_api_token"
        business_units_to_exclude = ["BU1", "BU2"]  # Replace with your exclusion list
        
        # Use asyncio to run the asynchronous code
        loop = asyncio.get_event_loop()
        people_df = loop.run_until_complete(fetch_people_data(base_url, api_token, business_units_to_exclude))

        st.dataframe(people_df)

if __name__ == "__main__":
    main()






