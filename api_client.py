import requests
from config_api import CREDENTIALS
class APIClient:
    def __init__(self):
        self.base_url = "https://prod-job-service.ambitionhire.ai"
        self.batch_url = "https://prod-batch-upload.ambitionhire.ai"
        self.company_profile_url = "https://prod-company-profile.ambitionhire.ai"
        self.token = None

    def login(self, email, password, client_name):
        url = "https://prod-auth-service.ambitionhire.ai/v1/auth_routes/recruiter-login/"
        params = {"email": email, "password": password, "client_name": client_name}
        headers = {
            'sec-ch-ua-platform': '"Windows"',
            'Referer': 'https://services-recruiter.ambitionhire.ai/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            'Accept': 'application/json',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'Content-Type': 'application/x-www-form-urlencoded',
            'sec-ch-ua-mobile': '?0',
        }
        response = requests.post(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            self.token = data.get("access_token")
            return data
        else:
            raise Exception(f"Login failed: {response.status_code}, {response.text}")

    def get_dashboard(self):
        if not self.token:
            raise Exception("Token is missing. Please login first.")
        url = f"{self.base_url}/v1/recruiter/dashboard"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'origin': 'https://services-recruiter.ambitionhire.ai',
            'referer': 'https://services-recruiter.ambitionhire.ai/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            'token': self.token,
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Dashboard API failed: {response.status_code}, {response.text}")

    def get_jobs(self, active=True):
        if not self.token:
            raise Exception("Token is missing. Please login first.")

        # URL for the 'company-jobs' endpoint
        url = f"{self.base_url}/v1/jobs/company-jobs?active={str(active).lower()}"

        # Headers to mimic the cURL request
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://services-recruiter.ambitionhire.ai',
            'priority': 'u=1, i',
            'referer': 'https://services-recruiter.ambitionhire.ai/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'token': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }

        # Make the GET request to the API endpoint
        response = requests.get(url, headers=headers)

        # Handle the response
        if response.status_code == 200:
            return response.json()  # Return the JSON response if successful
        else:
            raise Exception(f"API request failed: {response.status_code}, {response.text}")

    def get_candidates(self):
        if not self.token:
            raise Exception("Token is missing. Please login first.")

        # URL for the 'candidates' endpoint
        url = f"{self.base_url}/v1/jobs/candidates"

        # Headers to mimic the cURL request
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://services-recruiter.ambitionhire.ai',
            'priority': 'u=1, i',
            'referer': 'https://services-recruiter.ambitionhire.ai/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'token': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }

        # Make the GET request to the API endpoint
        response = requests.get(url, headers=headers)

        # Handle the response
        if response.status_code == 200:
            return response.json()  # Return the JSON response if successful
        else:
            raise Exception(f"API request failed: {response.status_code}, {response.text}")

    def get_hiring_stats(self, year):
        if not self.token:
            raise Exception("Token is missing. Please login first.")

        # URL for the 'hiring-stats' endpoint
        url = f"{self.base_url}/v1/jobs/hiring-stats/?year={year}"

        # Headers to mimic the cURL request
        headers = {
            'accept': 'application/json, text/plain, */*',
            'referer': 'https://services-recruiter.ambitionhire.ai/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'token': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }

        # Make the GET request to the API endpoint
        response = requests.get(url, headers=headers)

        # Handle the response
        if response.status_code == 200:
            return response.json()  # Return the JSON response if successful
        else:
            raise Exception(f"API request failed: {response.status_code}, {response.text}")

    def get_all_resume_parser(self):
        if not self.token:
            raise Exception("Token is missing. Please login first.")

        # URL for the 'all_resume_parser' endpoint
        url = "https://prod-resume-parser-service.ambitionhire.ai/v1/all_resume_parser?client_name=Services"

        # Headers to mimic the cURL request
        headers = {
            'accept': 'application/json, text/plain, */*',
            'referer': 'https://services-recruiter.ambitionhire.ai/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'token': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }

        # Make the GET request to the API endpoint
        response = requests.get(url, headers=headers)

        # Handle the response
        if response.status_code == 200:
            return response.json()  # Return the JSON response if successful
        else:
            raise Exception(f"API request failed: {response.status_code}, {response.text}")

    def get_candidate_invitation(self, page=1, limit=10):
        if not self.token:
            raise Exception("Token is missing. Please login first.")

        # URL for the 'get-batches' endpoint
        #https://prod-batch-upload.ambitionhire.ai/get-batches?manual=true&page=1&limit=10
        url = f"{self.batch_url}/get-batches?manual=true&page={page}&limit={limit}"

        # Headers to mimic the cURL request
        headers = {
            'accept': 'application/json, text/plain, */*',
            'referer': 'https://services-recruiter.ambitionhire.ai/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'token': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }

        # Make the GET request to the API endpoint
        response = requests.get(url, headers=headers)

        # Check for a successful response
        if response.status_code == 200:
            return response.json()  # Assuming the API returns JSON data
        else:
            response.raise_for_status()  # Raise an exception if the request failed

    def get_company_profile(self):
        if not self.token:
            raise Exception("Token is missing. Please login first.")

        # URL for the 'company-profile' endpoint
        url = f"{self.company_profile_url}/v1/company/profile"

        # Headers to mimic the cURL request
        headers = {
            'accept': 'application/json, text/plain, */*',
            'referer': 'https://services-recruiter.ambitionhire.ai/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'token': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }

        # Make the GET request to the API endpoint
        response = requests.get(url, headers=headers)

        # Check for a successful response
        if response.status_code == 200:
            return response.json()  # Assuming the API returns JSON data
        else:
            response.raise_for_status()  # Raise an exception if the request failed

    def get_role_based_access(self, client_name='Services'):
        if not self.token:
            raise Exception("Token is missing. Please login first.")

        url = "https://prod-auth-service.ambitionhire.ai/v1/roles/custom-roles/?client_name=Services"

        headers = {
            'accept': 'application/json, text/plain, */*',
            'referer': 'https://services-recruiter.ambitionhire.ai/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'token': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }

        # Make the GET request to the API endpoint
        response = requests.get(url, headers=headers)

        # Check for a successful response
        if response.status_code == 200:
            return response.json()  # Assuming the API returns JSON data
        else:
            response.raise_for_status()  # Raise an exception if the request failed