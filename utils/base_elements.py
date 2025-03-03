import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import platform
import pyperclip
import pyautogui
import tkinter as tk
import socket
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# logging.disable(logging.CRITICAL)


def zoom_out():
    """
    Simulate pressing Ctrl and '-' to zoom out in the active window on Windows,
    and Cmd and '-' on macOS.
    """
    if platform.system() == "Darwin":  # Darwin is the system name for macOS
        pyautogui.hotkey('command', '-')
    else:
        pyautogui.hotkey('ctrl', '-')


class BaseElement(object):
    def __init__(self, driver, locator):
        """Initializes the BaseElement with the provided WebDriver and locator.
                Finds the web element(s) associated with the locator.
                """
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.web_elements = None
        self.find()

    def find(self):
        """Finds a single web element using the locator and waits until it is visible.
                Returns the located web element.
                """
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return element

    def find_elements(self):
        """Finds all web elements matching the locator and waits until they are visible.
                Returns a list of located web elements.
                """
        elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator=self.locator))
        self.web_elements = elements
        return elements

    def find_elements_text(self):
        """Finds all web elements matching the locator, extracts their text, and returns a list of text values.
                Also prints the text of each element and sets a pytest trace.
                """
        text_list = []
        elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator=self.locator))
        for element in elements:
            text_list.append(element.text)
            print(element.text)
            pytest.set_trace()
        return text_list

    def click(self):
        """Finds a single web element using the locator, waits until it is visible, and clicks it."""
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            locator=self.locator))
        element.click()
        return None

    def send_keys(self, txt):
        """Sends the provided text to the web element previously found and stored in self.web_element."""
        self.web_element.send_keys(txt)
        # logging.info(f'Entered {txt} in the field {self.web_element.text}')
        return None

    def get_attribute(self, atr):
        """Finds a single web element using the locator, waits until it is visible, and returns the value of the specified attribute."""
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            locator=self.locator))  # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(mark=self.locator))

        text = element.get_attribute(atr)
        print('***** atr value ' + text)
        return text

    def get_current_url(self):
        """Returns the current URL of the WebDriver."""
        url = self.driver.current_url
        # logging.info(f'Entered {txt} in the field {self.web_element.text}')
        return url

    def attribute(self, attr_name):
        """Returns the value of the specified attribute for the web element stored in self.web_element."""
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    def scroll_to(self):
        """Scrolls the web page until the web element stored in self.web_element is in view."""
        self.driver.execute_script("arguments[0].scrollIntoView();", self.web_element)
        logging.info(f'Scrolled to the element {self.web_element.text}')

    def scroll_up(self):
        """Scrolls up the web page by 250 pixels."""
        self.driver.execute_script("window.scrollBy(0,-250);")
        logging.info('Scrolling up')

    def scroll_up_into_view(self):
        """Scrolls the web page up around the element located by the locator."""
        element = self.find()
        element_location = element.location_once_scrolled_into_view
        self.driver.execute_script("window.scrollTo(0, arguments[0] - 250);", element_location['y'])
        logging.info('Scrolled up around the element')

    def move_to_element(self):
        """Moves the mouse to the web element located by the locator and waits until it is visible."""
        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        actions.move_to_element(element)
        actions.perform()

    def double_click(self):
        """
            Perform a double-click action on the element located by the locator attribute.
            """
        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator=self.locator))
        actions.double_click(element)
        actions.perform()

    def key_down(self):
        """
            Simulate pressing the down arrow key.
            """
        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator=self.locator))
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()

    def key_up(self):
        """
            Simulate pressing the up arrow key.
            """
        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator=self.locator))
        actions.send_keys(Keys.ARROW_UP)
        actions.perform()

    def press_enter_key(self):
        """
            Simulate pressing the Enter key.
            """
        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator=self.locator))
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def drop_down(self, txt):
        """
            Select an option in a dropdown menu by value.
            """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        down = Select(element)
        down.select_by_value(txt)

    def drop_down_by_value(self, txt):
        """
            Select an option in a dropdown menu by visible text.
            """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        down = Select(element)
        down.select_by_visible_text(txt)

    def open_new_window(self, new_url=None):
        """
            Open a new browser window and navigate to the specified URL.
            """
        self.driver.execute_script("window.open('');")
        time.sleep(2)
        # Switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(new_url)

    # @property
    def get_text(self):
        """
        Retrieve the visible text of the element located by the locator attribute.
        """
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            locator=self.locator))
        text = element.text
        return text

    def clear(self):
        """
        Clear the value of an input element by sending backspace keys until it is empty.
        """
        element = self.web_element
        while element.get_attribute("value") != "":
            element.send_keys(Keys.BACK_SPACE)

    def selected(self):
        """
            Check if the element located by the locator attribute is selected.
            """
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            locator=self.locator))
        return element.is_selected()

    def is_element_visible(self, timeout=600):
        """
            Check if the element located by the locator attribute is visible within the given timeout.
            """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.locator)
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    def get_copied_code(self):
        """Clicks the element and retrieves the copied text from the clipboard."""
        self.click()  # Assuming clicking this element copies text to the clipboard
        return pyperclip.paste()

    def get_clipboard(self):
        """
            Retrieve text content from the system clipboard using Tkinter.
            """
        root = tk.Tk()
        # Hide the Tkinter window as it is not needed to be visible
        root.withdraw()
        # Attempt to get clipboard data
        try:
            clipboard_content = root.clipboard_get()
        except tk.TclError as e:
            logging.info("Error getting clipboard data:  %s", str(e))
            clipboard_content = None
        # Cleanup by destroying the Tkinter root object
        root.destroy()
        return clipboard_content

    def validate_elements_count(self):
        """
            Find elements located by the locator attribute and return the count of these elements.
            """
        elements = self.find_elements()
        actual_count = len(elements)
        return actual_count

    def send_packet(self, destination, port, text_data, timeout=8):
        """
            Send a UDP packet with the given text data to the specified destination and port,
            and log the response if received within the timeout period.
            """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(timeout)  # Set a timeout for response waiting
            try:
                byte_data = text_data.encode('utf-8')
                sock.sendto(byte_data, (destination, port))
                logging.info("Packet sent to {destination}:{port}")

                # Attempt to receive a response
                try:
                    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
                    logging.info(f"Received response from {addr}: {data.decode('utf-8')}")
                except socket.timeout:
                    logging.info("No response received (timed out)")
                except Exception as e:
                    logging.info(f"Error receiving response: {e}")

            finally:
                sock.close()
        except socket.error as e:
            logging.info(f"Socket error: {e}")
        except UnicodeEncodeError as e:
            logging.info(f"Encoding error: {e}")
        except Exception as e:
            logging.info(f"An unexpected error occurred: {e}")

    def load_config(self):
        """
            Load configuration data from a JSON file located at 'data/events.json'.
            """
        path_to_json = 'data/events.json'  # Adjust the path according to your project structure
        with open(path_to_json, 'r') as file:
            config = json.load(file)
        return config

    def wait_for_element_to_appear(self, timeout=600):
        """
        Wait until the element located by the locator appears on the webpage.

        :param timeout: Maximum time to wait for the element to appear (default is 600 seconds).
        :return: The WebElement if it becomes visible within the timeout period.
        :raises TimeoutException: If the element does not become visible within the timeout period.
        """
        try:
            # Wait until the element located by the locator is visible
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.locator)
            )
            return element
        except TimeoutException:
            print(f"Element with locator {self.locator} not found within {timeout} seconds.")

    def get_window_handle_count(self):
        WebDriverWait(self.driver, timeout=10).until(lambda driver: len(driver.window_handles) > 1)
        return len(self.driver.window_handles)



