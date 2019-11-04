# -*- coding: utf-8 -*- 

import pickle

def score(username):
    """The function will check if the scoreboard exist, if not,
create a new one and add the user into it."""
    try:
        with open('scores', 'rb') as F:
            S = pickle.load(F)
            if username in list(S.keys()):
                print(f"Welcome back {username}".upper())
            else:
                S[username] = 0
                print(f"Welcome for your first time {username}".upper())
    except:
        with open('scores', 'wb') as F:
            S = {username: 0}
            pickle.dump(S, F)
            print(f"Empty file. Welcome {username}".upper())
    return S
