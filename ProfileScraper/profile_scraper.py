from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import re
import mysql.connector

class ProfileScraper():

    def __init__(self):
        super().__init__()
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        mydb = mysql.connector.connect(
            host="localhost",
            user="innogeeksuser",
            password="innogeeks2021",
            database="innogeeksdb"
        )
        self.dbCursor = mydb.cursor(dictionary=True)
        self.profiles = {
            "codechef": {"https://www.codechef.com/users/{}": "//h5[contains(text(), 'Fully Solved')]"},
            "codeforces": {"https://codeforces.com/profile/{}": "//div[contains(@class, '_UserActivityFrame_counterValue')]"},
            "spoj": {"https://www.spoj.com/users/{}/": "//dl[contains(@class, 'profile-info-data')]/dd"},
            "leetcode": {"https://leetcode.com/{}/": "//div[contains(@class, 'total-solved-count')]"},
            "gfg": {"https://auth.geeksforgeeks.org/user/{}/practice": "//a[contains(text(), 'Problems Solved')]"},
        }

        self.getUsers()
        self.getProfiles()
        self.driver.close()
        mydb.commit()
    
    def getUsers(self):
        self.dbCursor.execute("SELECT * FROM member_codingprofile")
        self.profilesData = self.dbCursor.fetchall()

    def getProfiles(self):
        updateCmd = """UPDATE member_codingprofile SET codechef_questions = %s,
                    codeforces_questions = %s, spoj_questions = %s, leetcode_questions = %s,
                    gfg_questions = %s WHERE user_id=%s"""

        for user in self.profilesData:
            outputQueryList = []
            for platform, data in self.profiles.items():
                for profile, query in data.items():
                    if (user[platform] == "" or user[platform] == "N/A"):
                        outputQueryList.append('0')
                        continue
                    profile = profile.format(user[platform])
                    questions = self.runQuery(profile, query)
                    outputQueryList.append(questions)

            outputQueryList.append(user["user_id"])
            self.dbCursor.execute(updateCmd, tuple(outputQueryList))     

    def runQuery(self, profile, query):
        try:
            self.driver.get(profile)
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, query))
            )
            questions = int(re.search(r'\d+', element.text).group())
            return questions
        except:
            return '0'

ProfileScraper()
