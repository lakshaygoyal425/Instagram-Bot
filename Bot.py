from instapy import InstaPy

session = InstaPy(username="Type Your Username", password="Type Your Password")
session.login()


# like section
session.like_by_tags(['deeplearning', 'python'], amount=100)
session.set_dont_like(["naked", "nsfw", "sex"])

# following section
session.set_do_follow(True, percentage=50, times=1)

# comment section
session.set_do_comment(True, percentage=100)
session.set_comments(['Love it','Nice Post', 'Amazing Post'])

session.end()
