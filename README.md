# hawqeyesframework
Pytest based framework for web UI and API testing


Hi 👋, Welcome to

Hawqeyes Framework powered by pytest

How to install?
    Dependencies are mentioned in requirement.txt
    To install the libraries, use below command:
        pip -r requirements.txt

How to run the pytest?
    To run Test, use command below-
        python -m pytest --log-cli-level=INFO --alluredir="tmp/my_allure_results" -v
    To get Allure report, run-
        allure serve tmp/my_allure_results
    or just run the pytestrunner.bat



Selenium Cheat sheet:
    Selenium Documentation: https://www.selenium.dev/selenium/docs/api/py/api.html
    Courtesy:https://www.browserstack.com/guide/locators-in-selenium
    Web driver Initialization:

        from selenium import webdriver
        driver = webdriver.Chrome('./chromedriver')      #Path of chromedriver
        driver.get("https://www.python.org")             #Opens the given url

    The different locators in Selenium are as follows:
        By CSS ID: find_element_by_id
            search_bar = driver.find_element_by_id("id-search-field")

        By CSS class name: find_element_by_class_name
            # Returns first element with matching class
            first_search_bar = driver.find_element_by_class_name("id-class-name")

        By name attribute: find_element_by_name
            #    for html page <form id="loginForm">
            #    <input name="name" type="text" value="First Name" />
            #    <input name="name" type="text" value="Last Name" />
            #    <input name="email" type="text" value="Business Email" />
            #    <input name="password" type="password" />
            #    <input name="continue" type="submit" value="Sign Me Up" />
            #    </form>
            #to fetch email id:
            email_input = driver.find_element_by_name("email")
            #to fetch first name
            name_input = driver.find_element_by_name("name")

        By DOM structure or xpath: find_element_by_xpath
            email_input = driver.find_element_by_xpath("//form[input/@name='email']")
            first_name = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
            last_name = driver.find_element_by_xpath("//form[@id='loginForm']/input[2]")

        By link text: find_element_by_link_text
            # Exact Link Text
            click_here_link = driver.find_element_by_link_text('Click Here')

        By partial link text: find_element_by_partial_link_text
            # Partial Link Text
            click_here_link = driver.find_element_by_partial_link_text('Click')

        By HTML tag name: find_element_by_tag_name
            page_heading = driver.find_element_by_tag_name('h1')

        by class
            from selenium.webdriver.common.by import By
            all_elements = driver.find_elements(By.CLASS_NAME, 'my-css-class')

            In addition to this, the By class has the following attributes:
            By.ID: search using the CSS ID
            By.LINK_TEXT: search using exact link text
            By.PARTIAL_LINK_TEXT: search using partial link text
            By.NAME: search using the name attribute
            By.TAG_NAME: search using the HTML tag name

    Browser Dev Tools Console Commands - Finding Elements
        1. Find using an XPATH: $x("//div[@value='note the single quotes']")
        2. Find using a CSS Selector: $$("div[value='note the single quotes']")

Contact-
    sanjeeth.nayak@agmail.com
