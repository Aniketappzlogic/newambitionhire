import json
import logging
from datetime import time

import pytest
from api_client import APIClient
from config_api import CREDENTIALS

@pytest.fixture(scope="module")
def client():
    api_client = APIClient()
    api_client.login(
        email=CREDENTIALS["email"],
        password=CREDENTIALS["password"],
        client_name=CREDENTIALS["client_name"],
    )
    return api_client
@pytest.mark.APItest
def test_login(client):
    assert client.token is not None, "Login failed, token is missing."
    print(f"Access Token: {client.token}")

@pytest.mark.APItest
def test_dashboard(client):
    dashboard_data = client.get_dashboard()
    assert dashboard_data is not None, "Dashboard API returned no data."
    print("Dashboard Data:", dashboard_data)

@pytest.mark.APItest
def test_jobs(client):
    jobs_data = client.get_jobs()
    assert jobs_data is not None, "Jobs API returned no data."
    print("Jobs Data:", jobs_data)

@pytest.mark.APItest
def test_hiring_stats(client):
    hiring_data = client.get_hiring_stats(year=2024)
    assert hiring_data is not None, "Hiring API returned no data."
    print("Hiring Stats Data:", hiring_data)

@pytest.mark.APItest
def test_resume_parser(client):
    resume_parser_data = client.get_all_resume_parser()
    assert resume_parser_data is not None, "Resume Parser API returned no data."
    print("Resume Parser Data:", resume_parser_data)

@pytest.mark.APItest
def test_candidate_invitation(client):
    candidate_invitation_data = client.get_candidate_invitation(page=1,limit=10)
    assert candidate_invitation_data is not None, "Candidate Invitation API returned no data."
    print("Candidate Invitation Data:", candidate_invitation_data)

@pytest.mark.APItest
def test_company_profile(client):
    company_profile_data = client.get_company_profile()
    assert company_profile_data is not None, "Company Profile API returned no data."
    print("Company Profile Data: ", company_profile_data)

def test_role_based_access(client):
    role_based_access_data = client.get_role_based_access()
    assert role_based_access_data is not None, "Role Based API returned no data."
    print("Jobs Data: ", role_based_access_data)
