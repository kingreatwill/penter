# https://github.com/dotnet/roslyn.git
import argparse
import re
import os


# 为了减少依赖还是直接命令号了， pip install GitPython

# 项目名称不能重复
def read_git_list(filename):
    dic = {}
    with open(filename, 'r') as f:
        list = f.readlines()
    for repo in list:
        repo = repo.strip('\n')
        if repo.isspace():
            continue
        # https://git-scm.com/docs/git-clone#URLS
        repo_match = re.search(r'(?<=/)[^/]+(?=\.git)', repo)
        if repo_match:
            dic[repo_match.group(0)] = repo
    return dic


# https://gitee.com/shoubashou/NetCoreMicroService.git
# git@gitee.com:newgateway/xdh-map.git
# https://gitee.com/iteaj/ivzone.git

def main(path, name, git_prefix):
    list = read_git_list(os.path.join(path, name))
    for (proj_name, repo_url) in list.items():
        repo_path = os.path.join(path, proj_name)
        # 不存在：clone( 还可以检查是否是git仓库，有时存在目录却不是git仓库，那么可以删除)
        if not os.path.exists(repo_path):
            output = os.popen("git clone {} {}".format(repo_url, repo_path))
            print(output.read())
        # git remote -v
        output = os.popen("cd {} & git remote -v".format(repo_path))
        # git remote set-url --add origin git@e.coding.net:openjw/kingreatwill/open.git
        sync_url = "{}/{}.git".format(git_prefix, proj_name)
        if output.read().find(sync_url) < 0:
            print(os.popen("git remote set-url --add origin {}".format(sync_url)).read())
        # pull repo, push repo
        print(os.popen("cd {} & git pull & git push".format(repo_path)).read())


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path",
                    default="",
                    help="路径，默认当前路径")
parser.add_argument("-r", "--repo_list",
                    default="list.txt",
                    help="list.txt")
parser.add_argument("-git", "--git_url",
                    required=True,
                    help="git url")
# python gitdemo.py -p D:/ -git xx
if __name__ == '__main__':
    args = parser.parse_args()
    # main("", "gitdemo.txt", "x")
    main(args.path, args.repo_list, args.git_url)
