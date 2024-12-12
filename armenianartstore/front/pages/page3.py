"""
Streamlit Application for Armenian Art Gallery and Store.

This application provides an interactive user interface for showcasing Armenian art,
including special offers, a catalog of artworks, and a footer with contact details and 
promotional subscriptions. It uses external CSS for styling and dynamically loads 
content such as images and layouts.

Modules:
    - streamlit: For creating the web application interface.
    - os: For file and directory handling, including resolving relative paths.
    - base64: For encoding image files to Base64 format for embedding in HTML.

Features:
    - Header section with a title, navigation buttons, and a search box.
    - Special Offers section with dynamically loaded images and details.
    - Catalog section displaying a range of artworks with prices and details.
    - Footer section with contact information, a subscription box, and social media icons.
    - Uses external CSS for styling and Base64 encoding for embedding images.

Directory Structure:
    - styles/
        - Contains external CSS and helper functions for generating styles (e.g., `style1.css`).
    - images/
        - Contains images for special offers, catalog items, and footer icons.
    - pages/
        - Contains additional pages for multi-page navigation if integrated.
    - app.py
        - Main file to run the application.

Example Use Case:
    - Displays a visually appealing interface for an art gallery, providing users with a
      seamless experience to explore and interact with artwork, offers, and promotions.
"""

import streamlit as st
from styles.style import *  # Import utility functions for generating HTML and CSS
import base64
import os
import logging
from os.path import splitext, basename
from utils import create_user_choice, get_report

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
PROJECT_ID = 64

# Generate dynamic mapping for only one bandit for this page
def get_bandit_mapping_for_page(project_id, script_name):
    """
    Map the specific bandit to the current script based on its position.
    This ensures only one bandit is mapped to this page.
    """
    report = get_report(project_id)
    for i, row in enumerate(report.to_dict(orient="records"), start=1):
        # Match this script to its corresponding bandit
        if script_name == SCRIPT_NAME:
            return {row["bandit_name"]: script_name}
    return {}

# Generate the mapping for this page
bandit_mapping = get_bandit_mapping_for_page(PROJECT_ID, SCRIPT_NAME)
logging.debug(f"Bandit Mapping for {SCRIPT_NAME}: {bandit_mapping}")

# Debugging: Print the bandit mapping
print(f"Bandit Mapping for {SCRIPT_NAME}: {bandit_mapping}")

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
    try:
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        print(f"CSS file not found: {css_path}")

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
            #     if st.button("Go to Catalog", key="button1"):
            #         bandit_name = list(bandit_mapping.keys())[0]
            #         create_user_choice(bandit_name=bandit_name, chosen=True)
            #     if st.button("Not Interested", key="button2"):
            #         bandit_name = list(bandit_mapping.keys())[0]
            #         create_user_choice(bandit_name=bandit_name, chosen=False)
            # # Display the search box
            # st.markdown(get_search_box_html(), unsafe_allow_html=True)

                if st.button("Go to Catalog", key="button1"):
                    try:
                        bandit_name = list(bandit_mapping.keys())[0]
                        logging.debug(f"'Go to Catalog' clicked with bandit: {bandit_name}")
                        create_user_choice(bandit_name=bandit_name, chosen=True)
                    except IndexError:
                        logging.error("No bandit mapping available for 'Go to Catalog'.")
                if st.button("Not Interested", key="button2"):
                    try:
                        bandit_name = list(bandit_mapping.keys())[0]
                        logging.debug(f"'Not Interested' clicked with bandit: {bandit_name}")
                        create_user_choice(bandit_name=bandit_name, chosen=False)
                    except IndexError:
                        logging.error("No bandit mapping available for 'Not Interested'.")

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