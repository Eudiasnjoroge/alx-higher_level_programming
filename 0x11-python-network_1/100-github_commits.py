#!/usr/bin/python3
"""
Script that fetches 10 commits (from the most recent to oldest) of a given
GitHub repository by the specified owner.
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]

        for commit in commits:
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author}")
    else:
        print("Failed to retrieve commits")
