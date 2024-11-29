"""
Streamlit Application for Dynamic Random Page Loading.

This module provides a Streamlit-based user interface that randomly selects a page
from a list of available pages or allows navigation through a sidebar. It demonstrates
the use of Streamlit's multi-page navigation features, enabling a dynamic user experience.

Modules:
    - streamlit: For creating the web application interface.
    - random: For randomly selecting a page from the available list.

Directory Structure:
    - pages/
        - Contains the modules for individual pages (e.g., `page1.py`, `page2.py`, etc.).    
"""

import streamlit as st
import random  # For randomly selecting a page

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
st.set_page_config(page_title="Dynamic Random Page Loader", layout="wide")

# -----------------------------------------------------
# Random Page Selection
# -----------------------------------------------------
page = random.choice(["pages/page1.py", "pages/page2.py", "pages/page3.py"])  

# -----------------------------------------------------
# Sidebar Navigation
# -----------------------------------------------------
def generate_sidebar_links(tabs: list, label: str = "page"):
    """
    Generates sidebar links for navigating between pages.

    **Parameters:**
    - `tabs (list):` A list of relative paths to the page modules.
    - `label (str):` The display label for the page in the sidebar (default is "page").

    **Functionality:**
    Iterates through the list of page paths (`tabs`) and creates a clickable link
    for each page in Streamlit's sidebar.

    **Example Usage:**
        tabs = ["pages/page1.py", "pages/page2.py", "pages/admin.py"]
        generate_sidebar_links(tabs)

    **Raises:**
    - No exceptions are raised directly by this function, but the `page_link` function
      depends on the validity of the page paths in the `tabs` list.
    """
    if not tabs:
        st.error("No pages available to display.")
        st.stop()

    for page_id in tabs:
        st.sidebar.page_link(
            page_id, label=label  # Adds each page as a clickable link in the sidebar
        )

# Example usage of the function
tabs = [page, "pages/admin.py"]  # Example tabs list
generate_sidebar_links(tabs)

# -----------------------------------------------------
# Page Switching
# -----------------------------------------------------
st.switch_page(page)