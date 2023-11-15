test_chrome_headless:
	pytest --reruns 5 -n 3 --headless=True  --browser=chromium --alluredir=allure_results_chrome
test_chrome:
	pytest --reruns 5 -n 3 --headless=False  --browser=chromium --alluredir=allure_results_chrome

test_firefox_headless:
	pytest --reruns 5 -n 3 --headless=True --browser=firefox --alluredir allure_results_firefox
test_firefox:
	pytest --reruns 5 -n 3 --headless=False  --browser=firefox --alluredir allure_results_firefox

serve_results_chrome: test_chrome_headless
	allure serve -p 8000 allure_results_chrome
serve_results_firefox:
	allure serve -p 8000 allure_results_firefox
