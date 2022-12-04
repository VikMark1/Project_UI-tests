from selene.support.shared import browser


class RadioButton:
    def __init__(self):
        pass
    def select_choice(self, value: str):
        browser.element(f'[data-test-id="tripclass-{value}-label"]').click()