"""
This type stub file was generated by pyright.
"""

import abc
from typing import Awaitable, Callable, List, Optional
from bleak.backends.device import BLEDevice

class AdvertisementData:
    """
    Wrapper around the advertis"""
    def __init__(self, **kwargs) -> None:
        """
        Keyword Args:
         """
        ...
    
    def __repr__(self) -> str:
        ...
    


AdvertisementDataCallback = Callable[[BLEDevice, AdvertisementData], Optional[Awaitable[None]]],
AdvertisementDataFilter = Callable[[BLEDevice, AdvertisementData], bool],
class BaseBleakScanner(abc.ABC):
    """
    Interface for Bleak Bluetoo"""
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    async def __aenter__(self): # -> Self@BaseBleakScanner:
        ...
    
    async def __aexit__(self, exc_type, exc_val, exc_tb): # -> None:
        ...
    
    @classmethod
    async def discover(cls, timeout=..., **kwargs) -> List[BLEDevice]:
        """Scan continuously for ``timeout`"""
        ...
    
    def register_detection_callback(self, callback: Optional[AdvertisementDataCallback]) -> None:
        """Register a callback that is call"""
        ...
    
    @abc.abstractmethod
    async def start(self):
        """Start scanning for devices"""
        ...
    
    @abc.abstractmethod
    async def stop(self):
        """Stop scanning for devices"""
        ...
    
    @abc.abstractmethod
    def set_scanning_filter(self, **kwargs):
        """Set scanning filter for the Blea"""
        ...
    
    @property
    @abc.abstractmethod
    def discovered_devices(self) -> List[BLEDevice]:
        """Gets the devices registered by t"""
        ...
    
    async def get_discovered_devices(self) -> List[BLEDevice]:
        """Gets the devices registered by t"""
        ...
    
    @classmethod
    async def find_device_by_address(cls, device_identifier: str, timeout: float = ..., **kwargs) -> Optional[BLEDevice]:
        """A convenience method for obtaini"""
        ...
    
    @classmethod
    async def find_device_by_filter(cls, filterfunc: AdvertisementDataFilter, timeout: float = ..., **kwargs) -> Optional[BLEDevice]:
        """A convenience method for obtaini"""
        ...
    


