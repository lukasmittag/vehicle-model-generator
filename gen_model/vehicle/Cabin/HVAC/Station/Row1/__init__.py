#!/usr/bin/env python3

"""Row1 model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    Model,
)

from vehicle.Cabin.HVAC.Station.Row1.Left import Left
from vehicle.Cabin.HVAC.Station.Row1.Right import Right


class Row1(Model):
    """Row1 model.

    Attributes
    ----------
    Left: branch
        HVAC for single station in the vehicle

    Right: branch
        HVAC for single station in the vehicle

    """

    def __init__(self, name, parent):
        """Create a new Row1 model."""
        super().__init__(parent)
        self.name = name

        self.Left = Left("Left", self)
        self.Right = Right("Right", self)
