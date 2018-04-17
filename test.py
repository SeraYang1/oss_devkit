# run with `python -m unittest -v test`
import unittest
import os
import subprocess

class TestGitHubMethods(unittest.TestCase):

    # Initialize by syncing down all the info.
    if not os.path.isdir("file"):
        os.mkdir("file")
    os.chdir("file")
    if not os.path.isdir("OutsideHacks"):
        p = subprocess.run(["git", "clone", "https://github.com/SeraYang1/OutsideHacks.git"])
    os.chdir("OutsideHacks")
    path = ".git/git-hub/pull-requests.toml"
    if not os.path.isfile(path) or os.stat(path).st_size == 0:
        p = subprocess.run(["git", "hub", "sync"])

    # Checks to see if sync properly created the pull-requests.toml file
    def test_sync(self):
        dir = ".git/git-hub/pull-requests.toml"
        self.assertTrue(os.path.isfile(dir))

    # Checks the general case for search prints out everything
    def test_search(self):
        p = subprocess.run(["git", "hub", "search"], stdout=subprocess.PIPE)
        output = p.stdout.decode("utf-8")
        self.assertEqual(8, len(output.split("\n")))

    # Checks search works with a keyword
    def test_search_keyword(self):
        p = subprocess.run(["git", "hub", "search", "space"], stdout=subprocess.PIPE)
        output = p.stdout.decode("utf-8").split("\n")
        output = output[:-1]
        self.assertEqual(2, len(output))
        self.assertEqual(output[0], "3  C  SeraYang1/test 'adding spaces' : 2017-09-18")
        self.assertEqual(output[1], "4  C  SeraYang1/space 'space' : 2017-08-28")

    # Checks the -o (open or closed) and -b (branch) search terms work
    def test_search_open_and_branch(self):
        p = subprocess.run(["git", "hub", "search", "-o", "closed", "-b", "space"], stdout=subprocess.PIPE)
        output = p.stdout.decode("utf-8").split("\n")
        output = output[:-1]
        self.assertEqual(1, len(output))
        self.assertEqual(output[0], "4  C  SeraYang1/space 'space' : 2017-08-28")

    # Checks the -n (number) search term works
    def test_search_number(self):
        p = subprocess.run(["git", "hub", "search", "-n", "7"], stdout=subprocess.PIPE)
        output = p.stdout.decode("utf-8").split("\n")
        output = output[:-1]
        self.assertEqual(1, len(output))
        self.assertEqual(output[0], "7  O  SeraYang1/new_branch 'New branch' : 2018-04-10")


if __name__ == '__main__':
    unittest.main()
