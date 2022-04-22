"""
This type stub file was generated by pyright.
"""

import os
from bleak.__version__ import __version__
from bleak.backends.bluezdbus import check_bluez_version
from bleak.exc import BleakError
from bleak.backends.p4android.scanner import BleakScannerP4Android as BleakScanner
from bleak.backends.p4android.client import BleakClientP4Android as BleakClient

"""Top-level package for bleak."""
__author__ = ...
__email__ = ...
_on_rtd = ...
_on_ci = ...
_logger = ...
if bool(os.environ.get("BLEAK_LOGGING", False)):
    FORMAT = ...
    handler = ...
if _on_rtd:
    ...
else:
    ...
if not_on_rtd:
    discover = ...
def cli(): # -> None:
    ...

if __name__ == "__main__":
    ...
