import selene
from selene.support.shared import browser


class DatePicker:
    def __init__(self, element: selene.Element):
        self.element = element
    def select_departure_date(self):
        browser.element('[data-test-id="departure-date-field"]').click()
        #browser.element('.calendar-navbar__button.--next').click()
        browser.element('[aria-label="Tue Jan 31 2023"]').press()
        return self
    def select_return_date(self):
        browser.element('[data-test-id="return-date-field"]').click()
        browser.element('.calendar-navbar__button.--next').click()
        browser.element('[aria-label="Tue Feb 28 2023"]').press()
        return self
    def select_check_in_date(self):
        browser.element('[data-test-id="departure_date_input"]').click()
        browser.element('[aria-label="Tue Jan 31 2023"]').press()
        return self