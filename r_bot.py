import time
import os 
import requests
import praw


start_time = time.time()


# create reddit object instance
reddit = praw.Reddit(client_id="#CientID Here",
                     client_secret="#ClientSecretHere",
                     password="#Password",
                     user_agent="#userAgent",
                     username="#Username")

# List of Subreddits to scrape...
subreddits = [# Add sub-reddits to scrape... Example:
              # "test",
              # "test2",
              # "etc",
]

cur_dir = os.getcwd()

#need to add exeption handling...
# turn bot into funtion... call funtion and add list as parameters....
for i in subreddits:
    print(i)
    current_sub = reddit.subreddit(i)
    print(current_sub.title)
            # can change current_sub.hot to {.new or .top} 
    for subs in current_sub.hot(limit=1): #limit can be changed to 1 - 60)
        x = subs.title
        print(x)
        y = requests.get(subs.url)
        z = subs.url
        print(z)
        with open(cur_dir +x+ ".jpg", 'wb') as f:
            f.write(y.content)
            f.close()
            print("Downloaded Images: "+x+ ".......")


end_time = time.time()


print("Script took " + str(end_time - start_time) + " to run")
