import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
from BaseTest import BaseTest

now = datetime.now() 



# If any more library is needed import it here.

# Holds down the alt key


@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
class Helper(BaseTest):


    def help(self):

        # environment = str(self.driver.current_url.split('@')[1].split('.')[0])
        if "stg1" in self.driver.current_url:
            environment = "stg1"
        elif "prod1" in self.driver.current_url:
            environment = "prod1"

        testing = {
                'stg1': {},
                'prod1': {}
            }   

        env_name = testing.get(environment)

        return env_name, environment;