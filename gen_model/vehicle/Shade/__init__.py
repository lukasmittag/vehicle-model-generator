#!/usr/bin/env python3

"""Shade model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointBoolean,
    Model,
)


class Shade(Model):
    """Shade model.

    Attributes
    ----------
    Move: actuator
        0 = shade down; 1 = shade up

    """

    def __init__(self, name, parent):
        """Create a new Shade model."""
        super().__init__(parent)
        self.name = name

        self.Move = DataPointBoolean("Move", self)
