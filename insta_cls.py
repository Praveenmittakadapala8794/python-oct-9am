from instagramy import InstagramUser

username =input("enter your username:")

user_data =InstagramUser(username)

# print(dir(user_data))
print(user_data)

print(user_data.number_of_followers)

print(user_data.number_of_followings)

print(user_data.number_of_posts)

print(user_data.posts_display_urls)

