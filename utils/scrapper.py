from selenium import webdriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time, sys


class EpisodeQuality:
    low = "360p"
    mid = "720p"
    high = "1080p"


class Scrapper:
    def __init__(self, wdpath: str, cli_args: dict[str, str]) -> None:
        self.driver: webdriver.Chrome = webdriver.Chrome(wdpath)

    def init(self) -> None:
        try:
            self.driver.get(
                "https://animepahe.com/play/66f426f7-9e20-8646-b0f4-9fd4c61bbb14/c7f535bb5115e1492e63b821c994238b5d6043a9a6b5445cc5d2e317514d3a6a"
            )

            self.driver.execute_cdp_cmd(
                "Network.setUserAgentOverride",
                {
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36"
                },
            )

            soup = BeautifulSoup(self.driver.page_source, "lxml")
            self.driver.get(soup.find_all("a", class_="dropdown-item")[-2]["href"])

            time.sleep(4)

            soup2 = BeautifulSoup(self.driver.page_source, "lxml")
            self.driver.get(
                soup2.find("a", class_="btn btn-primary btn-block redirect")["href"]
            )

            # Executing js script to start downloading
            self.driver.execute_script(
                """
                document.querySelector("form").submit()
            """
            )

            print("Please quit after downloading is complete")

            # Preventing exit of browser
            while 1:
                pass

        except KeyboardInterrupt:
            print("\nEnding process")
            sys.exit()

        except Exception as E:
            print("\nProcess exited due to an error")
            sys.exit()
