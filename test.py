# run with `python -m unittest test`
import unittest
import os
import subprocess
import shutil

class TestStringMethods(unittest.TestCase):

    shutil.rmtree("file")
    os.mkdir("file")
    os.chdir("file")
    p = subprocess.run(["git", "clone", "https://github.com/SeraYang1/OutsideHacks.git"])
    os.chdir("OutsideHacks")
    p = subprocess.run(["git", "hub", "sync"])

    def test_sync(self):
        dir = ".git/git-hub/pull-requests.toml"
        self.assertTrue(os.path.isdir(dir))

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    os.chdir("../..")

suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
