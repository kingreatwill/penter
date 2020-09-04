

# https://gitee.com/api/v5/repos/{owner}/{repo}/issues
import requests


def issues():
    resp = requests.get('https://gitee.com/api/v5/repos/openeuler/pyporter/issues?state=open&sort=created&direction=desc&page=1&per_page=20')
    if resp.ok:
        for issue in resp.json():
            print(issue['title'])

if __name__ == '__main__':
    issues()