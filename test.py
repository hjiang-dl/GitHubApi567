import unittest
import requests
from unittest import mock
import hwjh
from hwjh import get_information

class Testget_information(unittest.TestCase):
    @mock.path('hwjh.get_information')
    def testget_information(self,mockedget):
        list1 = ['Repo: csp Commits number: 2', 
                 'Repo: hellogitworld Commits number: 30',
                 'Repo: helloworld Commits number: 6',
                 'Repo: Mocks Commits number: 10', 
                 'Repo: Project1 Commits number: 2', 
                 'Repo: richkempinski.github.io Commits number: 9',
                 'Repo: threads-of-life Commits number: 1',
                 'Repo: try_nbdev Commits number: 2',
                 'Repo: try_nbdev2 Commits number: 5']
        mockedget.return_value = list1
        self.assertEqual(hwjh.get_information("momotech"), list1[0])

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

