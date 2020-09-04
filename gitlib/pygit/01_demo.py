import os
from pygit2 import init_repository, clone_repository, discover_repository, Repository

# repo = init_repository('test')  # Creates a non-bare repository
# repo = init_repository('test', bare=True)  # Creates a bare repository
#
# repo_url = 'git://github.com/libgit2/pygit2.git'
# repo_path = '/path/to/create/repository'
# repo = clone_repository(repo_url, repo_path)  # Clones a non-bare repository
# repo = clone_repository(repo_url, repo_path, bare=True)  # Clones a bare repository
#
# current_working_directory = os.getcwd()
# repository_path = discover_repository(current_working_directory)
# repo = Repository(repository_path)

repo = Repository('../../.git')

print(repo.path)
