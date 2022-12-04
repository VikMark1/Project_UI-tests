from selene.support.shared import browser
from aviasales_tests.model.controls import datepicker
from aviasales_tests.model.controls.radiobutton import RadioButton


class SearchFlights:
    def open_site_ready(self):
        browser.open('https://www.aviasales.com')
        browser.element('#origin').clear()
        browser.element('[data-test-id="checkbox-booking"]').click()
        return self

    def fill_from(self, value: str):
        browser.element('#origin').type(value)
        return self

    def fill_to(self, value: str):
        browser.element('#destination').type(value)
        return self

    def fill_departure_date(self):
        datepicker.DatePicker.select_departure_date(self)
        return self

    def fill_return_date(self):
        datepicker.DatePicker.select_return_date(self)
        return self

    def submit_search(self):
        browser.element('[data-test-id="form-submit"]').click()
        return self

    def increase_adults_passengers_number(self):
        browser.element('[data-test-id="passengers-field"]').click()
        browser.element('.additional-fields__passenger-control.--increment').click()
        return self

    def increase_children_passengers_number(self):
        browser.element('[data-test-id="passengers-field"]').click()
        browser.element('[data-test-id="passengers-children-field"]>[data-test-id="tooltip-wrapper"]>.additional-fields__passenger-control.--increment').click()
        return self

    def increase_infants_passengers_number(self):
        browser.element('[data-test-id="passengers-field"]').click()
        browser.element('[data-test-id="passengers-infants-field"]>[data-test-id="tooltip-wrapper"]>.additional-fields__passenger-control.--increment').click()
        return self

    def set_class(self, value):
        RadioButton.select_choice(self, value)
        return self

    def switch_to_hotels(self):
        browser.element('[data-goal="hotelTab"]').click()
        return self

    def fill_hotel_city(self, value: str):
        browser.element('[data-test-id="destination-autocomplete-field"]').type(value)
        return self

    def fill_check_in_date(self):
        datepicker.DatePicker.select_check_in_date(self)
        return self

    def submit_hotels_search(self):
        browser.element('.button_70e8ad4.orange_70e8ad4.primary_70e8ad4.form-submit').click()
        return self

    def increase_adults_guests_number(self):
        browser.element('[data-test-id="passengers-field"]').click()
        browser.element('.additional-fields__passenger-control.--increment').click()
        return self