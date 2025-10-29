from playwright.sync_api import sync_playwright

user_data_dir = 'user-data'
print(f'Using user data dir: {user_data_dir}')
with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        headless=False,
    )
    page = context.pages[0] if context.pages else context.new_page()
    page.goto('https://www.google.com')
    print('Browser launched. Press Enter here to close...')
    input()
    context.close()
