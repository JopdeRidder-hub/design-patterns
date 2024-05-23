from bridges.bridge import Device


class Tv(Device):
    """
    A concrete implementation of Device representing a TV.
    """

    def __str__(self) -> str:
        """
        Return a string representation of the TV.

        Returns:
            str: Description of the device as "TV".
        """
        return "TV"


class Radio(Device):
    """
    A concrete implementation of Device representing a Radio.
    """

    def __str__(self) -> str:
        """
        Return a string representation of the Radio.

        Returns:
            str: Description of the device as "Radio".
        """
        return "Radio"
