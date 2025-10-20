from playwright.sync_api import Page

def test_open_google(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    print("Launching Chrome browser ..............")
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://www.google.com")
    assert "Google" in page.title()
    browser.close()




