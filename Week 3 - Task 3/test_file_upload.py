import os
from playwright.sync_api import Page, expect

# Example 4 – File Upload Validation

def test_file_upload(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    print("Launching Chrome browser ..............")
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")

    file_path = os.path.abspath("sample.txt") #C:\Users\newaj\PycharmProjects\QA-Launchpad
    page.locator("#file-upload").set_input_files(file_path)
    page.locator("#file-submit").click()
    success_text = page.locator("h3").text_content()

    assert "File Uploaded!" in success_text
    browser.close()