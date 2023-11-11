#!/usr/bin/env python3

"""Mirrors model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    Model,
)

from vehicle.Body.Mirrors.Left import Left
from vehicle.Body.Mirrors.Right import Right


class Mirrors(Model):
    """Mirrors model.

    Attributes
    ----------
    Left: branch
        All mirrors.

    Right: branch
        All mirrors.

    """

    def __init__(self, name, parent):
        """Create a new Mirrors model."""
        super().__init__(parent)
        self.name = name

        self.Left = Left("Left", self)
        self.Right = Right("Right", self)
