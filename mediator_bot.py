import praw   #library for reddit comment pulling
import xlrd   #library for reading excel sheets
reddit = praw.Reddit(client_id = 'nk7_2ZlG2QSpmw',                                     #Connects the bot to a sub-reddit
                    client_secret = 'hAi0KInm8DnchFOU2MT1vLHt6kI',
                    password = 'principle05',
                    user_agent = 'Python/mediatorapp:v1 (request by u/TheMediators4984)',
                    username = 'TheMediators4984')
print(reddit.user.me())

bad = {}          #Three dictionaries are initialized for personal identifiers, negations, and negative words
ident = {}
neg = {}
wb = xlrd.open_workbook('Dictionary.xls')
sh = wb.sheet_by_index(0)
for i in range(25):                       #The dictionaries are populated by the excel spreadsheet
    cell_value_word = sh.cell(i,0).value
    cell_value_numb = sh.cell(i,1).value
    ident[cell_value_word] = cell_value_numb
for i in range (26, 50):
    cell_value_word = sh.cell(i,0).value
    cell_value_numb = sh.cell(i,1).value
    neg[cell_value_word] = cell_value_numb
for i in range (51, 100):
    cell_value_word = sh.cell(i,0).value
    cell_value_numb = sh.cell(i,1).value
    bad[cell_value_word] = cell_value_numb

for comment in reddit.subreddit('pythonforengineers').stream.comments(): #So long as this bot runs, dynamically receive new comments
    if(comment.link_id == "t3_7cy2wk" and comment.saved == False):
        comment.save(category=None)
        
        totalSentiment = 0         #Initialize total comment sentiment
        
        thisComment = comment.body      #Get the comment as a string
        print("Full comment: " + thisComment)
        
        sub_sentences = thisComment.split(",")  #Split it into components
        
        for i in range (0, len(sub_sentences)):           #for each component...
            mult_ident = False        #Initialize identification and negation multiplier
            mult_neg = False
            
            sentiment = 0             #Initialize component sentiment
            words = sub_sentences[i].split(" ")   #Split component into words
            
            for j in range (0, len(words)):               #for each word in component
                currentWord = words[j].lower()
                
                if currentWord in bad:                    #If in negative word dictionary...
                    sentiment = sentiment + d[currentWord];  #...add to sentiment
                elif currentWord in neg:                  #If in negation or identifer dictionary...
                    mult_neg = True                       #...save multiplier for later
                elif currentWord in ident:
                    mult_ident = True
                        
            if (mult_ident == True):                      #Apply multipliers if found
                sentiment = sentiment * 1.5
            if (mult_neg == True):
                sentiment = sentiment * -1
            
            if (sentiment > 0):                           #Add component sentiment to total if negative
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
