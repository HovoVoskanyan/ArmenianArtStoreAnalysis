import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.stats import beta
from utils import get_projects, get_report, create_project, set_project_id  # Import the functions to fetch data
 
# Function to fetch bandit data from the backend
def fetch_real_bandits(project_id):
    try:
        # Fetch the report from the backend
        df_bandits = get_report(project_id=project_id)

        # Create a list of dictionaries for bandits from the DataFrame
        bandits = [
            {"bandit_id": row['bandit_id'], "alpha": row['alpha'], "beta": row['beta']}
            for _, row in df_bandits.iterrows()
        ]
        return bandits
    except Exception as e:
        st.error(f"Failed to fetch bandit data: {e}")
        return []

# Function to fetch available project IDs
def fetch_project_ids():
    """
    Fetches all project IDs and descriptions from the backend.

    Returns:
    - List of tuples containing project ID and description.
    """
    try:
        df_projects = get_projects()
        # Extract project IDs and descriptions
        project_options = [(row['project_id'], row['project_description']) for _, row in df_projects.iterrows()]
        return project_options
    except Exception as e:
        st.error(f"Failed to fetch projects: {e}")
        return []

# Function to generate the beta distribution plot using Plotly
def generate_bandit_plot(bandits):
    """
    Generates a beta distribution plot for the given bandits using Plotly and displays it in a Streamlit app.

    Parameters:
    - bandits (list): List of dictionaries containing alpha and beta values.
    """
    if not bandits:  # Handle case where no bandits are provided
        st.error("No bandits provided!")
        return

    # Initialize the Plotly figure
    fig = go.Figure()
    
    x = np.linspace(0, 1, 200)

    # Iterate through the list of bandits to plot their beta distributions
    for bandit in bandits:
        alpha = bandit['alpha']  # Get alpha value for the bandit
        beta = bandit['beta']    # Get beta value for the bandit
        bandit_id = bandit['bandit_id']  # Get bandit ID

        # Special case for alpha = beta = 1 (uniform distribution)
        if alpha == 1 and beta == 1:
            y = np.ones_like(x)  # Uniform horizontal line
        else:
            # Compute the beta probability density function (PDF)
            y = beta_dist.pdf(x, alpha, beta)

        # Add a line trace for the beta distribution
        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                mode="lines",
                name=f"Bandit {bandit_id} (α={alpha}, β={beta})",
                hoverinfo="x+y+name"
            )
        )

    # Update layout for the plot
    fig.update_layout(
        xaxis_title="Probability",
        yaxis_title="Density",
        legend_title="Bandits",
        template="plotly_white",
    )

    # Render the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Main application logic
def main():
    # Streamlit title for the section
    st.title("Beta Distributions of Bandits")
    
    st.title("Project Selection")

    # Fetch project options dynamically
    project_options = fetch_project_ids()

    # Handle empty project options
    if not project_options:
        st.warning("No projects available.")
        return

    # Create a dropdown with project descriptions
    selected_project = st.selectbox(
        "Select a Project",
        options=project_options,
        format_func=lambda x: f"{x[1]} (ID: {x[0]})",  # Display project description and ID
    )

    if selected_project:
        project_id = selected_project[0]  # Extract selected project ID

        # Fetch and display bandit data
        bandits = fetch_real_bandits(project_id)
        if bandits:
            generate_bandit_plot(bandits)

# Run the application
if __name__ == "__main__":
    main()
