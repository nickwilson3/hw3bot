import praw
import random
import datetime
# connect to reddit 
reddit = praw.Reddit('botgang')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/'
submission = reddit.submission(url=reddit_debate_url)


# FIXME:
# copy your generate_comment functions from the week_07 lab here
def generate_comment_0():
    trump_names = ['Donald Trump', 'President Trump', 'The Don', 'Donald', 'Trump', 'Mr. Trump', 'the guy with the hot wife']
    trump_name = random.choice(trump_names)
    good_feelings = ['like', 'love', 'support', 'am a fan of', 'will sacrifice my life for']
    good_feeling = random.choice(good_feelings)
    roles = ['president', 'POTUS', 'king', 'superior human of the country']
    role = random.choice(roles)
    descriptions = ['funny', 'big', 'small', 'cool']
    description = random.choice(descriptions)
    features = ['face', 'foot', 'personality', 'ego']
    feature = random.choice(features)
    positive_superlatives = ['better than', 'superior to', 'greater than', 'more elite']
    positive_superlative = random.choice(positive_superlatives)
    text = 'I ' + good_feeling + ' ' + trump_name + ' as ' + role + ' because he has a ' + description + ' ' + feature+'. ' + trump_name + ' is ' + positive_superlative + ' Joe Biden.'
    return text

def generate_comment_1():
    trump_names = ['Donald Trump', 'President Trump', 'The Don', 'Donald', 'Trump', 'Mr. Trump', 'the guy with the hot wife']
    trump_name = random.choice(trump_names)
    positive_rankings = ['best', 'greatest', 'coolest', 'funniest']
    positive_ranking = random.choice(positive_rankings)
    roles = ['president', 'POTUS', 'king', 'superior human of the country']
    role = random.choice(roles)
    americas = ['America', 'the USA', 'the United States of America', 'merica', 'this great land', 'the land of the free']
    america = random.choice(americas)
    text = trump_name + ' is the ' + positive_ranking + ' ' + role + ' ' + america + ' has ever had. No other ' + role + ' can compare to ' + trump_name+'.'
    return text

def generate_comment_2():
    good_feelings = ['like', 'love', 'support', 'am a fan of', 'will sacrifice my life for']
    good_feeling = random.choice(good_feelings)
    positive_descriptions = ['smarter', 'more intelligent', 'more handsome', 'funnier']
    positive_description = random.choice(positive_descriptions)
    characteristics = ['factor', 'reason', 'characteristic', 'description']
    characteristic = random.choice(characteristics)
    trump_names = ['Donald Trump', 'President Trump', 'The Don', 'Donald', 'Trump', 'Mr. Trump', 'the guy with the hot wife']
    trump_name = random.choice(trump_names)
    joe_names = ['Joe', 'Biden', 'Joe Biden', 'Mr. Biden', 'the man with dementia', 'the guy older than Jesus']
    joe_name = random.choice(joe_names)
    text = 'I ' + good_feeling + ' ' + trump_name + ' he is ' + positive_description + ' than ' + joe_name +'. That ' + characteristic + ' is why I am going to vote for ' + trump_name+'.'
    return text

def generate_comment_3():
    joe_names = ['Joe', 'Biden', 'Joe Biden', 'Mr. Biden', 'the man with dementia', 'the guy older than Jesus', 'Mr. University of Delaware']
    joe_name = random.choice(joe_names)
    negative_superlatives = ['worst', 'most horrible', 'biggest bum', 'very bad']
    negative_superlative = random.choice(negative_superlatives)
    roles = ['president', 'POTUS', 'king', 'superior human of the country']
    role = random.choice(roles)
    negative_descriptions = ['bad', 'horrible', 'atrocious', 'disgraceful']
    negative_description = random.choice(negative_descriptions)
    americas = ['America', 'the USA', 'the United States of America', 'merica', 'this great land', 'the land of the free']
    america = random.choice(americas)
    text = joe_name + ' is the ' + negative_superlative + ' ' + role + ' candidate. ' + joe_name + ' is a ' + negative_description + ' representation of ' + america+'.'
    return text

