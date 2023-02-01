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
                'https://animepahe.com/anime/c9a03d10-964a-bd20-ee4d-8370be493f28')

            self.driver.execute_cdp_cmd(
                "Network.setUserAgentOverride",
                {
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36"
                },
            )

            # arranging page in ascending order
            self.driver.execute_script("""
             document.querySelector("body > section > article > div.content-wrapper > div.episode-bar.form-group.row > div.col-6.bar > div > label:nth-child(1)").click()
            """
                                  )
            # going to the page one
            time.sleep(2)
            self.driver.execute_script("""
             document.querySelector("body > section > article > div.content-wrapper > div.episode-list-wrapper > div > div:nth-child(1) > div > div.episode-snapshot > a").click()
            """
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
