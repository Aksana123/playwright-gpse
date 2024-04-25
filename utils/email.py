import requests
import logging
from utils.logger import setup_logging
from utils.config import EnvironmentConfig, ENVIRONMENTS

setup_logging()


def send_email(meta_url, recipients, subject, body, environment):
    email_sent = False
    env_settings = ENVIRONMENTS[environment]

    try:
        # Get API token
        res = requests.post(meta_url + "/createToken",
                            json={"username": env_settings['username'], "password": env_settings['password']})
        if res.status_code == 200:
            token = res.json().get("data", {}).get("token")
            if token:
                headers = {"X-HTTP-AUTH-USER": env_settings['username'], "X-HTTP-AUTH-TOKEN": token}
                for recipient in recipients:
                    res = requests.post(meta_url + "/sendEmail",
                                        headers=headers,
                                        json={"to": recipient.strip(), "subject": subject, "body": body})
                    if res.status_code == 200:
                        logging.info(f"Email sent successfully to {recipient}")
                    else:
                        logging.warning(f"Failed to send email to {recipient}")
                email_sent = True
            else:
                logging.warning("Failed to retrieve token from API.")
        else:
            logging.warning(f"Failed to authenticate. Status code: {res.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    if email_sent:
        logging.info("All emails sent successfully.")
    else:
        logging.warning("Unable to send some or all emails.")
