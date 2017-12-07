import praw
import xlrd
reddit = praw.Reddit(client_id = 'nk7_2ZlG2QSpmw',
                    client_secret = 'hAi0KInm8DnchFOU2MT1vLHt6kI',
                    password = 'principle05',
                    user_agent = 'Python/mediatorapp:v1 (request by u/TheMediators4984)',
                    username = 'TheMediators4984')
print(reddit.user.me())

d = {}
wb = xlrd.open_workbook('Dictionary.xls')
sh = wb.sheet_by_index(0)
for i in range(3):
    cell_value_word = sh.cell(i,0).value
    cell_value_numb = sh.cell(i,1).value
    d[cell_value_word] = cell_value_numb

for comment in reddit.subreddit('pythonforengineers').stream.comments(): #dynamic
    if(comment.link_id == "t3_7cy2wk" and comment.saved == False):
        comment.save(category=None)
        
        totalSentiment = 0
        
        thisComment = comment.body
        print("Full comment: " + thisComment)
        
        sub_sentences = thisComment.split(",")
        
        for i in range (0, len(sub_sentences)):           #for each sub-sentence
            mult_ident = False        #reset multipliers
            mult_neg = False
            
            sentiment = 0
            words = sub_sentences[i].split(" ")
            
            for j in range (0, len(words)):               #for each word in sub-sentence
                currentWord = words[j].lower()
                
                if currentWord in d:
                    if (currentWord == "you"):            #check for identifiers
                        mult_ident = True
                    elif (currentWord == "not"):          #check for negators 
                        mult_neg = True
                    else:
                        sentiment = sentiment + d[currentWord];
                        
            if (mult_ident == True):                      #apply multipliers
                sentiment = sentiment * d['you']
            if (mult_neg == True):
                sentiment = sentiment * d['not']
            
            if (sentiment > 0):                           #add to total if negative
                totalSentiment = totalSentiment + sentiment
                        
        print("Sentiment: %f" %totalSentiment)
        
        if(sentiment > 3.49): #if word counter return true
            comment.reply("This is possibly an ad hominem.") #replies with acknowledgment of ad hominem
            print("replied") #confirms a reply was made
            
        print(" ")
        
submission.comments.replace_more(limit=0) #replace MoreComment objects to avoid error
for comment in submission.comments.list(): #Queues through all levels breadth-first 
    print(comment.body)
    comment.unsave()
