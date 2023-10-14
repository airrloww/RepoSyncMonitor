
from git import Repo
import shutil

repo_name = "to_test_another_repo"
remote_repo = f"new_{repo_name}"
local_hash_list = []
remote_hash_list = []

def remove_dir():
    try:
        shutil.rmtree(remote_repo)
        print("Directory removed successfully")
    except OSError as o:
        print(f"Error, {o.strerror}: {remote_repo}")


def local_repo_hashes():
    local_repo = Repo(repo_name)

    # Get a list of all commits on the Main branch
    commits = list(local_repo.iter_commits('main'))

    for i in commits:
        local_hash_list.append(i)
        # print(local_hash_list)

    print(f" [+] Local hash count: {len(commits)}")
    return local_hash_list


def remote_repo_hashes():

    # Clone the repo from Github
    repo_url = "https://github.com/airrloww/to_test_another_repo"
    cloned_repo = Repo.clone_from(repo_url, remote_repo)

    # Get a list of all commits on the Main branch
    commits = list(cloned_repo.iter_commits('main'))

    for i in commits:
        remote_hash_list.append(i)
        # print(remote_hash_list)
        # print(i)

    print(f" [+] Remote hash count: {len(commits)}")


def main():
    local_repo_hashes()
    remote_repo_hashes()
    # remove_dir()

    if len(local_hash_list) == len(remote_hash_list):
        print("[+] There are no new commits")
    elif len(local_hash_list) < len(remote_hash_list):
        print(f"[+] There are {len(remote_hash_list) - len(local_hash_list)} new commits!")

if __name__ == '__main__':
    main()