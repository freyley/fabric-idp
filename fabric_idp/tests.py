from api import dir, symlink, user
from unittest import TestCase, main
from fabric.api import local, settings
from os.path import  exists
import os.path

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

class DirTests(TestCase):
    def setUp(self):
        with settings(warn_only=True):
            local('rm -r %s/tmp' % CURRENT_DIR)

        local('mkdir %s/tmp' % CURRENT_DIR)
        self.tmpfilename =  "%s/tmp/test_dir"

    def test_dir(self):
        self.assertFalse(exists(self.tmpfilename))
        dir(self.tmpfilename)
        self.assertTrue(exists(self.tmpfilename))
        dir(self.tmpfilename)
        self.assertTrue(exists(self.tmpfilename))

if __name__=='__main__':
    main()
