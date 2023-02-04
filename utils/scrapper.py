from selenium import webdriver
from bs4 import BeautifulSoup
from utils.prg_bar import progress_bar
import time, sys, colorama


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

    def init(self) -> None:
        try:
            for i in range(start_from, max_episodes):
                self.driver.get(
                    'https://animepahe.com/play/500e0c7f-656e-7649-d602-1f24dbdf3c58/5ebdbae707c70347ec1dd951fdde9e673913f4b0529a8f29b93fa12bf872f802')

                self.driver.execute_cdp_cmd(
                    "Network.setUserAgentOverride",
                    {
                        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36"
                    },
                )

                # minimizing window
                self.driver.minimize_window()

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

                #progress bar for showing how much links have been parsed
                if i == 1: 
                    print('Parsing')
                progress_bar(i,max_episodes-start_from)

            # downloading from all the links given to the scraper
            for i in self.d_links:

                self.driver.get(i)

                # Executing js script to start downloading
                self.driver.execute_script(
                    """
                    document.querySelector("form").submit()
                """
                )

                # progress bar for downloads
                if (self.d_links.index(i) == 0):
                    print('Starting Download')
                progress_bar(self.d_links.index(i) + 1, len(self.d_links))
                
                time.sleep(1)
            
            print('Your downloads have begun')
            print("Please quit after downloading is complete")

            # Preventing exit of browser
            while 1:
                pass

        except KeyboardInterrupt:
            print(colorama.Fore.RESET + "\nEnding process")
            sys.exit()

        except Exception as E:
            print(colorama.Fore.RESET + f"\nProcess exited due to an error: {E}")
            sys.exit()
