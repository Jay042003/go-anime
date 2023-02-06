<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Jay042003/go-anime">
    <img src="images\logo.png" alt="Logo" >
  </a>

  <h1 align="center">goanime</h1>

  <p align="center">
    An awesome program which can help you bulk download your favourite anime.
    <br />
    <a href="https://github.com/Jay042003/anime-downloader"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Jay042003/anime-downloader/issues">Report Bug</a>
    ·
    <a href="https://github.com/Jay042003/anime-downloader/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

It is a web scraping program which helps you bulk download your favorite animes from a site called "animepahe".
You can auto download any anime found on animepahe.

It is hassle to download one episode at a time but you don't have to worry anymore you can bulk download all the episodes you want with help of this progrm

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][python-url]
* [![Selenium][Selenium]][selenium-url]
* [![Beautifulsoup][Beautifulsoup]][beautifulsoup-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


To get started you will need some packages and softwares in your device and it is recommended to use a virtual environment.

### Prerequisites

This are some softwares you need to install on your device.
* Python
  <p>You can download from the given url: <a href="https://www.python.org/downloads/"> Python </a></p>
* Chrome driver
  <p>You can download Chrome driver from the following link: <a href="https://chromedriver.chromium.org/downloads"> Chrome Driver </a></p>
> You need to download the exact version of chromedriver as your chrome browser. For checking the version of your chrome browser , you can type `chrome://version/` in search bar and hit enter to check the version.

### Installation

This are the steps you need to follow to install the program on your device:

1. Clone the repo
   ```sh
   git clone https://github.com/Jay042003/anime-downloader.git
   ```
2. Install packages
   ```sh
   pip install -r requirements.txt
   ```
3. You need to keep webdriver on this specific path in your device for it to work
   ```js
   C:/webdrivers/chromedriver.exe
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

In this section I will show how to use this program.

First of all there are many options in this program as following:
1. To set the link "-l"
    > <p> You can get the links from <a href="https://animepahe.com/"> here </a>. </p>
    > <p style ="color:Red;"><b>Warning !!</b></p>
    >link should be of the page like this page given in example
    > <img src="images\Website.png">
    > you can get it by following the given steps<br>
    > 1. Visit the given website.<br>
    > 2. Search the anime you want to see.<br>
    > 3. The page of the anime you want to see will open if you select a anime from the search click on any one of the episodes and you will come across a page like this.
2. To set the maximum number of episode "-m"
3. To set the starting episode "-s"
4. To set the quality of episodes downloaded "-q"
    > three qualities are available 
        "1080p"
        "720p"
        "360p"
execute this in terminal for using short args
``` sh
py main.py -l "LINK" -q "QUALITY" -s "START" -m "MAX"
```
execute this in terminal for using long args
``` sh
py main.py --link="link" --quality="quality" --start="start" --max="max"
```

You can also use "--epilist" or "-e" instead of start and max arguments to download specific episodes instead of a range
```sh
py main.py -l "LINK" -q "QUALITY" -m "1 2 4 6"
```
> this command will download eqisodes 1, 2, 4 and 6. You can also use "--eplist" instead of "-e" if you are using long args.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Jay Kadel - kadejay666@gmail.com

Project Link: [https://github.com/Jay042003/go-anime](https://github.com/Jay042003/go-anime)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/
[Selenium]: https://img.shields.io/badge/-selenium-CB02A?style=for-the-badge&logo=selenium&logoColor=whitestyle=for-the-badge&logo=selenium&logoColor=white
[selenium-url]: https://www.selenium.dev/
[Beautifulsoup]: https://img.shields.io/badge/-beautifulsoup-green?style=for-the-badge
[beautifulsoup-url]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
