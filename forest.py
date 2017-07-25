import json
import requests


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
        return login_response

    def get_followed_rank(self):
        followed_setting = self.setting["FOLLOWED"]
        followed_rank_url = followed_setting["FOLLOWED_RANK_URL"]
        followed_rank_header = followed_setting["FOLLOWED_RANK_HEADER"]
        followed_rank_header["Cookie"] = self.LOGIN_TOKEN

        followed_rank = requests.get(
            url=followed_rank_url, headers=followed_rank_header, verify=False)
        return followed_rank

    def add_follow(self, target_email):
        target_email = {"target_email": target_email}
        add_follow_setting = self.setting["ADD_FOLLOW"]
        add_follow_url = add_follow_setting["ADD_FOLLOW_URL"]
        add_follow_header = add_follow_setting["ADD_FOLLOW_HEADER"]
        add_follow_header["Cookie"] = self.LOGIN_TOKEN
        add_follow = requests.post(
            url=add_follow_url,
            headers=add_follow_header,
            data=target_email,
            verify=False)
    
# DEBUG SNIPPET
# if __name__ == '__main__':
#     forest = Forest()
#     login_response = forest.login()
#     followed_rank = json.loads(forest.get_followed_rank().text,encoding="utf-8")
#     followed_rank = [{
#         "user_id": r["user_id"],
#         "name": r["name"],
#         "total_minute": r["total_minute"]
#     } for r in followed_rank]
#     print followed_rank