from wxpy import *

bot = Bot()
hogwarts_group = bot.groups().search('霍格沃茨中国校友会')[0]

@bot.register(msg_types=FRIENDS)
def welcome(msg):
    new_friend = msg.card.accept(verify_content="Hogwarts")
    new_friend.send('Welcome to Hogwarts, please take house sorting test.')
    hogwarts_group.add_members(new_friend, use_invitation=False)

@bot.register()
def get_house_registraters(self):
    '''
    Regist a keyword listener to reply with current house registraters.
    [return]    A dict of registraters for four houses
    '''
    pass

@bot.register()
def set_forest_email(self):
    '''
    Regist a keyword listener to accept a Forest email address, and call Forest.add_follow() to add follow to this email.
    Reply with a success/fail message.
    '''
    pass

@bot.register()
def get_house_score(self):
    '''
    Regist a keyword listener to reply with current house score.
    '''
    pass

def calculate_house_score(self, followed_rank, registraters):
    '''
    [params]:     
    followed_rank   followed_rank from forest API
    registraters    registraters of four houses

    [return]:
    house score adjusted with registraters
    '''
    pass
