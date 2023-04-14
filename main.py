import tkinter as tk
from tkinter import simpledialog, messagebox
import instaloader
import pandas as pd
from time import sleep
import re

ROOT = tk.Tk()

ROOT.withdraw


class instagramScrapper():

    def __init__(self):

        self.L = instaloader.Instaloader()

    def accountLogin(self):

        try:

            from argparse import ArgumentParser
            from glob import glob
            from os.path import expanduser
            from platform import system
            from sqlite3 import OperationalError, connect

            try:
                from instaloader import ConnectionException, Instaloader
            except ModuleNotFoundError:
                raise SystemExit("Instaloader not found.\n  pip install [--user] instaloader")


            def get_cookiefile():
                default_cookiefile = {
                    "Windows": "~/AppData/Roaming/Mozilla/Firefox/Profiles/*/cookies.sqlite",
                    "Darwin": "~/Library/Application Support/Firefox/Profiles/*/cookies.sqlite",
                }.get(system(), "~/.mozilla/firefox/*/cookies.sqlite")
                cookiefiles = glob(expanduser(default_cookiefile))
                if not cookiefiles:
                    raise SystemExit("No Firefox cookies.sqlite file found. Use -c COOKIEFILE.")
                return cookiefiles[0]


            def import_session(cookiefile, sessionfile):
                print("Using cookies from {}.".format(cookiefile))
                conn = connect(f"file:{cookiefile}?immutable=1", uri=True)
                try:
                    cookie_data = conn.execute(
                        "SELECT name, value FROM moz_cookies WHERE baseDomain='instagram.com'"
                    )
                except OperationalError:
                    cookie_data = conn.execute(
                        "SELECT name, value FROM moz_cookies WHERE host LIKE '%instagram.com'"
                    )

                self.L.context._session.cookies.update(cookie_data)
                username = self.L.test_login()
                if not username:
                    raise SystemExit("Not logged in. Are you logged in successfully in Firefox?")
                print("Imported session cookie for {}.".format(username))
                self.L.context.username = username
                self.L.save_session_to_file(sessionfile)


            if __name__ == "__main__":
                p = ArgumentParser()
                p.add_argument("-c", "--cookiefile")
                p.add_argument("-f", "--sessionfile")
                args = p.parse_args()
                try:
                    import_session(args.cookiefile or get_cookiefile(), args.sessionfile)
                except (ConnectionException, OperationalError) as e:
                    raise SystemExit("Cookie import failed: {}".format(e))

            messagebox.showinfo(title="WARNING", message="Good Authentication")

        except:

            messagebox.showinfo(title="WARNING", message="Bad Authentication")

    def followersSave(self):

        try:

            self.L.context.do_sleep()

            profile = simpledialog.askstring(title="PROFILE", prompt="Username")
            followersProfile = instaloader.Profile.from_username(self.L.context, profile)

        
            followers = []


            for seg in followersProfile.get_followers():
                followers.append([profile, seg.username])
                print(seg.username)
                sleep(1)

            df = pd.DataFrame(followers, columns=['User','Followers'])

            with pd.ExcelWriter(profile + "Followers" + ".xlsx") as writer:
                df.to_excel(writer, index=False)

            messagebox.showinfo(title="WARNING", message="Followers file create")

        except:

            messagebox.showinfo(title="WARNING", message="Try again")

    def followingSave(self):

        try:

            self.L.context.do_sleep()

            profile = simpledialog.askstring(title="PROFILE", prompt="User")
            followingsProfile = instaloader.Profile.from_username(self.L.context, profile)

            #postagens = []
            followees = []

            ###CAPTURAR SEGUINDO###
            for seg in followingsProfile.get_followees():
                followees.append([profile, seg.username])
                sleep(1)

            df1 = pd.DataFrame(followees, columns=['Users', 'Followings'])

            with pd.ExcelWriter(profile + "Followings" + ".xlsx") as writer:
                df1.to_excel(writer, index=False)

            messagebox.showinfo(title="WARNING", message="Followings file create")

        except:

            messagebox.showinfo(title="WARNING", message="Try again")

    def posts(self):

        try:

            self.L.context.do_sleep()

            profile = simpledialog.askstring(title="PROFILE", prompt="User")

            feed = instaloader.Profile.from_username(self.L.context, profile).get_posts()

            for posts in feed:
                self.L.download_post(posts, profile)

            messagebox.showinfo(title="WARNING", message="All posts saved")

        except:

            messagebox.showinfo(title="WARNING", message="Try again")

    def onePost(self):

        #try:

            self.L.context.do_sleep()

            url = simpledialog.askstring(title="POST", prompt="URL")

            profile = simpledialog.askstring(title="USER", prompt="Profile")

            shortcode = url.split("/")[-2]

            profilePost = instaloader.Post.from_shortcode(self.L.context, shortcode)

            self.L.download_post(profilePost, target=profile + shortcode)

            comments = []

            for comment in profilePost.get_comments():
                postOwner = str(comment.owner)
                postUser = postOwner.split(" ")[-2]
                userID = re.sub('[()>]', '', postOwner.split(" ")[-1])
                postDateTime = str(comment.created_at_utc)
                postDate = postDateTime.split(" ")[0]
                postTime = postDateTime.split(" ")[1]

                comments.append((postUser, userID, comment.text, postDate, postTime))

                for answers in comment.answers:
                    postOwnerAnswers = str(answers.owner)
                    postUserAnswers = postOwnerAnswers.split(" ")[-2]
                    userIDAnswers = re.sub('[()>]', '', postOwnerAnswers.split(" ")[-1])
                    postDateTimeAnswers = str(answers.created_at_utc)
                    postDateAnswers = postDateTimeAnswers.split(" ")[0]
                    postTimeAnswers = postDateTimeAnswers.split(" ")[1]

                    comments.append((postUserAnswers, userIDAnswers, " ->" + answers.text, postDateAnswers, postTimeAnswers))

            df2 = pd.DataFrame(comments, columns=['User_Profile', 'UserID', 'Comment', 'Date', 'Time (UTC)'])

            with pd.ExcelWriter(profile + shortcode + "Comments" + ".xlsx") as writer:
                df2.to_excel(writer, index=False)

            messagebox.showinfo(title="WARNING", message="Target Post Downloaded")

        #except:

            #messagebox.showinfo(title="WARNING", message="Try again")

    def stories(self):

        try:

            self.L.context.do_sleep()

            profile = simpledialog.askstring(title="PROFILE", prompt="User")

            Id = self.L.check_profile_id(profile)

            self.L.download_stories(userids=[Id], fast_update=True, filename_target=profile + '-stories')

            messagebox.showinfo(title="WARNING", message="Stories saved")

        except:

            messagebox.showinfo(title="WARNING", message="Try again")

    def highlights(self):

        try:

            self.L.context.do_sleep()

            profile = simpledialog.askstring(title="PROFILE", prompt="User")

            Id = self.L.check_profile_id(profile)

            self.L.download_highlights(Id, fast_update=True, filename_target=profile + '-highlights')

            messagebox.showinfo(title="WARNING", message="Download complete")

        except:

            messagebox.showinfo(title="WARNING", message="Try again")

