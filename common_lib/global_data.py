# bnk
class GlobalData():
    MAX_EXPLICIT_SYNC_TIME = 20  #20 second default time
    CHROME_EXECUTABLE_PATH="C:/D/PyWorkspace/amazon/drivers/chromedriver.exe"
    BASE_URL = "https://www.amazon.in"
    SEARCH_TERM = "WD My Passport 4TB"
    HOME_PAGE_TITLE = "Amazon.in"
    NO_RESULTS_TEXT = "No results found."
    SIGN_IN_PAGE_TITLE = "Amazon Sign In"
    REQRES_API_USERS = "http://reqres.in/api/users"
    REQRES_API_LOGIN = "http://reqres.in/api/login"
    REQRES_API_REGISTER = "http://reqres.in/api/register"
    REQRES_API_UNKNOWN = "http://reqres.in/api/unknown"
    COMMON_HEADER =  {'Content-Type': 'application/json'}