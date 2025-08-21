import pytest
from playwright.sync_api import Page, expect

# Base URL for the application
BASE_URL = "http://localhost:8000"

# Helper function to log in a user
def _login_user(page: Page, email: str = "someone@holistiplan.com", password: str = "bfx!wkp3zve3WUX*guq"):
    """Logs in a user with provided credentials."""
    page.goto(f"{BASE_URL}/accounts/login"),timeout=60000

    expect(page.locator("input[name='login']")).to_be_visible()
    page.fill("input[name='login']", email)
    page.fill("input[name='password']", password)
    page.click("button[type='submit']")
    
    expect(page).to_have_url(f"{BASE_URL}/users/1/")
    expect(page.locator("div.alert-success:has-text('successfully signed in as ')")).to_be_visible()

@pytest.fixture(scope="function", autouse=True)
def setup_teardown(page: Page):
    """
    Navigate to the base URL before each test and cleanup if needed.
    """
    page.goto(BASE_URL)
    # Ensure a clean state for tests that don't start from login,
    # or handle logout explicitly in relevant tests.
    yield

def test_successful_login(page: Page):
    """
    Tests successful login functionality with default credentials.
    """
    page.goto(f"{BASE_URL}/accounts/login/")

    # Fill in active email and password
    page.fill("input[name='login']", "someone@holistiplan.com")
    page.fill("input[name='password']", "bfx!wkp3zve3WUX*guq")

    # Click the login button
    page.click("button[type='submit']")

    # confirm on account page after successful login
    expect(page).to_have_url(f"{BASE_URL}users/1/")
    # check for a welcome message or an element only visible on the dashboard
    expect(page.locator("div.alert-success:has-text('successfully signed in as someone@holistiplan.com.')")).to_be_visible()
    print("Test: Successful login passed.")

def test_invalid_login(page: Page):
    """
    Tests login with invalid credentials.
    """
    page.goto(f"{BASE_URL}/accounts/login/")
    expect(page.locator("input[name='login']")).to_be_visible()

    # Fill in invalid credentials
    page.fill("input[name='login']", "wrong@holistiplan.com")
    page.fill("input[name='password']", "wrongpassword!")

    # Click the login button
    page.click("button[type='submit']")

    # confirm an error message is displayed
    expect(page.locator("div.alert-danger:has-text('The email address and/or password you specified are not correct.')")).to_be_visible()
    # Confirm the user remains on the login page
    expect(page).to_have_url(f"{BASE_URL}/accounts/login/")
    print("Test: Invalid login passed.")

def test_forgot_password(page: Page):
    """
    Tests the 'Forgot password' flow by submitting an email.
    Assumes there's a link to 'Forgot password' on the login page and a confirmation message after submission.
    """
    page.goto(f"{BASE_URL}/accounts/login")
    expect(page.locator("text='Forgot password?'")).to_be_visible()
    page.click("text='Forgot password?'")

    expect(page).to_have_url(f"{BASE_URL}/accounts/password/reset/")
    expect(page.locator("input[name='login']")).to_be_visible()
    page.fill("input[name='email']", "someone@holistiplan.com")
    page.click("button[type='submit']")

    # Confirm success message for sending reset link
    expect(page.locator("text='We have sent you an e-mail. Please contact us if you do not receive it within a few minutes.'")).to_be_visible()
    print("Test: Forgot password successfully.")


def test_signup_valid_user(page: Page):
    """
    Tests successful user registration with valid credentials.
    """
    page.goto(f"{BASE_URL}/accounts/signup/")
    expect(page.locator("input[name='email']")).to_be_visible()

    import time
    unique_email = f"test_user_{int(time.time())}@example.com"

    page.fill("input[name='email']", unique_email)
    page.fill("input[name='password1']", "SecurePass123!")
    page.fill("input[name='password2']", "SecurePass123!")

    page.click("button[type='submit']")

    # Assert successful registration (e.g., redirected to dashboard or a success page)
    expect(page).to_have_url(f"{BASE_URL}/accounts/confirm-email/")
    expect(page.locator("text='Verify Your E-mail Address'")).to_be_visible()
    print(f"Test: Valid signup for {unique_email} passed.")

