Before running the automation tests, ensure you have the following installed:

Python 3.x - Install Python
Selenium - A web automation library.
Pytest - A testing framework that will run the test cases.

You can install the required dependencies via pip by running the following commands in your terminal:
pip install -r requirements.txt

To run the Automation tests use the folwing cmmand in the terminal 
e.g  pytest -m dashboard_page --env services --myBrowser chrome --html=report.html

This is an example command which will ruun the test marked as "dashboard_page" (you can change this marker according to your choice of test cases you want to run)
for --env you can select between " Services" or " Dev"
