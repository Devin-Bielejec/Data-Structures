import unittest
from lru_cache import LRUCache


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(3)

    # def test_cache_overwrite_appropriately(self):
    #     self.cache.set('item1', 'a')
    #     self.cache.set('item2', 'b')
    #     self.cache.set('item3', 'c')

    #     self.cache.set('item2', 'z')

    #     self.assertEqual(self.cache.get('item1'), 'a')
    #     self.assertEqual(self.cache.get('item2'), 'z')

    def test_cache_insertion_and_retrieval(self):
        self.cache.set('item1', 'a')
        self.cache.set('item2', 'b')
        self.cache.set('item3', 'c')
        self.assertEqual(self.cache.dll.head.value, "item3")
        self.assertEqual(self.cache.dll.tail.value, "item1")
        #3, 2, 1
        self.assertEqual(self.cache.get('item1'), 'a')
        self.assertEqual(self.cache.dll.head.value, "item1")
        self.assertEqual(self.cache.dll.tail.value, "item2")
        #1, 3, 2

        self.cache.set('item4', 'd')
        self.assertEqual(self.cache.dll.head.value, "item4")
        # remove 2, add 4, to make 4, 1, 3
        self.assertEqual(self.cache.get('item1'), 'a')
        self.assertEqual(self.cache.get('item3'), 'c')
        self.assertEqual(self.cache.get('item4'), 'd')
        self.assertIsNone(self.cache.get('item2'))

    def test_cache_nonexistent_retrieval(self):
        self.assertIsNone(self.cache.get('nonexistent'))


if __name__ == '__main__':
    unittest.main()
