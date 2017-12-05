# MediatorBot
Reddit bot that searches a submission and attempts to find character attacks

To change the targetted Reddit submission for the bot go to the code:
for comment in reddit.subreddit('pythonforengineers').stream.comments(): #dynamic
    if(comment.link_id == "t3_7cy2wk" and comment.saved == False):
    
and change the 'pythonforengineers' string to any subreddit you want to run the bot in. 
(IMPORTANT!: Make sure you either own the subreddit yourself or the specific subreddit is okay with bots! Otherwise you may be banned)
Then change the "t3_7cy2wk" string to "t3_ + the submission ID" where the submission ID is of the specific submission inside your selected subreddit that you wish to run in. For example, the current submission ID is 7cy2wk.
(submission ID can be found by going to the specific submission in your browser and looking at the URL. It will be the string of letters and numbers between slashes right after /comments/ in the URL.)

If you want to run the bot for the whole subreddit then simply remove the first half of the if statement from the second line: "comment.link_id == "t3_7cy2wk" and". Leaving only "if(comment.saved == False):"
