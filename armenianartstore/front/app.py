import os
import streamlit as st
from utils import get_champion, get_report

# Streamlit Page Configuration
st.set_page_config(page_title="Dynamic Page Loader", layout="wide")

# Desierd project ID
PROJECT_ID = 60

# # Fetch champion bandit dynamically
# try:
#     # `champion` is directly the page name, e.g., "page2"
#     champion_bandit = get_champion(PROJECT_ID)
#     print(f"Champion Bandit: {champion_bandit}")  # Debugging output
# except Exception as e:
#     st.error(f"Error fetching champion bandit: {e}")
#     st.stop()



# # For checking
# champion_bandit = get_champion(PROJECT_ID)

# # Map bandit names to pages
# pages = {f"page{i}": f"pages/page{i}.py" for i in range(1, 4)}

# page = pages.get(champion_bandit)



# # Fetch champion bandit dynamically
# try:
#     champion_bandit = get_champion(PROJECT_ID)  # Fetch the champion details
#     print(f"Champion Bandit: {champion_bandit}")  # Debugging
# except Exception as e:
#     st.error(f"Error fetching champion bandit: {e}")
#     st.stop()

# # Assuming `champion_bandit` contains a name dynamically returned by the API
# # Example: {"name": "dynamic_page_name"}
# bandit_name = champion_bandit.get("name", "default_page_name")

# # Map dynamic names to pages
# pages = {bandit_name: f"pages/{bandit_name}.py"}  # Dynamically map based on API response

# page = pages.get(bandit_name)



# # Fetch champion bandit dynamically
# try:
#     champion_bandit = get_champion(PROJECT_ID)  # Fetch the champion details
#     print(f"Champion Bandit: {champion_bandit}")  # Debugging
# except Exception as e:
#     st.error(f"Error fetching champion bandit: {e}")
#     st.stop()

# # # Extract bandit name
# bandit_name = champion_bandit.get("name", "default_page_name")

# pages = {f"bandit_name": f"pages/page{i}.py" for i in range(1, 4)}

# # Map dynamic names to pages
# pages = {bandit_name: f"pages/{bandit_name}.py"}  # Dynamically map based on API response

# page = pages.get(bandit_name)

# # # Map bandit names to pages
# pages = {f"bandit_name": f"pages/page{i}.py" for i in range(1, 4)}


# # Map bandit names to pages
# pages = {
#     "page1": "pages/page1.py",
#     "page2": "pages/page2.py",
#     "page3": "pages/page3.py"
# }

# # Get the page for the champion bandit
# page = pages.get(champion_bandit)


# # Fetch champion bandit dynamically
# try:
#     champion_bandit = get_champion(PROJECT_ID)  # Fetch the champion details
#     print(f"Champion Bandit: {champion_bandit}")  # Debugging
# except Exception as e:
#     st.error(f"Error fetching champion bandit: {e}")
#     st.stop()

# # Extract bandit name
# bandit_name = champion_bandit.get("name", "default_page_name")

# # Map dynamic names to pages
# pages = {bandit_name: f"pages/{bandit_name}.py"}  # Dynamically map based on API response

# page = pages.get(bandit_name)


# # Fetch champion bandit dynamically
# try:
#     champion_bandit = get_champion(PROJECT_ID)  # Example: ["bandit1", "bandit2", "bandit3"]
#     print(f"Champion Bandits for Project ID {PROJECT_ID}: {champion_bandit}")  # Debugging
# except Exception as e:
#     st.error(f"Error fetching champion bandits for Project ID {PROJECT_ID}: {e}")
#     st.stop()

# # Map bandit names to pages using f-strings
# #pages = {bandit: f"pages/page{i}.py" for i, bandit in enumerate(champion_bandit, start=1)}

# pages = {f"{bandit}": f"pages/page{i}.py" for i, bandit in enumerate(champion_bandit, start=1)}

# # Example: Select a specific bandit (this could come dynamically)  # Replace with user input or dynamic selection
# page = pages.get(champion_bandit)



# # List existing page files dynamically
# def list_existing_pages(pages_dir="pages"):
#     """List all available page files in the `pages/` directory."""
#     return [file for file in os.listdir(pages_dir) if file.startswith("page") and file.endswith(".py")]

# # Desired project ID
# PROJECT_ID = 27

# try:
#     # Fetch champion bandit dynamically
#     champion_bandit = get_champion(PROJECT_ID)  # Example: ["bandit1", "bandit2", "bandit3", "bandit4"]
#     print(f"Champion Bandits for Project ID {PROJECT_ID}: {champion_bandit}")  # Debugging
# except Exception as e:
#     st.error(f"Error fetching champion bandits for Project ID {PROJECT_ID}: {e}")
#     st.stop()

# # List actual pages in the `pages/` directory
# existing_pages = list_existing_pages()

# # Map bandit names to existing pages dynamically
# pages = {
#     bandit: f"pages/page{i}.py"
#     for i, bandit in enumerate(champion_bandit, start=1)
#     if f"page{i}.py" in existing_pages  # Only include pages that actually exist
# }

# page = pages.get(champion_bandit)


# List existing page files dynamically
def list_existing_pages(pages_dir="pages"):
    """List all available page files in the `pages/` directory."""
    return [file for file in os.listdir(pages_dir) if file.startswith("page") and file.endswith(".py")]

# Desired project ID
PROJECT_ID = 64

# Fetch the champion bandit (single name, e.g., "bandit2")
champion_bandit = get_champion(PROJECT_ID)  # Example: "bandit2"
print(f"Champion Bandit for Project ID {PROJECT_ID}: {champion_bandit}")  # Debugging

# List actual pages in the `pages/` directory
existing_pages = list_existing_pages()
print(existing_pages)
# Map a single bandit to an available page dynamically
# pages = {
#     f"bandit{i}": f"pages/page{i}.py"
#     for i in range(1, len(existing_pages) + 1)  # Map only to existing pages
# }

pages = {
    row["bandit_name"]: f"pages/page{i}.py"
    for i, row in enumerate(get_report(PROJECT_ID).to_dict(orient="records"), start=1)
    if f"page{i}.py" in existing_pages  # Map only to existing pages
}

print(pages)
# Get the corresponding page for the champion bandit
page = pages.get(champion_bandit)
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