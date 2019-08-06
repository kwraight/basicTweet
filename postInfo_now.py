import argparse
import tweepy
from datetime import datetime, date, timedelta
import time
import imp
#import configSettings_ppe

def GetArgs():
    parser = argparse.ArgumentParser(description=__file__)

    parser.add_argument('--config', help='directory for config file')
    parser.add_argument('--tweet', help='text to tweet')
    parser.add_argument('--hash', nargs='+', help='hashtags: text only (no symbols), space separated')

    args = parser.parse_args()

    print "args:",args

    argDict={'config':"../configs/configSettings_ppe.py", 'tweet':"testText" }

    for a in vars(args).iteritems():
        if not a[1]==None:
            print "got argument",a
            try:
                argDict[a[0]]=int(a[1])
            except:
                argDict[a[0]]=a[1]

    return argDict

######################
### useful functions
######################

def postInfo(tweet, configPath):
    print "string to tweet:\n"+tweet
    #sys.path.insert(0, "../configs")
    #import configSettings_ppe as configSettings
    configSettings = imp.load_source('something', configPath)
    api=configSettings.get_api()
    tweet = str(tweet)+" at:"+str(datetime.now()) # add time to avoid repeated tweets
    status = api.update_status(status=tweet)
    print "...tweeted"
# Yes, tweet is called 'status' rather confusing

######################
### main
######################

def main():

    argDict=GetArgs()


    tweetStr=argDict['tweet']
    for h in argDict['hash']:
        tweetStr+=" #"+str(h)
    postInfo(tweetStr, argDict['config'])



if __name__ == "__main__":
    print "### in",__file__,"###"
    start = time.time()
    main()
    end = time.time()
    print "\n+++ Total scan time: ",(end-start),"seconds +++\n"
    print "### out",__file__,"###"

    #some values to post