scrapper = instagramScrapper()

opcao = simpledialog.askstring(title="MENU:", prompt=" 1 - LOGIN \n 2 - Get Followers \n 3 - Get Followings \n 4 - Get all Feed Posts \n 5 - Get Stories \n 6 - Get Highlights \n 7 - Get a Specifc Post \n 0 - Exit \n ")

while(int(opcao) < 7 or opcao != 0):

    try:
        if (int(opcao) == 1):

            scrapper.accountLogin()

        elif int(opcao) == 2:

            scrapper.followersSave()

        elif int(opcao) == 3:

            scrapper.followingSave()

        elif int(opcao) == 4:
            scrapper.posts()

        elif int(opcao) == 5:
            scrapper.stories()

        elif int(opcao) == 6:
            scrapper.highlights()

        elif int(opcao) == 7:
            scrapper.onePost()

        elif int(opcao) == 0:
            messagebox.showinfo(title="Finishing", message="TURNED OFF")
            break

    except:

        messagebox.showinfo(title="WARNING", message="Try again")


    opcao = simpledialog.askstring(title="MENU:", prompt=" 1 - LOGIN \n 2 - Get Followers \n 3 - Get Followings \n 4 - Get all Feed Posts \n 5 - Get Stories \n 6 - Get Highlights \n 7 - Get a Specifc Post \n 0 - Exit \n ")
