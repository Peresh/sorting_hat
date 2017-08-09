import json
import requests
import datetime

class Forest:
    def __init__(self):
        with open("setting.json", "r") as setting_file:
            self.setting = json.loads(setting_file.read())

    def login(self):
        login_setting = self.setting["LOGIN"]
        login_url = login_setting["LOGIN_URL"]
        login_header = login_setting["LOGIN_HEADER"]
        login_form = json.dumps(login_setting["LOGIN_FORM"])

        login_response = requests.post(
            url=login_url, data=login_form, headers=login_header, verify=False)

        self.LOGIN_TOKEN = "remember_token=" + login_response.cookies["remember_token"]

        if login_response.status_code == requests.codes.ok:
            print "Forest login succeed."
        else:
            print "Forest login failed."
        return login_response

    def get_followed_rank(self):
        followed_setting = self.setting["FOLLOWED"]
        followed_rank_url = followed_setting["FOLLOWED_RANK_URL"]
        followed_rank_header = followed_setting["FOLLOWED_RANK_HEADER"]
        followed_rank_header["Cookie"] = self.LOGIN_TOKEN

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        
        param_tail = "%2016%3A00%3A00%20%2B0000"
        params = {
            'brief': 'true',
            'from_date': yesterday,
            'to_date': today
        }

        followed_rank = requests.get(
            url=followed_rank_url,params=params, headers=followed_rank_header, verify=False)
        followed_rank = json.loads(followed_rank.text, encoding="utf-8")
        return followed_rank


    def add_follow(self, target_email):
        target_email = {"target_email": target_email}
        add_follow_setting = self.setting["ADD_FOLLOW"]
        add_follow_url = add_follow_setting["ADD_FOLLOW_URL"]
        add_follow_header = add_follow_setting["ADD_FOLLOW_HEADER"]
        add_follow_header["Cookie"] = self.LOGIN_TOKEN
        
        print target_email
        print add_follow_header

        add_follow = requests.post(
            url=add_follow_url,
            headers=add_follow_header,
            data=json.dumps(target_email),
            verify=False)
        
        if add_follow.status_code == requests.codes.ok:
            return "Add Forest follow succeed."
        else:
            return "Add Forest follow failed."

if __name__ == '__main__':
    forest = Forest()
    print forest.login()
    # print forest.add_follow("18302106510@163.com")