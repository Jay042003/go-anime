from selenium import webdriver
from bs4 import BeautifulSoup
from utils.prg_bar import progress_bar
import time
import sys
import colorama

class Scrapper:

    AVAILABLE_QUALITIES = {
        "360p": -3,
        "720p": -2,
        "1080p": -1,
    }

    def __init__(self, wdpath: str, cli_args: dict[str, str]) -> None:
        self.driver: webdriver.Chrome = webdriver.Chrome(wdpath)
        self.d_links = []

        # scrapper options
        self.link = cli_args.get("link")
        self.max = cli_args.get("max")
        self.start = cli_args.get("start")
        self.quality = -3
        self.epilist = cli_args.get("epilist")
        if cli_args.get("quality") != None:
            self.quality = Scrapper.AVAILABLE_QUALITIES[str(cli_args.get("quality"))]
        if self.epilist != None:
            self.episodes =[int(i) for i in self.epilist.split()]
        else:
            self.episodes = [int(i) for i in range(self.start, self.max+1)]
    def init(self) -> None:
        try:
            self.driver.get(
                self.link)

            self.driver.execute_cdp_cmd(
                "Network.setUserAgentOverride",
                {
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36"
                },
            )

            # minimizing window
            self.driver.minimize_window()

            for i in self.episodes:

                # selecting ith episode
                self.driver.execute_script(f"""
                document.querySelector("#scrollArea > a:nth-child({i})").click()
                """
                                           )

                # waiting for links to load
                time.sleep(1)

                #  visiting the redirect page
                soup = BeautifulSoup(self.driver.page_source, "lxml")
                self.driver.get(soup.find_all(
                    "a", class_="dropdown-item")[self.quality]["href"])

                # progress bar for showing how much links have been parsed
                action = "parsing"
                progress_bar(action, i, len(self.episodes))

                time.sleep(5)

                # getting dowload links
                soup2 = BeautifulSoup(self.driver.page_source, "lxml")
                self.d_links.append(
                    soup2.find(
                        "a", class_="btn btn-primary btn-block redirect")["href"]
                )

                # preparing for the next link
                self.driver.back()
                self.driver.back()

            print("\n")
            print("Parsing successful")

            # downloading from all the links given to the scraper
            for i in self.d_links:

                self.driver.get(i)
                time.sleep(2)

                # Executing js script to start downloading
                self.driver.execute_script(
                    """
                    document.querySelector("form").submit()
                """
                )

                # progress bar for downloads
                if (self.d_links.index(i) == 0):
                    action = "starting download"
                progress_bar(action, self.d_links.index(i) + 1, len(self.d_links))

                time.sleep(2)

            print("\nDownloads started successfully")
            print(colorama.Fore.RESET + "Please quit after downloading is complete")

            # Preventing exit of browser
            while 1:
                pass

        except KeyboardInterrupt:
            print(colorama.Fore.RESET + "\nEnding process")
            sys.exit()

        except Exception as E:
            print(colorama.Fore.RESET +
                  f"\nProcess exited due to an error")
            sys.exit()
