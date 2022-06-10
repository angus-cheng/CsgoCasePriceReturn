from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def goToSite(page=None):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              chrome_options=options)
    if page:
        driver.get("https://csgostash.com/" + page)
    else:
        driver.get("https://csgostash.com/")
    return driver


def getPages():
    driver = goToSite()
    pages = driver.find_elements(By.XPATH, "//*[@id='navbar-expandable']/ul/li[7]")
    # pages = driver.find_elements(By.XPATH, "//*[@id='navbar-expandable']/ul/li[8]")
    pageArray = []
    for page in pages:
        # Add pages at each \n
        pageArray.append(page.get_attribute("textContent").splitlines())
    # Unpack page array
    [pageArray] = pageArray
    noSearch = ["Cases", "All Skin Cases", "Souvenir Packages",
                "Gift Packages", "Newest Cases", ""]
    pageArray = list(filter(lambda page: page not in noSearch, pageArray))
    # pageArray = [page.replace(" ", "-") for page in pageArray]
    print(pageArray)
    return pageArray


def crawlPage(page=None):
    driver = goToSite(page)
    if page in driver.page_source:
        page.click()
    print(page.title)
    collection = driver.find_elements(By.TAG_NAME, "h3")
    for item in collection:
        print(item.text)
    return


pages = getPages()
for page in pages:
    crawlPage()
