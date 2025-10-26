from playwright.sync_api import Page, expect


# Example 1 – Page Title Assertion

def test_page_title(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    print("Launching Chrome browser ..............")
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    # assert "Test Login | Practice Test Automation" in page.title() # General Python approach
    expect(page).to_have_title("Test Login | Practice Test Automation") # Playwright built-in assertion mechanism
    browser.close()