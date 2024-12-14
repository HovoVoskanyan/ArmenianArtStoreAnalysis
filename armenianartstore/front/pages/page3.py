import streamlit as st
from styles.style import *  # Import utility functions for generating HTML and CSS
import base64
import os
import logging
from os.path import splitext, basename
from utils import create_user_choose_bandit, get_report
from config import PROJECT_ID

# Set page configuration
st.set_page_config(page_title="Armenian Art Gallery and Store", layout="wide")

# Define base directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Directory of the current file

# Go up one level to the project root
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Define paths relative to the project root
IMAGES_DIR = os.path.join(PROJECT_DIR, "images")
SPECIAL_OFFERS_DIR = os.path.join(IMAGES_DIR, "special_offer")
CATALOG_DIR = os.path.join(IMAGES_DIR, "art_catalog")
FOOTER_DIR = os.path.join(IMAGES_DIR, "footer")
BACKGROUND_DIR = os.path.join(IMAGES_DIR, "background")
STYLES_DIR = os.path.join(PROJECT_DIR, "styles")

# Get the script name
SCRIPT_NAME = os.path.splitext(os.path.basename(__file__))[0]

# Desired project ID
#PROJECT_ID = 1

# Generate dynamic mapping for only one bandit for this page
def map_bandit_for_page(project_id, script_name):
    """
    Matches the script name to its corresponding bandit and returns the mapping.

    Args:
    - project_id (str): Unique identifier for the project.
    - script_name (str): Name of the current script.

    Returns:
    - dict: Mapping of bandit ID to the script name.

    Raises:
    - ValueError: If no match is found for the script name in the bandit report.
    """
    report = get_report(project_id)

    for row in report.to_dict(orient="records"):
        # Match this script to its corresponding bandit
        if row["bandit_name"] == script_name:
            return {row["bandit_id"]: script_name}

    # If no match is found after checking all rows, raise an error
    raise ValueError(f"Please enter bandit name as: {SCRIPT_NAME.rstrip('0123456789')}") 

# Generate the mapping for this page
bandit_mapping = map_bandit_for_page(PROJECT_ID, SCRIPT_NAME)
script_name = list(bandit_mapping.values())[0]

# Set the background image
background_file = os.path.join(BACKGROUND_DIR, "background1.png")
st.markdown(generate_background_style(background_file), unsafe_allow_html=True)

# Function to apply external CSS
def apply_css():
    """
    Reads and applies external CSS for styling the Streamlit app.

    Raises:
    - FileNotFoundError: If the CSS file does not exist at the specified path.
    """
    css_path = os.path.join(STYLES_DIR, "style1.css")
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main function to render the app
def main():
    """
    Renders the entire Streamlit app, including header, special offers, catalog, and footer sections.
    """
    # Apply CSS for additional styling
    apply_css()

    # Header Section
    with st.container():
        # Define two columns for header layout
        col1, col2 = st.columns([2, 1])
        with col1:
            # Display the title
            st.markdown("<h1 class='montserrat-title'>Armenian Art<br>Gallery and Store</h1>", unsafe_allow_html=True)

        # Buttons and search box on the right
        with col2:
            # Create extra columns for button alignment
            left_col, button_col = st.columns([4, 2])

            with button_col:
                # Buttons for navigation
                if st.button("Go to Catalog", key="button1"):
                    create_user_choose_bandit(script_name, True, PROJECT_ID)
                if st.button("Not Interested", key="button2"):
                    create_user_choose_bandit(script_name, False, PROJECT_ID)

    # Convert images to Base64 for the Special Offers section
    special_offer_img1 = get_base64_of_bin_file(os.path.join(SPECIAL_OFFERS_DIR, "special_offer1.jpeg"))
    special_offer_img2 = get_base64_of_bin_file(os.path.join(SPECIAL_OFFERS_DIR, "special_offer2.jpeg"))
    special_offer_img3 = get_base64_of_bin_file(os.path.join(SPECIAL_OFFERS_DIR, "special_offer3.jpeg"))

    # Get the Special Offers HTML
    special_offers_html = get_special_offers_html(special_offer_img1, special_offer_img2, special_offer_img3)
    # Render the Special Offers section
    st.markdown(special_offers_html, unsafe_allow_html=True)

    # Convert images to Base64 for the Catalog section
    catalog_img1 = get_base64_of_bin_file(os.path.join(CATALOG_DIR, "catalog1.jpeg"))
    catalog_img2 = get_base64_of_bin_file(os.path.join(CATALOG_DIR, "catalog2.jpeg"))
    catalog_img3 = get_base64_of_bin_file(os.path.join(CATALOG_DIR, "catalog3.jpeg"))
    catalog_img4 = get_base64_of_bin_file(os.path.join(CATALOG_DIR, "catalog4.jpeg"))

    # Get the Catalog HTML
    art_catalog_hml = get_art_catalog_hml(catalog_img1, catalog_img2, catalog_img3, catalog_img4)
    # Render the Catalog section
    st.markdown(art_catalog_hml, unsafe_allow_html=True)

    # Footer Section
    # Convert the footer icons image to Base64
    social_icons_img = get_base64_of_bin_file(os.path.join(FOOTER_DIR, "social1.png"))
    
    # Get the Footer HTML
    footer_hml = get_footer_hml(social_icons_img)
    # Render the Footer section
    st.markdown(footer_hml, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()