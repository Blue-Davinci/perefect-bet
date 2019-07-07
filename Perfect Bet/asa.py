from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.yahoo.com")
with open("page_source.html", "w") as f:
    f.write(driver.page_source)