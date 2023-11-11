#!/usr/bin/env python3

"""Row3 model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    Model,
)

from vehicle.Cabin.HVAC.Station.Row3.Left import Left
from vehicle.Cabin.HVAC.Station.Row3.Right import Right


class Row3(Model):
    """Row3 model.

    Attributes
    ----------
    Left: branch
        HVAC for single station in the vehicle

    Right: branch
        HVAC for single station in the vehicle

    """

    def __init__(self, name, parent):
        """Create a new Row3 model."""
        super().__init__(parent)
        self.name = name

        self.Left = Left("Left", self)
        self.Right = Right("Right", self)