def test_signup_invalid_credentials(page: Page):
    """
    Tests user registration with invalid credentials (e.g., mismatched passwords, weak password).
    """
    page.goto(f"{BASE_URL}/signup") 
    expect(page.locator("input[name='email']")).to_be_visible()

    page.fill("input[name='email']", "invalid_email")
    page.fill("input[name='password1']", "weak")
    page.fill("input[name='password2']", "mismatch")

    page.click("button[type='submit']")

    # Confirm error messages are displayed for invalid input
    expect(page.locator("text='This password is too short. It must contain at least 8 characters.'")).to_be_visible()
    expect(page.locator("text='You must type the same password each time.'")).to_be_visible()
    expect(page).to_have_url(f"{BASE_URL}/accounts/signup/")
    print("Test: Invalid signup with multiple errors passed.")

def test_home_page_confirm_working(page: Page):
    """
    Confirms that the home page loads successfully and displays key elements.
    """
    page.goto(BASE_URL)
    expect(page.locator("div.container:has-text('You\\'ve earned DjangoCon rewards!')")).to_be_visible()

    # Confirm key elements on the homepage
    expect(page.locator("text='You've earned DjangoCon rewards!'")).to_be_visible()
    expect(page.locator("button:has-text('Redeem this Reward')")).to_be_visible()
    expect(page.locator("button:has-text('+5')")).to_be_visible()
    expect(page.locator("text='Points Remaining'")).to_be_visible()
    print("Test: Home page successfully loaded.")

def test_about_page_confirm_working(page: Page):
    """
    Tests the "About" page
    """

    about_url = f"{BASE_URL}/about/" 
    page.goto(about_url)
    expect(page.locator("text='Use this document as a way to quick start any new project.'")).to_be_visible()

    # Confirm key elements on the page
    expect(page.locator("text='Use this document as a way to quick start any new project.'")).to_be_visible()
    print(f"Test: About page successfully loaded.")


def test_my_info_page_logged_in(page: Page):
    """
    Tests access to the 'My Info' page for a logged-in user.
    """
    _login_user(page)

    # Navigate to the 'My Info' page
    page.goto(f"{BASE_URL}/my-info/") 

    # Confirm key element unique to 'My Info' page is visible
    expect(page.get_by_label("text='Name of User'"))
    expect(page.locator("input[name='first_name']")).to_be_visible()
    print("Test: My Info page loaded successfully for logged-in user.")

def test_email_page_logged_in(page: Page):
    """
    Tests access to the 'Email' settings page for a logged-in user.
    """
    _login_user(page)

    # Navigate to the 'Email' page
    page.click("text='E-Mail'")
    page.goto(f"{BASE_URL}/accounts/email/")

    # Confirm the page title or a key element unique to 'Email' page is visible
    expect(page.locator("h1:has-text('E-mail Addresses')")).to_be_visible()
    expect(page.locator("h2:has-text('Add E-mail Address')")).to_be_visible()
    expect(page.locator("button[type='email']")).to_be_visible()
    print("Test: Email settings page loaded successfully for logged-in user.")

def test_MyInfo_page_logged_in(page: Page):
    """
    Tests access to the 'My Info' settings page for a logged-in user.
    """
    _login_user(page)

    # Navigate to the 'My Info' page
    page.click("text='My Info'")
    page.goto(f"{BASE_URL}/users/~update/")

    # Confirm the page title or a key element unique to 'My Info' page is visible
    expect(page.locator("h1:has-text('Someone AtHolistiplan')")).to_be_visible()
    expect(page.locator("input[name='name']")).to_be_visible()
    print("Test: My Info settings page loaded successfully for logged-in user.")


def test_claim_rewards_button_disabled(page: Page):
    """
    Tests that the 'Claim my rewards' button remains disabled even after adding points.
    """
    page.goto(BASE_URL)

    # Add points
    page.click("button:has-text('+5')")
    expect(page.locator("button[text='+5']")).to_be_visible()
    expect(page.locator("text=Points Remaining:")).to_contain_text("5")

    # Locate the "Claim my rewards" button
    claim_button = page.locator("button:has-text('Claim my rewards')")

    # Assert that the button is disabled
    expect(claim_button).to_be_disabled()
    print("Test: Claim rewards button disabled for unauthenticated user passed.")

