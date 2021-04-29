import browser_cookie3 # https://github.com/borisbabic/browser_cookie3

from TikTokApi import TikTokApi

# collect all cookies belonging to tiktok
chrome_browser_cookies = browser_cookie3.chrome(domain_name="www.tiktok.com") # replace .chrome(...) with .load(...) to load cookies across all browsers

# NOTE: a user must be logged in on https://www.tiktok.com
user_verifyFp = chrome_browser_cookies.__dict__["_cookies"]["www.tiktok.com"]["/"]["s_v_web_id"].value # grab the s_v_web_id cookie from tiktok so we can login and view a user's profile

print(user_verifyFp)

# create a tiktok API instance
api = TikTokApi.get_instance(custom_verifyFp = user_verifyFp)
user_lookup = api.getUserObject(username = "bezlyn_")
user_data = api.user_liked(userID = user_lookup["id"], secUID = user_lookup["secUid"])

# grab some tiktoks
print("\n", user_data)
