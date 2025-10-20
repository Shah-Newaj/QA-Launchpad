from playwright.sync_api import sync_playwright

def test_locators_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://practicetestautomation.com/practice-test-login/")

        username = page.locator("#username") #CSS Selector
        password = page.locator("//input[@id='password']") #XPATH
        login_button = page.get_by_role("button", name="Submit")

        # Print confirmation
        print("Username field found:", username.count() > 0)
        print("Password field found:", password.count() > 0)
        print("Login button found:", login_button.count() > 0)

        browser.close()
