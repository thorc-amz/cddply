#from .context import newworld

import unittest

from newworld.ring import Ring

class DefaultRingDiameterTestCase(unittest.TestCase):
    def test_default_ring_diameter(self):
        ring = Ring()
        self.assertEqual(ring.diameter, 1)
