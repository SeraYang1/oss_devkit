# run with `python -m unittest -v test`
import unittest
import os
import subprocess
import shutil

class TestGitHubMethods(object):

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
    # TODO - how to know which file I'm in
    def test_sync(self):
        curr_dir = os.getcwd()
        curr_dir = curr_dir[len(curr_dir)-17:]
        if not curr_dir == "file/OutsideHacks":
            os.chdir("file/OutsideHacks")
        dir = ".git/git-hub/pull-requests.toml"
        self.assertTrue(os.path.isfile(dir))

    # Checks the general case for search prints out everything
    def test_search(self):
        curr_dir = os.getcwd()
        curr_dir = curr_dir[len(curr_dir)-17:]
        if not curr_dir == "file/OutsideHacks":
            os.chdir("file/OutsideHacks")
        p = subprocess.run(["git", "hub", "search"], stdout=subprocess.PIPE)
        output = p.stdout.decode("utf-8")
        self.assertEqual(8, len(output.split("\n")))

    # Checks search works with a keyword
    def test_search_keyword(self):
        curr_dir = os.getcwd()
        curr_dir = curr_dir[len(curr_dir)-17:]
        if not curr_dir == "file/OutsideHacks":
            os.chdir("file/OutsideHacks")
        p = subprocess.run(["git", "hub", "search", "space"], stdout=subprocess.PIPE)
        output = p.stdout.decode("utf-8").split("\n")
        output = output[:-1]
        self.assertEqual(2, len(output))
        self.assertEqual(output[0], "3  C  SeraYang1/test 'adding spaces' : 2017-09-18")
        self.assertEqual(output[1], "4  C  SeraYang1/space 'space' : 2017-08-28")



    os.chdir("../..")

if __name__ == '__main__':
    unittest.main()
