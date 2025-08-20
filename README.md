Holistiplan Rewards Application - QA Homework
This repository contains the manual and automated testing documentation for the Holistiplan Rewards Application, along with the Playwright Python automation suite.

Project Structure
.
├── .gitignore                           <- Files/folders Git should ignore
├── README.md                           <- This project overview file
├── manual_testing_documentation.md     <- Report on manual testing findings
├── automated_testing_documentation.md  <- Report on automated testing results
└── qa_homework/                        <- The Holistiplan application code
    ├── docker-compose.yml              <- Docker configuration for the app
    ├── .env.local                      <- Environment variables for the app
    ├── pyproject.toml                  <- Pytest configuration for the app
    ├── test_rewards_app.py             <- Playwright Python automated tests
    └── ... (other original project files)

Setup Instructions (First Time)
Follow these steps to get the Holistiplan Rewards Application and the testing environment set up on your local machine.

1. Prerequisites
Before you start, ensure you have the following installed:

Docker Desktop: Essential for running the Holistiplan application locally. Download from docker.com/products/docker-desktop.

Python 3.8+: Required for running the automated tests. On macOS, Homebrew is recommended for Python installation.

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python

After installing Python, open a new Terminal window to ensure your system's PATH is updated.
Verify installation: python3 --version and pip3 --version

2. Clone or Download the Project
Using Git (Recommended):

git clone https://github.com/ocrfin/qa_homework.git # Replace with your actual repo URL if different

Then, navigate into the cloned directory (this will be your repository's root):

cd Your_Repo_Name # Replace with the name you gave your GitHub repo

Downloading as ZIP:

Go to your GitHub repository page (e.g., https://github.com/YOUR_USERNAME/YOUR_REPO_NAME).

Click the green Code button and select Download ZIP.

Unzip the downloaded file. This will create a folder (e.g., Your_Repo_Name-main).

Navigate into this folder:

cd path/to/Your_Repo_Name-main

3. Install Playwright and Pytest-Playwright
These libraries are necessary to execute your automated web tests. Ensure your terminal is in the root of your repository.

pip3 install pytest playwright pytest-playwright Django # Django is needed for test collection
playwright install

4. Create .env.local File
The Holistiplan application requires an environment file for its configuration. This file contains sensitive information and is ignored by Git (.gitignore).

Navigate into the qa_homework directory inside your repository's root.

cd qa_homework

Create a new file named .env.local in this qa_homework directory.

Add the following content to .env.local:

# The Django secret key is used for cryptographic signing.
# It's crucial for security; do NOT share this or commit to public repositories.
SECRET_KEY=a_very_secret_key_that_you_should_change_for_production_if_this_were_a_real_app

# Set Django's debug mode. 'True' for development, 'False' for production.
DJANGO_DEBUG=True

# Allowed hosts for Django. '*' allows all hosts; for production, list specific domains.
DJANGO_ALLOWED_HOSTS=*

# Database configuration for PostgreSQL
POSTGRES_DB=holistiplan_db
POSTGRES_USER=holistiplan_user
POSTGRES_PASSWORD=holistiplan_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Email configuration for MailHog (for development email testing)
EMAIL_HOST=mailhog
EMAIL_PORT=1025
DEFAULT_FROM_EMAIL=webmaster@localhost

Save the .env.local file.

Go back to your repository root in the terminal:

cd ..

5. Configure pyproject.toml for Pytest
The original pyproject.toml within the qa_homework folder might contain arguments that conflict with Playwright's testing setup.

Open qa_homework/pyproject.toml in your code editor.

Ensure the [tool.pytest.ini_options] section looks like this (remove or comment out any addopts lines):

[tool.pytest.ini_options]
minversion = "6.0"
python_files = [
    "test_*.py",
    "tests.py",
]
# No 'addopts' line here

Save the pyproject.toml file.

6. Place Automated Test Code
Ensure your test_rewards_app.py file is located directly inside the qa_homework directory (alongside docker-compose.yml). The code for test_rewards_app.py is part of your QA homework deliverables.

Running the Application and Tests 🚀
1. Start the Holistiplan Application (using Docker Compose)
Navigate to the qa_homework directory in your terminal and run:

docker-compose -f local.yml up --build -d

This command builds (if necessary) and starts the Django app, database, and MailHog services in the background.

Allow a few minutes for the first-time build and startup.

You can check if services are running with docker-compose ps.

Access the application in your browser at http://localhost:8000. Confirm it loads correctly before proceeding.

2. Run the Automated Tests
With the application running and your terminal still in the qa_homework directory:

pytest test_rewards_app.py

This will execute the Playwright tests defined in test_rewards_app.py.

Tests will launch a browser, perform actions, and assert outcomes.

Results (PASS/FAIL/ERROR/SKIPPED) will be displayed in your terminal.

Stopping the Application
To stop the Docker containers when you're done:

docker-compose down

Documentation Links
Manual Testing Documentation

[Automated Testing Documentation