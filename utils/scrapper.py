from selenium import webdriver
from bs4 import BeautifulSoup
from utils.prg_bar import progress_bar
import time
import sys
import colorama


class Scrapper:

    def __init__(self, wdpath: str, cli_args: dict[str, str]) -> None:
        self.driver: webdriver.Chrome = webdriver.Chrome(
            wdpath, options=self.options)
        self.d_links = []
        self.not_downloaded = []

        # setting default values
        self.link = "https://animepahe.com/play/65cda972-b195-1ac9-59f0-e2eb64553557/c6cdfbe2ee0b66d8a3d9a6d5a3db9ef3095962660ffec5e4899f5725e6a6910f"
        self.quality = '360p'
        self.max = 12
        self.start = 1

        # scrapper options
        if cli_args.get("link") != None:
            self.link = cli_args.get("link")

        if cli_args.get("max") != None:
            self.max = cli_args.get("max")

        if cli_args.get("start") != None:
            self.start = cli_args.get("start")

        self.epilist = cli_args.get("epilist")

        if cli_args.get("quality") != None:
            self.quality = str(cli_args.get("quality"))

        if self.epilist != None:
            self.episodes = [int(i) for i in self.epilist.split()]

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

                # selecting 1st episode
                self.driver.execute_script(f"""
                document.querySelector("#scrollArea > a:nth-child({i})").click()
                """
                                           )

                # waiting for links to load
                time.sleep(1)

                #  visiting the redirect page
                soup = BeautifulSoup(self.driver.page_source, "lxml")

                links = soup.find_all('a')
                indices = []
                for k in links:
                    if str(self.quality) in k.text:
                        indices.append(links.index(k))

                self.driver.get(soup.find_all(
                    "a")[indices[0]]["href"])

                # progress bar for showing how much links have been parsed
                action = "parsing"
                progress_bar(action, self.episodes.index(
                    i)+1, len(self.episodes))

                time.sleep(5)
                time.sleep(5)

                # getting dowload links
                soup2 = BeautifulSoup(self.driver.page_source, "lxml")
                self.d_links.append(
                    soup2.find(
                        "a", class_="btn btn-primary btn-block redirect")["href"]
                )

                # preparing for the next link
                self.driver.back()

            print("\n")
            print("Parsing successful")
            print(self.d_links)

            # downloading from all the links given to the scraper
            if self.start != None:
                count = self.start

            for i in self.d_links:
                if self.epilist != None:
                    count = self.episodes[self.d_links.index(i)]
                if i[0] == "#":
                    self.not_downloaded.append(count)
                else:
                    self.driver.get(i)
                    time.sleep(3)

                    # Executing js script to start downloading
                    self.driver.execute_script(
                        """
                        document.querySelector("form").submit()
                    """
                    )

                # progress bar for downloads
                if (self.d_links.index(i) == 0):
                    print(colorama.Fore.YELLOW + "starting download")

                count = count + 1
                time.sleep(3)

            print("\nDownloads started successfully")
            print(colorama.Fore.RESET +
                  "Please quit after downloading is complete by pressing Ctrl+C")
            print(colorama.Fore.RESET +
                  f"Following episode/episodes are not downloaded {self.not_downloaded}.")

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
