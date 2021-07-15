from selenium import webdriver
import time
import json

def scrape_for_wifis():
	driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
	driver.get('https://www.google.com/maps/d/viewer?mid=1Z1dI8hoBZSJNWFx2xr_MMxSxSxY&ll=10.602124500000008%2C-66.9955364&z=8')
	wifi_dict = {}
	driver.find_element_by_xpath('//*[@id="legendPanel"]/div/div/div[2]/div/div/div[2]/div/div/div[3]/div[2]/div/div').click()
	len_wifis_str = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[3]/div[383]/span').text
	len_wifis = int(re.findall(r'\d+',len_wifis_str)[0])
	html_starting_index = 3
	preloaded_airports = 4

	# Starts scraping starting from the first airport
	for i in range(html_starting_index , len_wifis + html_starting_index + preloaded_airports):
		try:
			driver.find_element_by_xpath(f'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[3]/div[{i}]').click()
		except :
			pass
		time.sleep(1)
		name = driver.find_elements_by_class_name('qqvbed-p83tee-lTBxed')[0].text
		wifi_dict[name] = driver.find_elements_by_class_name('qqvbed-p83tee-lTBxed')[1].text.split('\n\n')[0]
		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/div/div/div[3]/div[1]/div/span/span/span').click()
		time.sleep(1)
	return wifi_dict


if __name__ == __main__:
	wifi_dict = scrape_for_wifis()
	
	with open('./airport_wifis.txt','w') as f:
    f.write(json.dumps(pass_dict))
	