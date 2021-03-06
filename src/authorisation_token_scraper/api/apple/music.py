from authorisation_token_scraper.scraper import Scraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire.webdriver import Firefox


class Music(Scraper):
    """The Music class is an extension of the Scraper class that is designed for scraping the authorisation token
     from the Apple Music API.
     """

    def __init__(self):
        super().__init__()
        self.api_scope = 'https://amp-api.music.apple.com/'
        self.url = 'https://music.apple.com/gb/browse'

    def _make_api_request(self, driver: Firefox) -> None:
        # Wait for the button which makes a request to the API to be visible, and then click it.
        WebDriverWait(driver, self.timeout) \
            .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'div[role=link]'))) \
            .click()
