import unittest
from team.feed.model import FeedItem

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        item = FeedItem(item_name="coolmessage", item_type=1, item_body="Hello World!")
        self.assertEqual(item.item_body, 'Hello World!')

if __name__ == '__main__':
    unittest.main()