from mo import l_u


args = l_u.args
python = l_u.python
git = l_u.git
index_url = l_u.index_url
dir_repos = l_u.dir_repos




commit_hash = l_u.commit_hash
git_tag = l_u.git_tag

run = l_u.run
is_installed = l_u.is_installed
repo_dir = l_u.repo_dir

run_pip = l_u.run_pip
check_run_python = l_u.check_run_python
git_clone = l_u.git_clone


git_pull_recursive = l_u.git_pull_recursive
run_extension_installer = l_u.run_extension_installer
prepare_environment = l_u.prepare_environment

configure_for_tests = l_u.configure_for_tests
start = l_u.start



def main():
    if not args.skip_prepare_environment:
        prepare_environment()

    if args.test_server:
        configure_for_tests()

    start()


if __name__ == "__main__":
    main()
