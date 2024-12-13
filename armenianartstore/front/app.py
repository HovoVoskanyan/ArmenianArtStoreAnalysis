import os
import streamlit as st
from utils import get_champion, get_report

# Streamlit Page Configuration
st.set_page_config(page_title="Dynamic Page Loader", layout="wide")

# Desired project ID
PROJECT_ID = 1

# List existing page files dynamically
def list_existing_pages(pages_dir="pages"):
    return sorted([file for file in os.listdir(pages_dir) if file.startswith("page") and file.endswith(".py")])

# Fetch the champion bandit (using its ID)
champion_bandit = get_champion(PROJECT_ID)

# List actual pages in the `pages/` directory
existing_pages = list_existing_pages()

# Fetch report data and map bandit names to pages
def map_bandits_to_pages(project_id, existing_pages):

    report = get_report(project_id).to_dict(orient="records")

    # Create a mapping of bandit_name to the corresponding page file
    pages_mapping = {}
    for row in report:
        bandit_name = row["bandit_name"]
        matched = False
        for page in existing_pages:
            # Match bandit_name with page filename (e.g., "page1" matches "page1.py")
            if bandit_name in page:
                pages_mapping[bandit_name] = f"pages/{page}"
                matched = True
                break
        if not matched:
            raise ValueError(
                f"Please enter bandit name as: {', '.join(set([p.replace('.py', '').rstrip('0123456789') for p in existing_pages]))}"
            )

    return pages_mapping

# Generate the pages mapping using bandit_name
pages = map_bandits_to_pages(PROJECT_ID, existing_pages)
print(pages)
# Get the corresponding page for the champion bandit
page = pages.get(champion_bandit[0])
print(page)

def generate_sidebar_links(tabs: list, label: str = "page"):
    
    if not tabs:
        st.error("No pages available to display.")
        st.stop()

    for page_id in tabs:
        st.sidebar.page_link(
            page_id, label=label 
        )

tabs = list(pages.values()) + ["pages/admin.py"] 
generate_sidebar_links(tabs)

st.switch_page(page)