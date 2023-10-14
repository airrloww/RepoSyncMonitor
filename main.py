from git import Repo, exc
import shutil

def remove_dir(path):
    """Removes a directory."""
    try:
        shutil.rmtree(path)
        print("Directory removed successfully")
    except OSError as o:
        print(f"Error, {o.strerror}: {path}")


def get_local_repo_hashes(repo_name):
    """Fetch hashes from local repository."""

    local_repo = Repo(repo_name)
    commits = list(local_repo.iter_commits('main'))
    print(f" [+] Local hash count: {len(commits)}")
    return [commit for commit in commits]


def get_remote_repo_hashes(repo_url, path_to_clone):
    """Fetch hashes from remote repository."""
    try:
        cloned_repo = Repo.clone_from(repo_url, path_to_clone)
        commits = list(cloned_repo.iter_commits('main'))
        print(f" [+] Remote hash count: {len(commits)}")
        return [commit for commit in commits]
    except exc.GitCommandError as e:
        print(f"Error: {str(e)}")
        return []


def main():
    repo_name = "" # Insert dir name
    remote_repo = f"new_{repo_name}"
    repo_url = "" # Insert repository URL
    
    local_hashes = get_local_repo_hashes(repo_name)
    remote_hashes = get_remote_repo_hashes(repo_url, remote_repo)

    if len(local_hashes) == len(remote_hashes):
        print("[+] There are no new commits")
    elif len(local_hashes) < len(remote_hashes):
        print(f"[+] There are {len(remote_hashes) - len(local_hashes)} new commits!")

    remove_dir(remote_repo)

if __name__ == '__main__':
    main()
