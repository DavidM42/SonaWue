import requests
import shutil
# import pickle

class SonaWue:
    def __init__(self, username:str, password:str):
        self._host = "https://psywue.sona-systems.com"
        # self._cookies = None
        # self._token = self._read_token()
        self._token = self._authenticate(username,password)
        print("Initialized SonaWue with token "+ self._token)

    # def _read_token(self):
    #     try:
    #         f = open('token.pckl', 'rb')
    #         token = pickle.load(f)
    #         f.close()
    #         return token
    #     except IOError:
    #         return 

    # def _set_token(self, token):
    #     self._token = token
    #     f = open('token.pckl', 'wb')
    #     pickle.dump(self._token, f)
    #     f.close()

    def _request_invalidator(self, r):
        if r.status_code != 200 or r.json()["ErrorCode"] != 0:
            print(r.json()["Errors"])
            print(r.json())
            #TODO own exception here
            raise Exception("Request to SoNA api failed")
        return r.json()["Result"]


    def test_connection(self):
        #TODO export cause unused
        url = self._host + "/services/SonaMobileAPI.svc/TestConnection"
        r = requests.post(url)
        r_json = r.json()

        print(r.text)
        #TODO better way to invalidate errored
        r = self._request_invalidator(r)

    def _login_page(self):
        #TODO export cause unused
        url = self._host + "/services/SonaMobileAPI.svc/GetLoginPageInfo"
        r = requests.post(url)#, cookies=self._cookies)
        r = self._request_invalidator(r)
        # self._cookies = r.cookies
        # print(r.text)
        return r


    def _custom_icon(self):
        url = self._host + "/custom/customlogo.png"

        r = requests.get(url,stream=True) #cookies=self._cookies, 
        print(r.status_code)
        with open('logo.png', 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
        del r

    def _authenticate(self, username:str, password:str):
        # r_login_page = self._login_page()

        url = self._host + "/services/SonaMobileAPI.svc/Authenticate"

        body = {
            "p_username": username,
            "p_password": password,
            "p_language_pref":"DE",
            "p_mobile_version":"2.0"
        }

        print("Authenticasting")
        r = requests.post(url, json=body)#, cookies=self._cookies)

        #TODO own authorize exception
        token = self._request_invalidator(r)

        # print(r.text)
        # self._set_token(token)
        return token

    def _my_schedule(self):
        url = self._host + "/services/SonaMobileAPI.svc/GetMyScheduleInfo"

        body = {
            "p_sessionToken": self._token
        }

        r = requests.post(url, json=body)
        result = self._request_invalidator(r)

        resultDict = {
            "course_credits": result["course_credits"],
            "display_course_credits": result["display_course_credits"],
            "display_overall_credits": result["display_overall_credits"],
            "overall_credits_earned": float(result["overall_credits_earned"].split(":")[1].strip()),
            "overall_credits_needed": float(result["overall_credits_needed"].split(":")[1].strip()),
            "study_signups": result["study_signups"],
            "text_progress_display": result["text_progress_display"]
        }

        print(resultDict)

    def _main_menu_info(self):
        url = self._host + "/services/SonaMobileAPI.svc/GetMainMenuInfo"

        body = {
            "p_sessionToken": self._token
        }

        r = requests.post(url, json=body)
        result = self._request_invalidator(r)

        resultDict = {
            "announcement_display": result["announcement_display"],
            "announcement_name": result["announcement_name"],
            "announcement_text": result["announcement_text"],
            "credits_display": result["credits_display"],
            "credits_earned": result["credits_earned"],
            "credits_name": result["credits_name"],
            "credits_needed": result["credits_needed"],
            "credits_pending": result["credits_pending"],
            "email_questions_text": result["email_questions_text"],
            "faq_enabled": result["faq_enabled"],
            "logo_url": result["logo_url"],
            "signups": result["signups"],
            "signups_display": result["signups_display"],
            "signups_name": result["signups_name"],
            "site_name": result["site_name"],
            "username_name": result["username_name"],
            "username_text": result["username_text"],
            "username_type": result["username_type"]
        }

        print(resultDict)

    

