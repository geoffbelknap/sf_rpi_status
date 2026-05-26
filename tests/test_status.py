import unittest

from sf_rpi_status.status import _is_virtual_interface


class NetworkInterfaceFilterTest(unittest.TestCase):
    def test_filters_noisy_virtual_interfaces(self):
        for name in ("lo", "docker0", "vethabc123", "br-aabbcc", "virbr0"):
            self.assertTrue(_is_virtual_interface(name))

    def test_keeps_physical_style_interfaces(self):
        for name in ("eth0", "enp1s0", "wlan0", "usb0"):
            self.assertFalse(_is_virtual_interface(name))


if __name__ == "__main__":
    unittest.main()
