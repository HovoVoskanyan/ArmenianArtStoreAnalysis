import requests
import os
import pandas as pd

api_url = os.getenv("API_URL", "http://back:8000")

def create_project(project_description: str, bandit_name: str, bandit_qt: int) -> pd.DataFrame:
    """
    Creates a new project with the specified description and bandit configuration.

    Args:
    - project_description (str): A description for the project.
    - bandit_name (str): The name of the bandit.
    - bandit_qt (int): The quantity of the bandit.

    Returns:
    - pd.DataFrame: A DataFrame containing the details of the created bandits.

    Raises:
    - ValueError: If the API request fails, an error with the status code is raised.
    """
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

# Example usage
df_create_new_project = create_project("Test Project", "page", 3)
print(df_create_new_project)

def get_champion(project_id:int):
    """
    Retrieves the champion bandit for a given project.

    Args:
    - project_id (int): The ID of the project.

    Returns:
    - list: A list of champion bandit names.

    Raises:
    - ValueError: If the project is not found or the API request fails.
    """
    url = f"{api_url}/bandit/{project_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame([data])
        return df['name'].tolist()
    else:
        raise ValueError(f"Project with ID {project_id} not found: {response.status_code}")

# champion = get_champion(project_id = 1)
# print(champion)

def create_user_choose_bandit(bandit_name: str, chosen: bool, project_id:int) -> dict:
    """
    Submits a user's choice for a specific bandit.

    Args:
    - bandit_name (str): The name of the bandit chosen by the user.
    - chosen (bool): Whether the bandit was chosen (True) or not (False).
    - project_id (int): The ID of the project.

    Returns:
    - str: A formatted string representation of the updated data.

    Raises:
    - ValueError: If the API request fails.
    """
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

# choice = create_user_choose_bandit("page1", True, 1)
# print(choice)

def get_projects():
    """
    Fetches all available projects.

    Returns:
    - pd.DataFrame: A DataFrame containing the project data.

    Raises:
    - ValueError: If the API request fails.
    """
    url = f"{api_url}/projects"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['data'])
        return df

# df_projects = get_projects()
# print(df_projects)

def get_report(project_id:int):
    """
    Fetches the report for a specific project, including bandit performance metrics.

    Args:
    - project_id (int): The ID of the project.

    Returns:
    - pd.DataFrame: A DataFrame containing the bandit report.

    Raises:
    - ValueError: If the API request fails.
    """
    url = f"{api_url}/project/report/{project_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['bandits_report'])
        return df

# df_report = get_report(project_id = 1)
# print(df_report)