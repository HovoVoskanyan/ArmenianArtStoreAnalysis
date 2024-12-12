import requests
import os
import pandas as pd

api_url = os.getenv("API_URL", "http://back:8000")

# def create_project(project_description: str, bandit_names: list) -> dict:
#     payload = {
#         "project_description": project_description,
#         "bandits": [{"name": name} for name in bandit_names]
#     }

#     response = requests.post(f"{api_url}/project", json=payload)

#     if response.status_code == 200:
#         data = response.json()
#         # Convert the "bandits" list to a DataFrame
#         df = pd.DataFrame(data["bandits"])
#         return df
#     else:
#         raise ValueError(f"Failed to create project. Status code: {response.status_code}")

# df_create_new_project = create_project("hi", ["Bandit1", "Bandit2", "Bandit3"])
# print(df_create_new_project)

# def create_project(project_description: str, bandit: dict) -> dict:

#     payload = {
#         "project_description": project_description,
#         "bandits": bandit 
#     }

#     response = requests.post(f"{api_url}/project", json=payload)

#     if response.status_code == 200:
#         data = response.json()

#         df = pd.DataFrame(data["project_id", 
#                                 "start_date", 
#                                 "project_description", 
#                                 "bandits_qty", 
#                                 "bandits"])
#         return df
#     else:
#         raise ValueError(f"Failed to create project. Status code: {response.status_code}, Error: {error_details}")


# project_response = create_project(project_description = "My New Projectmmmm", bandit = {"name": "page", "qt": 3})
# print(project_response)

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
# df_create_new_project = create_project("Astx", "bandit", 3)
# print(df_create_new_project)

def get_champion(project_id:int):
    url = f"{api_url}/bandit/{project_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise ValueError(f"Project with ID {project_id} not found: {response.status_code}")

# champion = get_champion(project_id = 60)
# print(champion)

def create_user_choice(bandit_name: str, chosen: bool) -> dict:
    payload = {
        "bandit_name": bandit_name,
        "chosen": chosen
    }

    response = requests.post(f"{api_url}/user/bandit", json=payload)

    if response.status_code == 200:
        data = response.json()
        print(data)
        df = pd.DataFrame.from_dict(data, orient='index').T
        return df.to_string(header=True, index=False)
    else:
        raise ValueError(f"Failed to submit user choice. Status code: {response.status_code}")

choice = create_user_choice("bandit1", True)
print(choice)

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

df_report = get_report(project_id = 64)
print(df_report)

# if __name__ == "__main__":
#     import os
#     from os.path import splitext, basename
#     print(splitext(basename(__file__))[0])


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

# Debugging: Print the bandit mapping
print(f"Bandit Mapping for {SCRIPT_NAME}: {bandit_mapping}")