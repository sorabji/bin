#!/usr/bin/python

import requests
import datetime

baseUrl = 'http://reddit.com/r/'
subreddits = [
        baseUrl + 'technology/new.json',
        baseUrl + 'android/new.json',
        baseUrl + 'ubuntu/new.json'
]

minUp = 10
recentHours = 10
recentHoursDiff = datetime.timedelta(hours=recentHours)
now = datetime.datetime.utcnow()

def getFeed(r):
    res = requests.get(r, params={'limit': 75})
    if not res.ok:
        return 'fail ' + r
    return filter(recentFilter, filter(upDownFilter, res.json()['data']['children']))

def getFeeds(rs):
    return map(getFeed, subreddits)

def recentFilter(x):
    postDiff = now - datetime.datetime.fromtimestamp(x['data']['created_utc'])
    return postDiff < recentHoursDiff

def upDownFilter(x):
    downRatio = x['data']['ups'] * 0.2
    return x['data']['ups'] > minUp and x['data']['downs'] <= downRatio

def main():
    feeds = getFeeds(subreddits)
    for feed in feeds:
        if isinstance(feed, basestring):
            print feed
            continue
        for f in feed:
            print 'permalink: http://reddit.com' + f['data']['permalink']
            print 'article link: ' + f['data']['url']

if __name__ == '__main__':
    main()
