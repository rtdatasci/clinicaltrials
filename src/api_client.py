import requests
import pandas as pd

BASE_URL = "https://clinicaltrials.gov/data-api/api/v1/studies"

def fetch_study_info(study_id):
    """
    Fetch study information from ClinicalTrials.gov API using a study ID.
    """
    url = f"{BASE_URL}/{study_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}, {response.text}")

def format_study_info(study_data):
    """
    Extract relevant fields and format as a DataFrame for tabular output.
    """
    # Example: Extract key fields (adjust based on API response)
    fields = {
        "Study ID": study_data.get("studyId", ""),
        "Title": study_data.get("title", ""),
        "Condition": study_data.get("condition", ""),
        "Status": study_data.get("status", ""),
        "Start Date": study_data.get("startDate", ""),
        "Completion Date": study_data.get("completionDate", "")
    }
    return pd.DataFrame([fields])

if __name__ == "__main__":
    study_id = "BP28248"  # Example study ID
    try:
        study_info = fetch_study_info(study_id)
        study_table = format_study_info(study_info)
        print(study_table)
    except Exception as e:
        print(f"Error: {e}")
