from selenium import webdriver
from bs4 import BeautifulSoup
import time, sys


class EpisodeQuality:
    def low(self):
        return -3

    def mid(self):
        return -2

    def mid(self):
        return -1


quality = EpisodeQuality()
start_from = 1
max_episodes = 12


class Scrapper:
    def __init__(self, wdpath: str, cli_args: dict[str, str]) -> None:
        self.driver: webdriver.Chrome = webdriver.Chrome(wdpath)
        self.d_links = []
        self.v_links = []

    def init(self) -> None:
        try:
            for i in range(start_from, max_episodes):
                self.driver.get(
                    'https://animepahe.com/play/c9a03d10-964a-bd20-ee4d-8370be493f28/57fadf8ec9a7ad770e7a56c872b76b5024cd8cf56d1e02cce2d8d975f1a18e1f')

                self.driver.execute_cdp_cmd(
                    "Network.setUserAgentOverride",
                    {
                        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36"
                    },
                )

                # selecting ith episode
                self.driver.execute_script(f"""
                document.querySelector("#scrollArea > a:nth-child({i})").click()
                """
                                           )

                # waiting for links to load
                time.sleep(1)

                #  visiting the redirect page
                soup = BeautifulSoup(self.driver.page_source, "lxml")
                self.driver.get(soup.find_all("a", class_="dropdown-item")[quality.low()]["href"])

                time.sleep(4)

                # getting dowload links
                soup2 = BeautifulSoup(self.driver.page_source, "lxml")
                self.d_links.append(
                    soup2.find("a", class_="btn btn-primary btn-block redirect")["href"]
                )          

                # preparing for the next link
                self.driver.back()  
                self.driver.back()  

            # downloading from all the links given to the scraper
            for i in self.d_links:

                self.driver.get(i)

                # Executing js script to start downloading
                self.driver.execute_script(
                    """
                    document.querySelector("form").submit()
                """
                )
                time.sleep(1)

            print("Please quit after downloading is complete")

            # Preventing exit of browser
            while 1:
                pass

        except KeyboardInterrupt:
            print("\nEnding process")
            sys.exit()

        except Exception as E:
            print(f"\nProcess exited due to an error: {E}")
            sys.exit()
