#!/usr/bin/env python3

"""Music model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointBoolean,
    Model,
)


class Music(Model):
    """Music model.

    Attributes
    ----------
    Tired: actuator
        1 when played, 0 when not.

    """

    def __init__(self, name, parent):
        """Create a new Music model."""
        super().__init__(parent)
        self.name = name

        self.Tired = DataPointBoolean("Tired", self)
