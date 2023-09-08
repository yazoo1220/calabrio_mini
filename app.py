import streamlit as st
from calabrio_py.api import AsyncApiClient
from calabrio_py.manager import ConfigManager, PeopleManager, PersonAccountsManager
import os
from dotenv import load_dotenv
import asyncio
from tqdm import tqdm
import pandas as pd

st.title('Calabrio Mini')

# Access the environment variables
with st.sidebar:
  api_token = st.input("API Token: ")
  base_url = st.input("https://wise.teleopticloud.com/api/")
  business_units_to_exclude = st.input("").split(",")

if st.button("Run"):
  client = AsyncApiClient(base_url, api_token)

  people_mgr = PeopleManager(client)
  people_df = await people_mgr.fetch_all_people(with_ids=True, exclude_bu_names=business_units_to_exclude)

  st.dataframe(people_df)
