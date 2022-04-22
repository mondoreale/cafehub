"""
This type stub file was generated by pyright.
"""

import uuid
from typing import Callable, Optional, Union
from bleak.backends.device import BLEDevice
from bleak.backends.service import BleakGATTServiceCollection
from bleak.backends.client import BaseBleakClient
from bleak.backends.p4android.characteristic import BleakGATTCharacteristicP4Android
from bleak.backends.p4android.descriptor import BleakGATTDescriptorP4Android
from jnius import java_method
from . import utils

"""
BLE Client for python-for-andro"""
logger = ...
class BleakClientP4Android(BaseBleakClient):
    """A python-for-android Bleak Clien"""
    def __init__(self, address_or_ble_device: Union[BLEDevice, str], **kwargs) -> None:
        ...
    
    def __del__(self): # -> None:
        ...
    
    async def connect(self, **kwargs) -> bool:
        """Connect to the specified GATT se"""
        ...
    
    async def disconnect(self) -> bool:
        """Disconnect from the specified GA"""
        ...
    
    async def pair(self, *args, **kwargs) -> bool:
        """Pair with the peripheral.

     """
        ...
    
    async def unpair(self) -> bool:
        """Unpair with the peripheral.

   """
        ...
    
    @property
    def is_connected(self) -> bool:
        """Check connection status between """
        ...
    
    @property
    def mtu_size(self) -> Optional[int]:
        ...
    
    async def get_services(self) -> BleakGATTServiceCollection:
        """Get all services registered for """
        ...
    
    async def read_gatt_char(self, char_specifier: Union[BleakGATTCharacteristicP4Android, int, str, uuid.UUID], **kwargs) -> bytearray:
        """Perform read operation on the sp"""
        ...
    
    async def read_gatt_descriptor(self, desc_specifier: Union[BleakGATTDescriptorP4Android, str, uuid.UUID], **kwargs) -> bytearray:
        """Perform read operation on the sp"""
        ...
    
    async def write_gatt_char(self, char_specifier: Union[BleakGATTCharacteristicP4Android, int, str, uuid.UUID], data: bytearray, response: bool = ...) -> None:
        """Perform a write operation on the"""
        ...
    
    async def write_gatt_descriptor(self, desc_specifier: Union[BleakGATTDescriptorP4Android, str, uuid.UUID], data: bytearray) -> None:
        """Perform a write operation on the"""
        ...
    
    async def start_notify(self, char_specifier: Union[BleakGATTCharacteristicP4Android, int, str, uuid.UUID], callback: Callable[[int, bytearray], None], **kwargs) -> None:
        """Activate notifications/indicatio"""
        ...
    
    async def stop_notify(self, char_specifier: Union[BleakGATTCharacteristicP4Android, int, str, uuid.UUID]) -> None:
        """Deactivate notification/indicati"""
        ...
    


class _PythonBluetoothGattCallback(utils.AsyncJavaCallbacks):
    __javainterfaces__ = ...
    def __init__(self, client, loop) -> None:
        ...
    
    def result_state(self, status, resultApi, *data): # -> None:
        ...
    
    @java_method("(II)V")
    def onConnectionStateChange(self, status, new_state): # -> None:
        ...
    
    @java_method("(II)V")
    def onMtuChanged(self, mtu, status): # -> None:
        ...
    
    @java_method("(I)V")
    def onServicesDiscovered(self, status): # -> None:
        ...
    
    @java_method("(I[B)V")
    def onCharacteristicChanged(self, handle, value): # -> None:
        ...
    
    @java_method("(II[B)V")
    def onCharacteristicRead(self, handle, status, value): # -> None:
        ...
    
    @java_method("(II)V")
    def onCharacteristicWrite(self, handle, status): # -> None:
        ...
    
    @java_method("(Ljava/lang/String;I[B)V")
    def onDescriptorRead(self, uuid, status, value): # -> None:
        ...
    
    @java_method("(Ljava/lang/String;I)V")
    def onDescriptorWrite(self, uuid, status): # -> None:
        ...
    


