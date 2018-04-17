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

    # Checks that `git hub info {pr_num}` fetches all necessary info
    def test_info(self):
        p = subprocess.run(["git", "hub", "info", "5"], stdout=subprocess.PIPE)
        output = p.stdout.decode("utf-8").split("\n")
        output = output[:-1]
        self.assertEqual(8, len(output))
        self.assertEqual(output[0], "5  O  SeraYang1/another-pull 'empty'")
        self.assertEqual(output[1], "-Reviewers: [] ")
        self.assertEqual(output[2], "-Assignees: ['SeraYang1'] ")
        self.assertEqual(output[3], "-Labels: ['bug', 'enhancement'] ")
        self.assertEqual(output[4], "-Milestones: foxtrot ")
        self.assertEqual(output[5], "-Comment count: 3 ")
        self.assertEqual(output[6], "-Created at: 2017-09-02 ")
        self.assertEqual(output[7], "-Last modified: 2018-04-04")

    # Checks that `git hub render` creates an output.html
    def test_render(self):
        if os.path.isfile("output.html"):
            os.remove("output.html")
        p = subprocess.run(["git", "hub", "render"])
        self.assertTrue(os.path.isfile("output.html"))


if __name__ == '__main__':
    unittest.main()
