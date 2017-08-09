# -*- coding: utf-8 -*-
import re
import json

from datetime import timedelta
from wxpy_utils import SortingHat
from wxpy import *

from forest import Forest

if __name__ == '__main__':
    bot = Bot()
    hogwarts_group = ensure_one(bot.groups().search(u'霍格沃茨中国校友会'))
    forest = Forest()
    login_response = forest.login()

    @bot.register(hogwarts_group, TEXT, except_self=False, run_async=True)
    def regist_msg(msg, except_self=False):
        print msg.text
        if "Apareciym" in msg.text:
            member_by_house = get_member_by_house()
            registraters = calculate_registraters(member_by_house)
            registraters = ''.join('{}: {}\n'.format(key.capitalize(), val)
                                   for key, val in registraters.items())
            return registraters
        elif "Flagrate" in msg.text:
            return forest.add_follow(fetch_email(msg.text))
        elif "Expecto Patronum" in msg.text:
            followed_rank = forest.get_followed_rank()
            followed_rank = format_followed_rank(followed_rank)
            return followed_rank

    def fetch_email(msg):
        match = re.search(r'[\w\.-]+@[\w\.-]+', msg)
        return match.group(0)

    def get_member_by_house():
        houses = {'gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin'}
        member_by_house = {
            house: hogwarts_group.search(house)
            for house in houses
        }
        return member_by_house

    def calculate_registraters(member_by_house):
        registraters = {
            house: len(members)
            for house, members in member_by_house.items()
        }
        return registraters

    def calculate_house_weight(registraters):
        house_weight = {
            k: float(v) / sum(registraters.values())
            for k, v in registraters.items()
        }
        return house_weight

    def format_followed_rank(followed_rank):
        followed_rank = [
            r["name"].encode("utf-8") + ": " +
            str(r["total_minute"]).encode("utf-8") + "mins"
            for r in followed_rank
        ]
        followed_rank = ''.join(followed_rank)
        return followed_rank

    embed()