def generate_comment_4():
    joe_names = ['Joe', 'Biden', 'Joe Biden', 'Mr. Biden', 'the man with dementia', 'the guy older than Jesus', 'Mr. University of Delaware']
    joe_name = random.choice(joe_names)
    dumbs = ['an idiot', 'not a smart person', 'a person with dementia', 'a person who needs a teleprompter to speak']
    dumb = random.choice(dumbs)
    roles = ['president', 'POTUS', 'king', 'superior human of the country']
    role = random.choice(roles)
    disgraces = ['a disgrace', 'a bad look', 'a misreputation', 'dangerous']
    disgrace = random.choice(disgraces)
    americas = ['America', 'the USA', 'the United States of America', 'merica', 'this great land', 'the land of the free']
    america = random.choice(americas)
    text = joe_name + ' is ' + dumb + ' so he should not be able to be ' + role+'. ' + joe_name + ' would be ' + disgrace + ' to ' + america+'.'
    return text

def generate_comment_5():
    screweds = ['screwed', 'not in a good place', 'slacking', 'behind']
    screwed = random.choice(screweds)
    joe_names = ['Joe', 'Biden', 'Joe Biden', 'Mr. Biden', 'the man with dementia', 'the guy older than Jesus', 'Mr. University of Delaware']
    joe_name = random.choice(joe_names)
    roles = ['president', 'POTUS', 'king', 'superior human of the country']
    role = random.choice(roles)
    americas = ['America', 'the USA', 'the United States of America', 'merica', 'this great land', 'the land of the free']
    america = random.choice(americas)
    trump_names = ['Donald Trump', 'President Trump', 'The Don', 'Donald', 'Trump', 'Mr. Trump', 'the guy with the hot wife']
    trump_name = random.choice(trump_names)
    text = 'If ' + joe_name + ' is elected as ' + role + ' of ' + america + ' then our economy will be ' + screwed+'.' + ' This is why we need to elect ' + trump_name
    return text

def generate_comment():
    for i in range(1):
        options = [0,1,2,3,4,5]
        choice = random.choice(options)
        if choice==0:
            return generate_comment_0()
        elif choice==1:
            return generate_comment_1()
        elif choice==2:
            return generate_comment_2()
        elif choice==3:
            return generate_comment_3()
        elif choice==4:
            return generate_comment_4()
        elif choice==5:
            return generate_comment_5()


while True: #change to while loop at end

    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)
    submission.comments.replace_more(limit = None) #change to none at end

    # FIXME (task 0)
    all_comments = []
    for comment in submission.comments.list():
        all_comments.append(comment.body)
    print('len(all_comments)=',len(all_comments))



# FIXME (task 1)
    not_my_comments = []
    for comment in submission.comments.list():
            if comment.author != 'ibotalambo':
                not_my_comments.append(comment)
    print('len(not_my_comments)=',len(not_my_comments))
    

        # FIXME (task 2)
    has_not_commented = len(not_my_comments) == len(all_comments)
    if len(all_comments) == len(not_my_comments):
        submission.reply(generate_comment())
    else:
        print()

        # FIXME (task 3)
      
    comments_without_my_replies = []
    for comment in not_my_comments:
        if comment.author != 'ibotalambo':
            response = False
            for reply in comment.replies:
                if str(reply.author) == 'ibotalambo':
                    response = True
            if response == False:
                comments_without_my_replies.append(comment)
    print('len(comments_without_my_replies)=',len(comments_without_my_replies))
    

        # FIXME (task 4)
    for comments in comments_without_my_replies:
        selection = random.choice(comments_without_my_replies)
        generated_reply = generate_comment()
        try:
            selection.reply(generated_reply)
        except praw.exceptions.RedditAPIException as error:
            if "DELETED_COMMENT" in str(error):
                print("Comment" + comment.id + "was deleted")
            else:
                print(error)

        # FIXME (task 5)
    random_submission = reddit.subreddit('csci040temp').random()
    choices = [random_submission, submission]
    number = random.randint(0,101)
    if number < 50:
        submission = random_submission
    else: 
        submission = reddit.submission(url=reddit_debate_url)

    #task 6 upvote comment
    trump = ['Trump', 'Donald Trump', 'President Trump']
    for comment in submission.comments.list():
        if trump in comment.body.lower():
            comment.upvote() 
    #task 7 downvote comment
    biden = ['Biden', "Joe Biden", 'Vice President', 'Vice President Biden']
    for comment in submission.comments.list():
        if biden in comment.body.lower():
            comment.downvote()
    #task 8 upvote submission
    for submission in reddit.subreddit('csci040temp'):
        if trump in submission: 
            submission.upvote()
    #task 9 downvote submission
        if biden in submission:
            submission.downvote()
        
        
 
    







        