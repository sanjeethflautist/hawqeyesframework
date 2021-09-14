python -m pytest tests2 -n auto --env=PDT --profile=CX --log-cli-level=INFO --alluredir="tmp/my_allure_results2" -v
allure serve tmp/my_allure_results2