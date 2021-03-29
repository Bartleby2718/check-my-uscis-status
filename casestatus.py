import datetime
from pytz import timezone

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


MY_RECEIPT_NUMBER = 'CHANGE THIS PART'
USCIS_URL = 'https://egov.uscis.gov/casestatus/landing.do'


def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Remote("http://selenium:4444/wd/hub", options=options)
    browser.get(USCIS_URL)
    browser.find_element_by_id('receipt_number').send_keys(MY_RECEIPT_NUMBER)
    browser.find_element_by_name('initCaseSearch').click()
    content = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "text-center")))
    eastern = timezone('US/Eastern')
    now = datetime.datetime.now(eastern)
    filename = now.strftime('%Y-%m-%dT%H-%M-%S.txt')
    with open(filename, 'w') as f:
        f.write(content.text)
    print(content.text)
    print(f'This was also written to {filename}')
    browser.quit()


if __name__ == '__main__':
    main()
