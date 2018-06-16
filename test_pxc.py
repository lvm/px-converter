import pxc
import unittest

class TestPXC(unittest.TestCase):
    """
    PXC tests
    """

    def test_cm_to_px_72dpi(self):
        """
        Test convertion from cm to px in 72dpi.
        For Screens.
        """
        result = pxc.to_pixel(12, 72) # 12cm, 72dpi
        self.assertEqual(result, 340)

    def test_cm_to_px_300dpi(self):
        """
        Test convertion from cm to px in 300dpi
        For Printing.
        """
        result = pxc.to_pixel(12, 300) # 12cm, 300dpi
        self.assertEqual(result, 1417)

    def test_px_to_cm_72dpi(self):
        """
        Test convertion from px to cm in 72dpi.
        For Screens.
        """
        result = pxc.to_centimeter(340, 72) # 12cm, 72dpi
        self.assertEqual(result, 12)

    def test_px_to_cm_300dpi(self):
        """
        Test convertion from px to cm in 300dpi
        For Printing.
        """
        result = pxc.to_centimeter(1417, 300) # 12cm, 300dpi
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()
