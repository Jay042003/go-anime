from utils.cliargparser import CliArguments
from utils.scrapper import Scrapper
import os


#################################################################
WEBDRIVER_PATH = "C:/webdrivers/chromedriver.exe"
WEBDRIVER_PATH = os.environ.get("WEBDRIVER_PATH", WEBDRIVER_PATH)

if __name__ == "__main__":
    scrapper = Scrapper(
        wdpath=WEBDRIVER_PATH,  # passing webdriver path
        cli_args=CliArguments(
            [
                "link",
                "quality",
                "max",
                "start",
                "epilist"
            ],
        ).todict(),  # passing cli arguments as dict
    )

    # Start scrapping
    scrapper.init()
