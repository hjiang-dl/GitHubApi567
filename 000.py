import unittest
from hwjh import get_information

class Testget_information(unittest.TestCase):
    def testget_information(self):
        list1 = ['Repo: csp Commits number: 2', 
                 'Repo: hellogitworld Commits number: 30',
                 'Repo: helloworld Commits number: 6',
                 'Repo: Mocks Commits number: 10', 
                 'Repo: Project1 Commits number: 2', 
                 'Repo: richkempinski.github.io Commits number: 9',
                 'Repo: threads-of-life Commits number: 1',
                 'Repo: try_nbdev Commits number: 2',
                 'Repo: try_nbdev2 Commits number: 5']
        self.assertEqual(get_information("richkempinski"), list1)
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)

