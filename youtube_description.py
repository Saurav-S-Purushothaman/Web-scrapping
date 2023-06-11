from selenium import webdriver

# Set up Selenium webdriver (ensure you have the appropriate driver executable in PATH)
driver = webdriver.Chrome()

# Navigate to the YouTube video URL
video_url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
video_url = "https://www.youtube.com/watch?v=WgCavqDntlQ"
driver.get(video_url)

# Find the video description element
description_element = driver.find_element_by_xpath('//*[@id="description"]/yt-formatted-string')

# Get the text of the video description
video_description = description_element.text

# Print the video description
print(video_description)

# Close the browser
driver.quit()
