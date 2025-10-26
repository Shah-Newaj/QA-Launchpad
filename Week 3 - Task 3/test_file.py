import os
from playwright.sync_api import sync_playwright, TimeoutError

def test_file_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/upload")

        # ✅ Wait for the input element to be visible
        page.wait_for_selector("#file-upload", state="visible")

        # ✅ Make sure the file exists
        file_path = os.path.abspath("sample.txt")
        assert os.path.exists(file_path), f"File not found: {file_path}"

        # ✅ Upload the file
        page.locator("#file-upload").set_input_files(file_path)

        # ✅ Click submit
        page.locator("#file-submit").click()

        # ✅ Wait for success message
        page.wait_for_selector("h3")
        success_text = page.locator("h3").text_content()

        print("Upload Message:", success_text)
        assert "File Uploaded!" in success_text

        browser.close()
