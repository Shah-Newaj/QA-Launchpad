from playwright.sync_api import Page, expect


# Example 2 – Text Content Validation

def test_page_title(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    print("Launching Chrome browser ..............")
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    button_text = page.locator("#submit")
    # assert button_text == "Submit" # General Python approach
    expect(button_text).to_have_text("Submit") # Playwright built-in assertion mechanism
    print("Button text successfully matches")
    browser.close()