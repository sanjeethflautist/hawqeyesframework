python -m pytest tests -n auto --env=PDT --profile=CX --log-cli-level=INFO --alluredir="tmp/my_allure_results" -v
allure serve tmp/my_allure_results