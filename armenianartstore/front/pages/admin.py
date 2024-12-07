"""
Streamlit Application for Beta Distribution Visualization in Multi-Armed Bandit Problem.

This application simulates a multi-armed bandit scenario, visualizing the beta distributions
for a set of bandits. Each bandit represents a potential action with success and failure
parameters (α and β), which are updated dynamically in real-world scenarios. The application
uses Streamlit to display the beta distributions in an interactive web interface.

Modules:
    - streamlit: For creating the web application interface.
    - numpy: For generating a range of values to calculate the beta distribution.
    - scipy.stats: For calculating the beta probability density function.
    - matplotlib: For plotting the beta distributions.

Components:
    - MockBandit: A class representing a single bandit with associated beta distribution parameters.
    - generate_bandit_plot: A function to generate and display the beta distribution plot for the bandits.

Features:
    - Visualize beta distributions for a set of bandits.
    - Customize the alpha (successes + 1) and beta (failures + 1) parameters for each bandit.
    - Interactive interface with Streamlit for displaying plots and handling user interactions.

Directory Structure:
    - app/
        - Contains the Streamlit application files.
    - utils/
        - Contains helper functions or classes if needed (e.g., for more complex multi-armed bandit logic).

Example Use Case:
    - Run the application to visualize how the probabilities for each bandit evolve as the success
      and failure counts change in a multi-armed bandit experiment.
"""

import streamlit as st
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

# Define the MockBandit class
class MockBandit:
    """
    Represents a bandit in the multi-armed bandit problem.

    Attributes:
    - bandit_id (int): Unique identifier for the bandit.
    - alpha (float): The alpha parameter of the beta distribution.
    - beta (float): The beta parameter of the beta distribution.
    """

    def __init__(self, bandit_id, alpha, beta):
        """
        Initializes a MockBandit instance.

        Parameters:
        - bandit_id (int): The unique ID of the bandit.
        - alpha (float): Initial value of alpha (successes + 1).
        - beta (float): Initial value of beta (failures + 1).
        """
        self.bandit_id = bandit_id
        self.alpha = alpha
        self.beta = beta


# Create mock bandits
mock_bandits = [
    MockBandit(bandit_id=1, alpha=2, beta=5),  # Bandit with α=2, β=5
    MockBandit(bandit_id=2, alpha=3, beta=2),  # Bandit with α=3, β=2
    MockBandit(bandit_id=3, alpha=1, beta=1)   # Bandit with α=1, β=1
]

# Function to generate the beta distribution plot
def generate_bandit_plot(bandits):
    """
    Generates a beta distribution plot for the given bandits and displays it in a Streamlit app.

    Parameters:
    - bandits (list): List of MockBandit objects containing alpha and beta values.

    Behavior:
    - If no bandits are provided, displays an error message in the Streamlit app.
    - Generates a plot for the beta distributions of all provided bandits and
      displays it in the Streamlit app.
    """
    if not bandits:  # Handle case where no bandits are provided
        st.error("No bandits provided!")
        return

    # Streamlit title for the section
    st.title("Beta Distributions of Bandits")

    # Create a Matplotlib figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Iterate through the list of bandits to plot their beta distributions
    for bandit in bandits:
        alpha = bandit.alpha  # Get alpha value for the bandit
        beta = bandit.beta    # Get beta value for the bandit

        # Generate a range of x values between 0 and 1
        x = np.linspace(0, 1, 1000)

        # Compute the beta probability density function (PDF)
        y = scipy.stats.beta.pdf(x, alpha, beta)

        # Plot the beta distribution on the axes
        ax.plot(x, y, label=f"Bandit {bandit.bandit_id} (α={alpha}, β={beta})")

    # Add labels and legend to the plot
    ax.set_title("Beta Distributions of Bandits")  # Title of the plot
    ax.set_xlabel("Probability")  # Label for the x-axis
    ax.set_ylabel("Density")      # Label for the y-axis
    ax.legend()                   # Add legend to the plot

    # Render the plot in Streamlit
    st.pyplot(fig)

# Call the function with mock data
generate_bandit_plot(mock_bandits)