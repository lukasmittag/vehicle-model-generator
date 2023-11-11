#!/usr/bin/env python3

"""Sensor model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointFloat,
    Model,
)


class Sensor(Model):
    """Sensor model.

    Attributes
    ----------
    Position: sensor


    """

    def __init__(self, name, parent):
        """Create a new Sensor model."""
        super().__init__(parent)
        self.name = name

        self.Position = DataPointFloat("Position", self)
