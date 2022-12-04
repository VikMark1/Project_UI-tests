import allure

from aviasales_tests.model import app


def test_1_search_flights_without_return_1passenger_economy():
    with allure.step("Open homepage"):
        app.search_flights.open_site_ready()
    with allure.step("Fill departure point"):
        app.search_flights.fill_from('London')
    with allure.step("Fill destination point"):
        app.search_flights.fill_to('Berlin')
    with allure.step("Set departure date"):
        app.search_flights.fill_departure_date()
    with allure.step("Submit flights search"):
        app.search_flights.submit_search()

def test_2_search_flights_with_return_2passengers_business():
    with allure.step("Open homepage"):
        app.search_flights.open_site_ready()
    with allure.step("Fill departure point"):
        app.search_flights.fill_from('Paris')
    with allure.step("Fill destination point"):
        app.search_flights.fill_to('Rome')
    with allure.step("Set departure date"):
        app.search_flights.fill_departure_date()
    with allure.step("Set return date"):
        app.search_flights.fill_return_date()
    with allure.step("Set passengers number - adults"):
        app.search_flights.increase_adults_passengers_number()
    with allure.step("Set economy/business tripclass"):
        app.search_flights.set_class('business')
    with allure.step("Submit flights search"):
        app.search_flights.submit_search()

def test_3_search_flights_without_return_family_economy():
    with allure.step("Open homepage"):
        app.search_flights.open_site_ready()
    with allure.step("Fill departure point"):
        app.search_flights.fill_from('Madrid')
    with allure.step("Fill destination point"):
        app.search_flights.fill_to('Lisbon')
    with allure.step("Set departure date"):
        app.search_flights.fill_departure_date()
    with allure.step("Set passengers number - children"):
        app.search_flights.increase_children_passengers_number()
    with allure.step("Set passengers number - infants"):
        app.search_flights.increase_infants_passengers_number()
    with allure.step("Submit flights search"):
        app.search_flights.submit_search()

def test_4_search_hotels_1_guest():
    with allure.step("Open homepage"):
        app.search_flights.open_site_ready()
    with allure.step("Switch to 'Hotels' tab"):
        app.search_flights.switch_to_hotels()
    with allure.step("Fill hotel city"):
        app.search_flights.fill_hotel_city('Moscow')
    with allure.step("Set check-in date"):
        app.search_flights.fill_check_in_date()
    with allure.step("Submit hotels search"):
        app.search_flights.submit_hotels_search()

def test_5_search_hotels_2_guests():
    with allure.step("Open homepage"):
        app.search_flights.open_site_ready()
    with allure.step("Switch to 'Hotels' tab"):
        app.search_flights.switch_to_hotels()
    with allure.step("Fill hotel city"):
        app.search_flights.fill_hotel_city('Moscow')
    with allure.step("Set check-in date"):
        app.search_flights.fill_check_in_date()
    with allure.step("Set guests number"):
        app.search_flights.increase_adults_guests_number()
    with allure.step("Submit hotels search"):
        app.search_flights.submit_hotels_search()