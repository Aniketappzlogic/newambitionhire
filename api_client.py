import requests
from config_api import CREDENTIALS
import time

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
        start_time = time.time()

        # Make the POST request
        response = requests.post(url, params=params, headers=headers)

        # Calculate the response time in milliseconds
        response_time = (time.time() - start_time) * 1000  # in milliseconds

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            # Print the desired output format
            print(f"POST {url}")
            print(f"{response.status_code}")
            print(f"{round(response_time, 2)} ms")
            print("Network")
            print("\nRequest Headers:")
            for key, value in headers.items():
                print(f"{key}: {value}")
            print("\nResponse Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            print("\nResponse Body:")
            print(response.json())

            # Extract the token and return the data
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
        start_time = time.time()

        # Send the GET request
        response = requests.get(url, headers=headers)

        # Calculate the response time
        response_time = (time.time() - start_time) * 1000  # in milliseconds

        if response.status_code == 200:
            # Print the desired format:
            print(f"GET {url}")
            print(f"{response.status_code}")
            print(f"{round(response_time, 2)} ms")
            print("Network")
            print("\nRequest Headers:")
            for key, value in headers.items():
                print(f"{key}: {value}")
            print("\nResponse Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            print("\nResponse Body:")
            print(response.json())

            return response.json()
        else:
            response.raise_for_status()

    def get_jobs(self, active=True):
        if not self.token:
            raise Exception("Token is missing. Please login first.")
        url = f"{self.base_url}/v1/jobs/company-jobs?active={str(active).lower()}"
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
        start_time = time.time()

        # Send the GET request
        response = requests.get(url, headers=headers)

        # Calculate the response time
        response_time = (time.time() - start_time) * 1000  # in milliseconds

        if response.status_code == 200:
            # Print the desired format:
            print(f"GET {url}")
            print(f"{response.status_code}")
            print(f"{round(response_time, 2)} ms")
            print("Network")
            print("\nRequest Headers:")
            for key, value in headers.items():
                print(f"{key}: {value}")
            print("\nResponse Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            print("\nResponse Body:")
            print(response.json())

            return response.json()
        else:
            response.raise_for_status()

    def get_candidates(self):
        if not self.token:
            raise Exception("Token is missing. Please login first.")
        url = f"{self.base_url}/v1/jobs/candidates"
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
        start_time = time.time()

        # Send the GET request
        response = requests.get(url, headers=headers)

        # Calculate the response time
        response_time = (time.time() - start_time) * 1000  # in milliseconds

        if response.status_code == 200:
            # Print the desired format:
            print(f"GET {url}")
            print(f"{response.status_code}")
            print(f"{round(response_time, 2)} ms")
            print("Network")
            print("\nRequest Headers:")
            for key, value in headers.items():
                print(f"{key}: {value}")
            print("\nResponse Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            print("\nResponse Body:")
            print(response.json())

            return response.json()
        else:
            response.raise_for_status()

    def get_hiring_stats(self, year):
        if not self.token:
            raise Exception("Token is missing. Please login first.")
        url = f"{self.base_url}/v1/jobs/hiring-stats/?year={year}"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'referer': 'https://services-recruiter.ambitionhire.ai/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'token': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }
        start_time = time.time()

        # Send the GET request
        response = requests.get(url, headers=headers)

        # Calculate the response time
        response_time = (time.time() - start_time) * 1000  # in milliseconds

        if response.status_code == 200:
            # Print the desired format:
            print(f"GET {url}")
            print(f"{response.status_code}")
            print(f"{round(response_time, 2)} ms")
            print("Network")
            print("\nRequest Headers:")
            for key, value in headers.items():
                print(f"{key}: {value}")
            print("\nResponse Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            print("\nResponse Body:")
            print(response.json())

            return response.json()
        else:
            response.raise_for_status()

    def get_all_resume_parser(self):
        if not self.token:
            raise Exception("Token is missing. Please login first.")
        url = "https://prod-resume-parser-service.ambitionhire.ai/v1/all_resume_parser?client_name=Services"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'referer': 'https://services-recruiter.ambitionhire.ai/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'token': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }
        start_time = time.time()

        # Send the GET request
        response = requests.get(url, headers=headers)

        # Calculate the response time
        response_time = (time.time() - start_time) * 1000  # in milliseconds

        if response.status_code == 200:
            # Print the desired format:
            print(f"GET {url}")
            print(f"{response.status_code}")
            print(f"{round(response_time, 2)} ms")
            print("Network")
            print("\nRequest Headers:")
            for key, value in headers.items():
                print(f"{key}: {value}")
            print("\nResponse Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            print("\nResponse Body:")
            print(response.json())

            return response.json()
        else:
            response.raise_for_status()




    def get_candidate_invitation(self, page=1, limit=10):
        if not self.token:
            raise Exception("Token is missing. Please login first.")
        url = f"{self.batch_url}/get-batches?manual=true&page={page}&limit={limit}"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'referer': 'https://services-recruiter.ambitionhire.ai/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'token': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }
        start_time = time.time()

        # Send the GET request
        response = requests.get(url, headers=headers)

        # Calculate the response time
        response_time = (time.time() - start_time) * 1000  # in milliseconds

        if response.status_code == 200:
            # Print the desired format:
            print(f"GET {url}")
            print(f"{response.status_code}")
            print(f"{round(response_time, 2)} ms")
            print("Network")
            print("\nRequest Headers:")
            for key, value in headers.items():
                print(f"{key}: {value}")
            print("\nResponse Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            print("\nResponse Body:")
            print(response.json())

            return response.json()
        else:
            response.raise_for_status()



    def get_company_profile(self):
        if not self.token:
            raise Exception("Token is missing. Please login first.")
        url = f"{self.company_profile_url}/v1/company/profile"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'referer': 'https://services-recruiter.ambitionhire.ai/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'token': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }
        start_time = time.time()

        # Send the GET request
        response = requests.get(url, headers=headers)

        # Calculate the response time
        response_time = (time.time() - start_time) * 1000  # in milliseconds

        if response.status_code == 200:
            # Print the desired format:
            print(f"GET {url}")
            print(f"{response.status_code}")
            print(f"{round(response_time, 2)} ms")
            print("Network")
            print("\nRequest Headers:")
            for key, value in headers.items():
                print(f"{key}: {value}")
            print("\nResponse Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            print("\nResponse Body:")
            print(response.json())

            return response.json()
        else:
            response.raise_for_status()

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
        start_time = time.time()

        # Send the GET request
        response = requests.get(url, headers=headers)

        # Calculate the response time
        response_time = (time.time() - start_time) * 1000  # in milliseconds

        if response.status_code == 200:
            # Print the desired format:
            print(f"GET {url}")
            print(f"{response.status_code}")
            print(f"{round(response_time, 2)} ms")
            print("Network")
            print("\nRequest Headers:")
            for key, value in headers.items():
                print(f"{key}: {value}")
            print("\nResponse Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            print("\nResponse Body:")
            print(response.json())

            return response.json()
        else:
            response.raise_for_status()
