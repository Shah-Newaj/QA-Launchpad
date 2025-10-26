from playwright.sync_api import Page, expect

# Example 3 – Button State Check

def test_login_button_enabled_state(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    print("Launching Chrome browser ..............")
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    submit_button = page.locator("#submit")
    # assert submit_button is True
    expect(submit_button).to_be_enabled() # Playwright built-in assertion mechanism
    browser.close()