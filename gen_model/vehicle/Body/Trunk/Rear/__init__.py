#!/usr/bin/env python3

"""Rear model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointBoolean,
    Model,
)


class Rear(Model):
    """Rear model.

    Attributes
    ----------
    IsLocked: actuator
        Is trunk locked or unlocked. True = Locked. False = Unlocked.

    IsOpen: actuator
        Trunk open or closed. True = Open. False = Closed.

    """

    def __init__(self, name, parent):
        """Create a new Rear model."""
        super().__init__(parent)
        self.name = name

        self.IsLocked = DataPointBoolean("IsLocked", self)
        self.IsOpen = DataPointBoolean("IsOpen", self)
