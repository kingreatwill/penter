import github
import models

def convert_api_repo_to_db(repo: github.Repository) -> models.Repository:
    repo_db = models.Repository()
    repo_db.archived = repo.archived
    repo_db.archive_url = repo.archive_url
    repo_db.assignees_url = repo.assignees_url
    repo_db.blobs_url = repo.blobs_url
    repo_db.branches_url = repo.branches_url
    repo_db.clone_url = repo.clone_url
    repo_db.collaborators_url = repo.collaborators_url
    repo_db.comments_url = repo.comments_url
    repo_db.commits_url = repo.commits_url
    repo_db.compare_url = repo.compare_url
    repo_db.contents_url = repo.contents_url
    repo_db.contributors_url = repo.contributors_url
    repo_db.created_at = repo.created_at
    repo_db.default_branch = repo.default_branch
    repo_db.description = repo.description
    repo_db.downloads_url = repo.downloads_url
    repo_db.events_url = repo.events_url
    repo_db.fork = repo.fork
    repo_db.forks_count = repo.forks_count
    repo_db.full_name = repo.full_name
    repo_db.git_commits_url = repo.git_commits_url
    repo_db.git_refs_url = repo.git_refs_url
    repo_db.git_tags_url = repo.git_tags_url
    repo_db.git_url = repo.git_url
    repo_db.has_downloads = repo.has_downloads
    repo_db.has_issues = repo.has_issues
    repo_db.has_wiki = repo.has_wiki
    repo_db.homepage = repo.homepage
    repo_db.hooks_url = repo.hooks_url
    repo_db.html_url = repo.html_url
    repo_db.id = repo.id
    repo_db.issue_comment_url = repo.issue_comment_url
    repo_db.issue_events_url = repo.issue_events_url
    repo_db.issues_url = repo.issues_url
    repo_db.keys_url = repo.keys_url
    repo_db.labels_url = repo.labels_url
    repo_db.language = repo.language
    repo_db.languages_url = repo.languages_url
    repo_db.master_branch = repo.master_branch
    repo_db.merges_url = repo.merges_url
    repo_db.milestones_url = repo.milestones_url
    repo_db.mirror_url = repo.mirror_url
    repo_db.name = repo.name
    repo_db.network_count = repo.network_count
    repo_db.notifications_url = repo.notifications_url
    repo_db.open_issues = repo.open_issues
    repo_db.open_issues_count = repo.open_issues_count
    # TODO: Implement Organization
    # TODO: Implement Owner
    # TODO: Implement Parent
    # TODO: Implement Permissions
    repo_db.private = repo.private
    repo_db.pulls_url = repo.pulls_url
    repo_db.pushed_at = repo.pushed_at
    repo_db.size = repo.size
    # TODO: Implement Source
    repo_db.ssh_url = repo.ssh_url
    repo_db.stargazers_count = repo.stargazers_count
    repo_db.stargazers_url = repo.stargazers_url
    repo_db.statuses_url = repo.statuses_url
    repo_db.subscribers_url = repo.subscribers_url
    repo_db.subscribers_count = repo.subscribers_count
    repo_db.subscription_url = repo.subscription_url
    repo_db.svn_url = repo.svn_url
    repo_db.tags_url = repo.tags_url
    repo_db.teams_url = repo.teams_url
    repo_db.trees_url = repo.trees_url
    repo_db.updated_at = repo.updated_at
    repo_db.url = repo.url
    repo_db.watchers = repo.watchers
    repo_db.watchers_count = repo.watchers_count

    return repo_db