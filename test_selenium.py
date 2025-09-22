from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')  # Run in headless mode for Jenkins
driver = webdriver.Chrome(options=options)

try:
    driver.get('http://localhost:5000')
    time.sleep(2)  # Wait for page to load
    assert 'Hello, World!' in driver.page_source
    print('Test passed!')
except Exception as e:
    print(f'Test failed: {e}')
finally:
    driver.quit()
