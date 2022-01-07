import praw
import json

#donne accès à reddit au bot (botstc)
# Put the correct info for the bot under this comment
r = praw.Reddit(client_id='####################',
        client_secret='#######################',
    password='####################',
    username='####################',
    user_agent='##################')
#indiquer quel subreddit il aura accès
subreddit = r.subreddit("stocks")
ticks = {}


def analyse_post(sub_id):
    tout = []
    tout.append(sub_id.title)
    tout.append(sub_id.selftext)
    tout = ' '.join(tout)
    tout = tout.split(" ")
    with open("nasdaq.json", 'r') as n:
        data = json.load(n)
        for i in range(len(data)):
            for j in range(len(tout)):
                if  data[i]["Symbol"] in tout[j]:
                    s = data[i]["Symbol"]
                
                    if s in ticks:
                        ticks[s] +=1
                    else:
                        ticks[s] = 1
        return ticks     

def analyse_comm(sub_id):
    for comment in subreddit.stream.comments():
        if comment.body:
            with open("nasdaq.json", 'r') as n:
                data = json.load(n)
                for i in range(len(data)):
                    
                    if  data[i]["Symbol"] in comment.body:
                            s = data[i]["Symbol"]
                
                            if s in ticks:
                                ticks[s] +=1
                            else:
                                ticks[s] = 1
        return ticks             


#la limite indique le nombre de post qu'il verra sur la page Hot
def bot_activation():
    for submission in subreddit.hot(limit=50):
        analyse_post(submission)
        analyse_comm(submission)
    return(ticks)


