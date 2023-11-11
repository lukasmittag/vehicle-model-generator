#!/usr/bin/env python3

"""DriverSide model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointString,
    Model,
)

from vehicle.Window.Row2.DriverSide.Sensor import Sensor


class DriverSide(Model):
    """DriverSide model.

    Attributes
    ----------
    Action: actuator


    Sensor: branch


    """

    def __init__(self, name, parent):
        """Create a new DriverSide model."""
        super().__init__(parent)
        self.name = name

        self.Action = DataPointString("Action", self)
        self.Sensor = Sensor("Sensor", self)
