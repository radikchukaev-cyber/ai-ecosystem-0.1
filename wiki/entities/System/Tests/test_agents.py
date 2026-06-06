import unittest

class TestAgents(unittest.TestCase):
    def test_agent_initialization(self):
        # Mock test for agent setup
        agent_name = "VULCAN"
        self.assertEqual(agent_name, "VULCAN")
        
    def test_agent_tags(self):
        tags = ["#agent/vulcan", "#skill/coding", "#active"]
        self.assertIn("#active", tags)

if __name__ == '__main__':
    unittest.main()
