from selenium import webdriver
import time


# Takes in a browser with USNews page loaded in it
# and loads 25 more groups of colleges by pressing
# the "Load More" button
def load_25_pages(browser):
    for i in range(25):
        button = browser.find_element_by_link_text("Load More")
        browser.execute_script("arguments[0].scrollIntoView(true);", button)
        browser.execute_script("window.scrollTo(0, window.pageYOffset - 100);")
        button.click()
        time.sleep(5)


def fetch_and_parse():
    browser = webdriver.Chrome()
    browser.get(
        'https://www.usnews.com/best-colleges/search?school-name=&location='
        )
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(30)
    load_25_pages(browser)
    return


if __name__ == "__main__":
    fetch_and_parse()
