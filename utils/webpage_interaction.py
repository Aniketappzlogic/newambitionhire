from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebPageInteraction:
    def __init__(self, driver):
        self.driver = driver

    def click_and_move_up(self):
        try:
            # Ensure the page has loaded and the body element is visible
            element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.TAG_NAME, 'body'))
            )
            self.driver.maximize_window()  # Maximize to increase the likelihood of being within bounds

            # Calculate the center of the window
            window_size = self.driver.get_window_size()
            center_x = window_size['width'] // 2
            center_y = window_size['height'] // 2

            print(f"Center Coordinates: x={center_x}, y={center_y}")

            actions = ActionChains(self.driver)

            # Perform actions with a check to ensure not moving out of bounds
            if center_y - 30 > 0:  # Check if moving up 30px keeps us within bounds
                actions.move_to_element_with_offset(element, center_x, center_y) \
                    .click() \
                    .move_by_offset(0, -30) \
                    .perform()
            else:
                print("Adjusting move to stay within bounds.")
                actions.move_to_element_with_offset(element, center_x, center_y) \
                    .click() \
                    .perform()
        except Exception as e:
            print(f"An error occurred: {e}")
