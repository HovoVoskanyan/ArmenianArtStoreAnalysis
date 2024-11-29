import streamlit as st
import base64

# Function to get base64 encoding of an image
@st.cache_data
def get_base64_of_bin_file(bin_file):
    """
    Encodes a binary file (e.g., an image) into a Base64 string.

    Parameters:
    - bin_file (str): The path to the binary file.

    Returns:
    - str: Base64 encoded string of the file contents.
    """
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")

# Function to generate the HTML for the background
def generate_background_style(bin_file):
    """
    Generates CSS to set a background image for the Streamlit app.

    Parameters:
    - bin_file (str): The path to the image file to use as the background.

    Returns:
    - str: HTML and CSS for setting the background image.
    """
    bin_str = get_base64_of_bin_file(bin_file)
    return f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    '''

# Function to generate the search box HTML
def get_search_box_html():
    """
    Returns the HTML for a search box component.

    Returns:
    - str: HTML for a search box.
    """
    return """
    <div class='search-box'>
        <input type='text' placeholder='Search authors, artworks, etc...' />
    </div>
    """

# Function to generate HTML for the "Special Offers" section
def get_special_offers_html(img1, img2, img3):
    """
    Generates the HTML for displaying a "Special Offers" section.

    Parameters:
    - img1, img2, img3 (str): Base64-encoded strings of the special offer images.

    Returns:
    - str: HTML for the "Special Offers" section.
    """
    return f"""
    <div class="special-content-section">
        <h2 class="section-title">Special Offers</h2>
        <div class="item-columns">
            <div style="display: flex; gap: 20px; justify-content: space-around;">
                <div style="flex: 1;">
                    <img src="data:image/jpeg;base64,{img1}" alt="What kind of man are you" style="width: 100%; border-radius: 10px;"/>
                    <div class="item-title">What kind of man are you, by Tigran Vardikyan</div>
                    <div class="item-price">35.00 $ - 6,000.00 $</div>
                </div>
                <div style="flex: 1;">
                    <img src="data:image/jpeg;base64,{img2}" alt="An Arrested Dream" style="width: 100%; border-radius: 10px;"/>
                    <div class="item-title">An Arrested Dream, by Tigran Vardikyan</div>
                    <div class="item-price">35.00 $ - 2,400.00 $</div>
                </div>
                <div style="flex: 1;">
                    <img src="data:image/jpeg;base64,{img3}" alt="Bird Hunter" style="width: 100%; border-radius: 10px;"/>
                    <div class="item-title">Bird Hunter, by Tigran Vardikyan</div>
                    <div class="item-price">35.00 $ - 1,800.00 $</div>
                </div>
            </div>
        </div>
    </div>
    """

# Function to generate HTML for the "Catalog of Art Works" section
def get_art_catalog_hml(img1, img2, img3, img4):
    """
    Generates the HTML for displaying the "Catalog of Art Works" section.

    Parameters:
    - img1, img2, img3, img4 (str): Base64-encoded strings of the catalog images.

    Returns:
    - str: HTML for the "Catalog of Art Works" section.
    """
    return f"""
    <div class="catalog-content-section">
        <h2 class="section-title">Catalog of Art Works</h2>
        <div style="display: flex; gap: 10px; justify-content: space-around;">
            <div style="flex: 1;">
                <img src="data:image/jpeg;base64,{img1}" style="width: 100%; border-radius: 10px;" />
                <div class="item-title">Aghavnadzor, watercolor painting by Eduard Nersesyan</div>
                <div class="item-price">420.00 $</div>
                <div class="button-row">
                    <span style="cursor: pointer; text-decoration: none;">Add to cart</span> |
                    <span style="cursor: pointer; text-decoration: none;">Details</span>
                </div>
            </div>
            <div style="flex: 1;">
                <img src="data:image/jpeg;base64,{img2}" style="width: 100%; border-radius: 10px;" />
                <div class="item-title">Eternal Temptation, oil painting by Tigran Vardikyan</div>
                <div class="item-price">4,500.00 $</div>
                <div class="button-row">
                    <span style="cursor: pointer; text-decoration: none;">Add to cart</span> |
                    <span style="cursor: pointer; text-decoration: none;">Details</span>
                </div>
            </div>
            <div style="flex: 1;">
                <img src="data:image/jpeg;base64,{img3}" style="width: 100%; border-radius: 10px;" />
                <div class="item-title">Still Life Pomegranates, oil painting by Arman Asatryan</div>
                <div class="item-price">4,600.00 $</div>
                <div class="button-row">
                    <span style="cursor: pointer; text-decoration: none;">Add to cart</span> |
                    <span style="cursor: pointer; text-decoration: none;">Details</span>
                </div>
            </div>
            <div style="flex: 1;">
                <img src="data:image/jpeg;base64,{img4}" style="width: 100%; border-radius: 10px;" />
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

# Function to generate the HTML for the footer
def get_footer_hml(img1):
    """
    Generates the HTML for displaying the footer section.

    Parameters:
    - img1 (str): Base64-encoded string of the social icons image.

    Returns:
    - str: HTML for the footer section.
    """
    return f"""
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
                    <img src="data:image/png;base64,{img1}" alt="Social Icons" />
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
        """