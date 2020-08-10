from selenium import webdriver
import time
import winsound

class PaperBot:
    def __init__(self,username,pw):
        
        options = webdriver.ChromeOptions()
        
        """
        Uncomment the lines below if you want to save this to any specific location on your disk. 
        Be sure to use the right encoding for your platform! 
        Windows works very, very differently from MacOS, and Linux, so be careful with the forward and backslashes. 
        You can consult the video, or google Python Paths and look at StackOverflow, this is just to serve as a warning
        """
        
        #prefs = {"download.default_directory": r"your\download\directory\\"}
        #options.add_experimental_option("prefs",prefs)
        
        
        self.driver = webdriver.Chrome(options=options)
        
        self.driver.get("https://www.respaper.com")
        self.driver.find_element_by_xpath("//a[contains(text(), 'Sign in')]").click()
        self.driver.find_element_by_xpath("//input[@name=\"ui\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"pw\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//input[@name='li']").submit()
        
        myurl = "https://www.respaper.com/l?type=ICSE%20Prelims&subject=Mathematics&grade=10"
        
        self.driver.get(myurl)
        n = len(self.driver.find_elements_by_xpath("/html/body/div[2]/table/tbody/tr"))

        
        for i in range(151,n+1):
            try:
                print(i)
                #time.sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr["+str(i)+"]/td[1]/a").click()
                #time.sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[3]/p").click()
                self.driver.get(myurl)
                #self.driver.back()
            except:
                print(str(i) + "failed to download")
                self.driver.get(myurl)
        self.AudioAlert()
        time.sleep(10)
        
        
    def AudioAlert():
        winsound.Beep(4400,1000)
        print("\a")
        time.sleep(1)
        winsound.Beep(2000,1000)

"""
Uncomment the lines below to allow keyboard input for taking in the Username and Password 
(it will be on the Command Prompt, not in the actual Web Browser)
"""

username = ""
password = ""
#username = input("Enter your username: ")
#password = input("Enter your passsword: ")

PaperBot(username,password)