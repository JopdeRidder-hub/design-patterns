from __future__ import annotations
from abc import ABC
from enum import Enum


class Status(Enum):
    """
    Enum representing the status of a device.
    """

    STAND_BY = "Stand-by"
    OFF = "Off"
    ON = "On"
    UNKNOWN = "Unknown"


class BridgeController:
    """
    Controller class to manage a Device, providing methods to toggle power,
    adjust volume, and change channels.
    """

    def __init__(self, device: Device) -> None:
        """
        Initialize the BridgeController with a specific device.

        Args:
            device (Device): The device to be controlled.
        """
        self.device = device

    def toggle_power(self) -> None:
        """
        Toggle the power status of the device.
        """
        if self.device.status != Status.ON:
            self.device.turn_on()
            return

        if self.device.status == Status.ON:
            self.device.turn_off()

    def volume_up(self) -> None:
        """
        Increase the volume of the device by 1.
        """
        self.device.set_volume(self.device.volume + 1)

    def volume_down(self) -> None:
        """
        Decrease the volume of the device by 1.
        """
        self.device.set_volume(self.device.volume - 1)

    def channel_up(self) -> None:
        """
        Increase the channel of the device by 1.
        """
        self.device.set_channel(self.device.channel + 1)

    def channel_down(self) -> None:
        """
        Decrease the channel of the device by 1.
        """
        self.device.set_channel(self.device.channel - 1)

    def __str__(self) -> str:
        """
        Return a string representation of the controller.

        Returns:
            str: Description of the controller and its associated device.
        """
        return f"I'm a {self.device.__str__()} remote"


class Device(ABC):
    """
    Abstract base class representing a generic device with basic functionality
    such as turning on/off, adjusting volume, and changing channels.
    """

    status: Status = Status.UNKNOWN
    volume: int = 9
    channel: int = 1

    def turn_on(self) -> None:
        """
        Turn the device on and set its status to ON.
        """
        print("Turning on device..")
        self.status = Status.ON

    def turn_off(self) -> None:
        """
        Turn the device off and set its status to OFF.
        """
        print("Turning off device..")
        self.status = Status.OFF

    def set_standby(self) -> None:
        """
        Set the device status to STAND_BY.
        """
        print("Setting standby device..")
        self.status = Status.STAND_BY

    def set_volume(self, volume: int) -> None:
        """
        Set the device's volume to the specified level.

        Args:
            volume (int): The new volume level.
        """
        self.volume = volume

    @property
    def get_volume(self) -> int:
        """
        Get the current volume level of the device.

        Returns:
            int: The current volume level.
        """
        return self.volume

    def set_channel(self, channel: int) -> None:
        """
        Set the device's channel to the specified channel number.

        Args:
            channel (int): The new channel number.
        """
        self.channel = channel

    @property
    def get_channel(self) -> int:
        """
        Get the current channel number of the device.

        Returns:
            int: The current channel number.
        """
        return self.channel
