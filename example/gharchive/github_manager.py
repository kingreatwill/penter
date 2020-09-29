from github import Github, GithubObject
from env import GITHUB_ACCESS_TOKEN
from repo_query_params import RepoSortParamsEnum

class GithubManager:
    def __init__(self):
        self._github_client = Github(GITHUB_ACCESS_TOKEN)

    def search_repos(self, repo_params: dict, sort_param: RepoSortParamsEnum):
        repos = self._github_client.search_repositories("", sort_param.STARS.name.lower(), order="desc", **repo_params)
        for page in range(repos.totalCount):
            page = repos.get_page(page)
            print(page)
        return repos

    def get_rate_limit(self):
        return self._github_client.get_rate_limit()