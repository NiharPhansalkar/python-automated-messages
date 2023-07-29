from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.parse import quote

def send_whatsapp_msg(driver, phone, message):
    # Encode message for URL
    encoded_message = quote(message)

    # Create the URL with the phone number and message
    url = f'https://web.whatsapp.com/send?phone={phone}&text={encoded_message}'

    # Open the URL with the phone number and message
    driver.get(url)

    # Wait for a few seconds to let the message load
    time.sleep(10)

    try:
        send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']")))
        send_button.click()
        print("Message sent successfully!")
    except:
        print("Failed to send the message.")

    time.sleep(3)


def main():
    # Load webdriver
    driver = webdriver.Chrome()

    numbers = ['', '', '']
    message = 'This is an automated message. My account can be banned if I do this so I hope we have some random whatsapp number which we can use? Thanks'
    for number in numbers:
        send_whatsapp_msg(driver, number, message)
    driver.quit()

main()
