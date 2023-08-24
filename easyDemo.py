from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 创建 ChromeOptions 对象，启用无头模式
chrome_options = Options()
chrome_options.add_argument('--headless')

# 指定 Chrome WebDriver 的路径
# webdriver_path = '/usr/local/bin/chromedriver'  # 将路径替换为实际的 Chrome WebDriver 路径

# 创建 Chrome WebDriver 实例
# driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)
# 打开网页
driver.get("https://www.example.com")
sleep(5)
# 获取页面标题并打印
print("页面标题:", driver.title)

# 关闭浏览器
driver.quit()
