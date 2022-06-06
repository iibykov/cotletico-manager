import unittest
from src.event_generator import MarkovChain, EventGenerator
                #     C    I    G    C
transition_matrix = [[0.1, 0.3, 0.1, 0.5],  # C
                     [0.0, 0.0, 0.0, 1.0],  # I
                     [0.0, 0.0, 0.0, 1.0],  # G
                     [0.1, 0.15, 0.05, 0.7]] # Con


class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        """
        The probability values represent the probability of the system
        going from the state in the row to the states mentioned in the columns
        """
        self.match_chain = MarkovChain(transition_matrix, states=['Corner', 'Indirect_Kick', 'Goal', 'Continuation'])

    def test_next_state(self):
        self.assertEqual(self.match_chain.next_state(current_state='Indirect_Kick'), 'Continuation')
        self.assertEqual(self.match_chain.next_state(current_state='Goal'), 'Continuation')

        self.assertNotEqual(self.match_chain.next_state(current_state='Indirect_Kick'), 'Corner')
        self.assertNotEqual(self.match_chain.next_state(current_state='Indirect_Kick'), 'Indirect_Kick')
        self.assertNotEqual(self.match_chain.next_state(current_state='Indirect_Kick'), 'Goal')

        self.assertNotEqual(self.match_chain.next_state(current_state='Goal'), 'Corner')
        self.assertNotEqual(self.match_chain.next_state(current_state='Goal'), 'Indirect_Kick')
        self.assertNotEqual(self.match_chain.next_state(current_state='Goal'), 'Goal')

        self.assertIn(self.match_chain.next_state(current_state='Corner'), ['Corner', 'Indirect_Kick', 'Goal',
                                                                            'Continuation'])


class TestEventGenerator(unittest.TestCase):
    def setUp(self):
        """
        The probability values represent the probability of the system
        going from the state in the row to the states mentioned in the columns
        """
        self.match_chain = EventGenerator(transition_matrix, states=['Corner', 'Indirect_Kick', 'Goal', 'Continuation'])

    def test_generate_events(self):
        self.assertEqual(len(self.match_chain.generate_events(current_state='Corner', no=15)), 15)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
