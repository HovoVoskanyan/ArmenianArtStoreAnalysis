import streamlit as st
import base64
import os

# Set up page configuration
st.set_page_config(page_title="Armenian Art Gallery and Store", layout="wide")

# Paths
BASE_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(BASE_DIR, "images")
SPECIAL_OFFERS_DIR = os.path.join(IMAGES_DIR, "special_offer")
CATALOG_DIR = os.path.join(IMAGES_DIR, "art_catalog")
FOOTER_DIR = os.path.join(IMAGES_DIR, "footer")
BACKGROUND_DIR = os.path.join(IMAGES_DIR, "background")
STYLES_DIR = os.path.join(BASE_DIR, "styles")

# Function to get base64 encoding of an image
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")

# Function to set the background image
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to apply external CSS
def apply_css():
    css_path = os.path.join(STYLES_DIR, "style2.css")
    try:
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        print(f"CSS file not found: {css_path}")

# Set the background image
set_png_as_page_bg(os.path.join(BACKGROUND_DIR, "background2.png"))


def main():
    apply_css()

    # Header Section
    with st.container():
        col1, col2 = st.columns([3, 1])  
        with col1:
            st.markdown("<h1 class='montserrat-title'>Armenian Art<br>Gallery and Store</h1>", unsafe_allow_html=True)
            st.markdown(
                """
                <div class='search-box'>
                    <input type='text' placeholder='Search authors, artworks, etc...' />
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                """
                <div class='right-menu'>   
                    <div>Basket</div>
                    <div>Catalog</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Convert images to Base64 for Special Offers / tried with for loop but not working in this case
    special_offer_img1 = get_base64_of_bin_file(os.path.join(SPECIAL_OFFERS_DIR, "special_offer1.jpeg"))
    special_offer_img2 = get_base64_of_bin_file(os.path.join(SPECIAL_OFFERS_DIR, "special_offer2.jpeg"))
    special_offer_img3 = get_base64_of_bin_file(os.path.join(SPECIAL_OFFERS_DIR, "special_offer3.jpeg"))

    # Special Offers Section
    special_offers_html = f"""
    <div class="special-content-section">
        <h2 class="section-title">Special Offers</h2>
        <div class="item-columns">
            <div style="display: flex; gap: 20px; justify-content: space-around;">
                <div style="flex: 1;">
                    <img src="data:image/jpeg;base64,{special_offer_img1}" alt="What kind of man are you" style="width: 100%; border-radius: 10px;"/>
                    <div class="item-title">What kind of man are you, by Tigran Vardikyan</div>
                    <div class="item-price">35.00 $ - 6,000.00 $</div>
                </div>
                <div style="flex: 1;">
                    <img src="data:image/jpeg;base64,{special_offer_img2}" alt="An Arrested Dream" style="width: 100%; border-radius: 10px;"/>
                    <div class="item-title">An Arrested Dream, by Tigran Vardikyan</div>
                    <div class="item-price">35.00 $ - 2,400.00 $</div>
                </div>
                <div style="flex: 1;">
                    <img src="data:image/jpeg;base64,{special_offer_img3}" alt="Bird Hunter" style="width: 100%; border-radius: 10px;"/>
                    <div class="item-title">Bird Hunter, by Tigran Vardikyan</div>
                    <div class="item-price">35.00 $ - 1,800.00 $</div>
                </div>
            </div>
        </div>
    </div>
    """
    # Render the HTML for the special offers section
    st.markdown(special_offers_html, unsafe_allow_html=True)

    # Convert images to Base64 for Catalog / tried with for loop but not working in this case
    catalog_img1 = get_base64_of_bin_file(os.path.join(CATALOG_DIR, "catalog1.jpeg"))
    catalog_img2 = get_base64_of_bin_file(os.path.join(CATALOG_DIR, "catalog2.jpeg"))
    catalog_img3 = get_base64_of_bin_file(os.path.join(CATALOG_DIR, "catalog3.jpeg"))
    catalog_img4 = get_base64_of_bin_file(os.path.join(CATALOG_DIR, "catalog4.jpeg"))

    # Catalog of Art Works Section 
    art_catalog_hml = f"""
    <div class="catalog-content-section">
        <h2 class="section-title">Catalog of Art Works</h2>
        <div style="display: flex; gap: 10px; justify-content: space-around;">
            <div style="flex: 1;">
                <img src="data:image/jpeg;base64,{catalog_img1}" style="width: 100%; border-radius: 10px;" />
                <div class="item-title">Aghavnadzor, watercolor painting by Eduard Nersesyan</div>
                <div class="item-price">420.00 $</div>
                <div class="button-row">
                    <span style="cursor: pointer; text-decoration: none;">Add to cart</span> |
                    <span style="cursor: pointer; text-decoration: none;">Details</span>
                </div>
            </div>
            <div style="flex: 1;">
                <img src="data:image/jpeg;base64,{catalog_img2}" style="width: 100%; border-radius: 10px;" />
                <div class="item-title">Eternal Temptation, oil painting by Tigran Vardikyan</div>
                <div class="item-price">4,500.00 $</div>
                <div class="button-row">
                    <span style="cursor: pointer; text-decoration: none;">Add to cart</span> |
                    <span style="cursor: pointer; text-decoration: none;">Details</span>
                </div>
            </div>
            <div style="flex: 1;">
                <img src="data:image/jpeg;base64,{catalog_img3}" style="width: 100%; border-radius: 10px;" />
                <div class="item-title">Still Life Pomegranates, oil painting by Arman Asatryan</div>
                <div class="item-price">4,600.00 $</div>
                <div class="button-row">
                    <span style="cursor: pointer; text-decoration: none;">Add to cart</span> |
                    <span style="cursor: pointer; text-decoration: none;">Details</span>
                </div>
            </div>
            <div style="flex: 1;">
                <img src="data:image/jpeg;base64,{catalog_img4}" style="width: 100%; border-radius: 10px;" />
                <div class="item-title">Berlin, ink, watercolor painting by Anahit Samvelyan</div>
                <div class="item-price">132.00 $</div>
                <div class="button-row">
                    <span style="cursor: pointer; text-decoration: none;">Add to cart</span> |
                    <span style="cursor: pointer; text-decoration: none;">Details</span>
                </div>
            </div>
        </div>
    </div>
"""
    st.markdown(art_catalog_hml, unsafe_allow_html=True)

    # Add the "Go to the Catalog" button
    st.markdown(
        """
        <div style="text-align: left; margin-top: 15px; margin-bottom: 5px;">
            <a href="#catalog" style="
                font-family: 'Montserrat', sans-serif;
                font-size: 13px;
                color: white;
                text-decoration: none;
                padding: 10px 13px;
                border: 1px solid white;
                border-radius: 20px;
                display: inline-block;
            ">
                Go to the Catalog
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Footer Section
    social_icons_img = os.path.join(FOOTER_DIR, "social1.png")
    st.markdown(
        f"""
        <div class='footer'>
            <div class='section'>
                <h3>Armenian Art<br>Gallery and Store</h3>
            </div>
            <div class='section'>
                <h3>Menu</h3>
                <p>Main</p>
                <p>Catalog</p>
                <p>Basket</p>
            </div>
            <div class='section'>
                <h3>Contacts</h3>
                <p>+7 908 800 80 80</p>
                <p>help@nkar.com</p>
                <div class='social-icons'>
                    <img src="data:image/png;base64,{get_base64_of_bin_file(social_icons_img)}" alt="Social Icons" />
                </div>
            </div>
            <div class='section'>
                <h3>Get notified about promotions</h3>
                <div class='subscribe-box'>
                    <input type='email' placeholder='Email Address'/>
                    <button>Sign Up</button>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()