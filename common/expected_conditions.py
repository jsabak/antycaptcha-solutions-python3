class text_changed():
    def __init__(self, locator, original_text):
        self.locator = locator
        self.original_text = original_text

    def __call__(self, driver):
        elt = driver.find_element(*self.locator)
        return elt.text != self.original_text