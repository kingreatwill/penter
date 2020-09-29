from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from dbmanager import Base

URL_SIZE = 250
EMAIL_SIZE = 100

class Repository(Base):
    __tablename__ = "repositories"

    archived = Column(Boolean())
    archive_url = Column(String(URL_SIZE))
    assignees_url = Column(String(URL_SIZE))
    blobs_url = Column(String(URL_SIZE))
    branches_url = Column(String(URL_SIZE))
    clone_url = Column(String(URL_SIZE))
    collaborators_url = Column(String(URL_SIZE))
    comments_url = Column(String(URL_SIZE))
    commits_url = Column(String(URL_SIZE))
    compare_url = Column(String(URL_SIZE))
    contents_url = Column(String(URL_SIZE))
    contributors_url = Column(String(URL_SIZE))
    created_at = Column(DateTime())
    default_branch = Column(String(50))
    description = Column(Text())
    downloads_url = Column(String(URL_SIZE))
    events_url = Column(String(URL_SIZE))
    fork = Column(Boolean())
    forks_count = Column(Integer())
    full_name = Column(String(100))
    git_commits_url = Column(String(URL_SIZE))
    git_refs_url = Column(String(URL_SIZE))
    git_tags_url = Column(String(URL_SIZE))
    git_url = Column(String(URL_SIZE))
    has_downloads = Column(Boolean())
    has_issues = Column(Boolean())
    has_wiki = Column(Boolean())
    homepage = Column(String(URL_SIZE))
    hooks_url = Column(String(URL_SIZE))
    html_url = Column(String(URL_SIZE))
    id = Column(Integer, primary_key=True)
    issue_comment_url = Column(String(URL_SIZE))
    issue_events_url = Column(String(URL_SIZE))
    issues_url = Column(String(URL_SIZE))
    keys_url = Column(String(URL_SIZE))
    labels_url = Column(String(URL_SIZE))
    language = Column(String(25))
    languages_url = Column(String(URL_SIZE))
    master_branch = Column(String(50))
    merges_url = Column(String(URL_SIZE))
    milestones_url = Column(String(URL_SIZE))
    mirror_url = Column(String(URL_SIZE))
    name = Column(String(100))
    network_count = Column(Integer())
    notifications_url = Column(String(URL_SIZE))
    open_issues = Column(Integer())
    open_issues_count = Column(Integer())
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    # TODO: Implement Owner
    parent_id = Column(Integer, ForeignKey('repositories.id'))
    # TODO: Implement Permissions
    private = Column(Boolean())
    pulls_url = Column(String(URL_SIZE))
    pushed_at = Column(DateTime())
    size = Column(Integer())
    # TODO: Implement Source
    ssh_url = Column(String(URL_SIZE))
    stargazers_count = Column(Integer())
    stargazers_url = Column(String(URL_SIZE))
    statuses_url = Column(String(URL_SIZE))
    subscribers_url = Column(String(URL_SIZE))
    subscribers_count = Column(Integer())
    subscription_url = Column(String(URL_SIZE))
    svn_url = Column(String(URL_SIZE))
    tags_url = Column(String(URL_SIZE))
    teams_url = Column(String(URL_SIZE))
    trees_url = Column(String(URL_SIZE))
    updated_at = Column(DateTime())
    url = Column(String(URL_SIZE))
    watchers = Column(Integer())
    watchers_count = Column(Integer())

class Plan(Base):
    __tablename__ = 'plans'

    id = Column(Integer, primary_key=True, autoincrement=True)
    collaborators = Column(Integer())
    name = Column(String(100))
    private_repos = Column(Integer())
    space = Column(Integer())

class Organization(Base):
    __tablename__ = 'organizations'

    avatar_url = Column(String(URL_SIZE))
    billing_email = Column(String(EMAIL_SIZE))
    blog = Column(String(URL_SIZE))
    collaborators = Column(Integer())
    company = Column(String(50))
    created_at = Column(DateTime())
    disk_usage = Column(Integer())
    email = Column(String(EMAIL_SIZE))
    events_url = Column(String(URL_SIZE))
    followers = Column(Integer())
    gravatar_id = Column(String(50))
    html_url = Column(String(URL_SIZE))
    id = Column(Integer(), primary_key=True)
    location = Column(String(50))
    login = Column(String(50))
    members_url = Column(String(URL_SIZE))
    name = Column(String(50))
    owned_private_repos = Column(Integer())
    plan_id = Column(Integer, ForeignKey('plans.id'))
    private_gists = Column(Integer())
    public_gists = Column(Integer())
    public_members_url = Column(String(URL_SIZE))
    public_repos = Column(Integer())
    repos_url = Column(String(URL_SIZE))
    total_private_repos = Column(Integer())
    # TODO: Implement type
    updated_at = Column(DateTime())
    url = Column(String(URL_SIZE))

class NamedUser(Base):
    __tablename__ = "namedusers"

    avatar_url = Column(String(URL_SIZE))
    bio = Column(Text())
    blog = Column(Text())
    collaborators = Column(Integer())
    company = Column(String())
    contributions = Column(Integer())
    created_at = Column(DateTime())
    disk_usage = Column(Integer())
    email = Column(String(EMAIL_SIZE))
    events_url = Column(String(URL_SIZE))
    followers = Column(Integer())
    followers_url = Column(String(URL_SIZE))
    following = Column(Integer())
    following_url = Column(String(URL_SIZE))
    gists_url = Column(String(URL_SIZE))
    gravatar_id = Column(String(50))
    hireable = Column(Boolean())
    html_url = Column(String(URL_SIZE))
    id = Column(Integer, primary_key=True)
    location = Column(String(50))
    login
    name
    organizations_url
    owned_private_repos
    permissions
    plan
    private_gists
    public_gists
    public_repos
    received_events_url
    repos_url
    site_admin
    starred_url
    subscriptions_url
    total_private_repos
    type
    updated_at
    url
