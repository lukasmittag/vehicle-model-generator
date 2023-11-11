#!/usr/bin/env python3

"""Sensor model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointUint8,
    Model,
)


class Sensor(Model):
    """Sensor model.

    Attributes
    ----------
    Angle: sensor


    """

    def __init__(self, name, parent):
        """Create a new Sensor model."""
        super().__init__(parent)
        self.name = name

        self.Angle = DataPointUint8("Angle", self)
