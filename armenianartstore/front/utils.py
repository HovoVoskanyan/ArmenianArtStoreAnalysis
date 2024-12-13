import requests
import os
import pandas as pd

api_url = os.getenv("API_URL", "http://back:8000")




def create_project(project_description: str, bandit_name: str, bandit_qt: int) -> pd.DataFrame:
    payload = {
        "project_description": project_description,
        "bandits": {
            "name": bandit_name,
            "qt": bandit_qt
        }
    }

    response = requests.post(f"{api_url}/project", json=payload)

    if response.status_code == 200:
        data = response.json()
        # Convert the "bandits" list to a DataFrame
        df = pd.DataFrame(data["bandits"])
        return df
    else:
        raise ValueError(f"Failed to create project. Status code: {response.status_code}")

# # # Example usage
df_create_new_project = create_project("Astx", "page", 3)
print(df_create_new_project)

def get_champion(project_id:int):
    url = f"{api_url}/bandit/{project_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise ValueError(f"Project with ID {project_id} not found: {response.status_code}")

# champion = get_champion(project_id = 75)
# print(champion)

def create_user_choose_bandit(bandit_name: str, chosen: bool, project_id:int) -> dict:
    payload = {
        "bandit_name": bandit_name,
        "chosen": chosen,
        "project_id": project_id
    }

    response = requests.put(f"{api_url}/user/bandit", json=payload)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame.from_dict(data, orient='index').T
        return df.to_string(header=True, index=False)
    else:
        raise ValueError(f"Failed to submit user choice. Status code: {response.status_code}")

# choice = create_user_choice("page1", True, 75)
# print(choice)

def get_projects():
    url = f"{api_url}/projects"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['data'])
        return df

df_projects = get_projects()
print(df_projects)

def get_report(project_id:int):
    url = f"{api_url}/project/report/{project_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['bandits_report'])
        return df

df_report = get_report(project_id = 75)
print(df_report)



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


# Example usage of the function
PROJECT_ID = 75

# Fetch bandits
bandits = fetch_real_bandits(PROJECT_ID)

# Print the fetched bandits
if bandits:
    print("Fetched Bandit Data:")
    for bandit in bandits:
        print(bandit)
else:
    print("No bandit data found.")


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

projects =fetch_project_ids()

# Print the fetched bandits
if projects:
    print("Fetched Bandit Data:")
    for project in projects:
        print(project)
else:
    print("No bandit data found.")