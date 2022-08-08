# Python program for automating Instagram crawling using instaloader

import argparse
import os
import sys
import time

import instaloader


def get_posts(username, max_posts):
    """
    Get posts from a user's profile
    :param username: username of the user
    :param max_posts: maximum number of posts to be downloaded
    :return: list of posts
    """
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, username)
    posts = profile.get_posts()
    return posts[:max_posts]


def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser(description='Instagram Crawler')
    parser.add_argument('-u', '--username', help='username of the user', required=True)
    parser.add_argument('-p', '--password', help='password of the user', required=True)
    parser.add_argument('-d', '--directory', help='directory to save the images', required=True)
    parser.add_argument('-m', '--max_posts', help='maximum number of posts to be downloaded', required=True)
    args = parser.parse_args()
    username = args.username
    directory = args.directory
    max_posts = int(args.max_posts)
    posts = get_posts(username, max_posts)
    for post in posts:
        post.download_post(directory)
        time.sleep(1)


if __name__ == '__main__':
    main()
    # sleep until given time
    time.sleep(3600)
    # restart the program
    python = sys.executable
    os.execl(python, python, *sys.argv)
    sys.exit(0)
    # end of program
