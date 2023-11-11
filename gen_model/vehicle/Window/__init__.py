#!/usr/bin/env python3

"""Window model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    Model,
)

from vehicle.Window.Row1 import Row1
from vehicle.Window.Row2 import Row2


class Window(Model):
    """Window model.

    Attributes
    ----------
    Row2: branch


    Row1: branch


    """

    def __init__(self, name, parent):
        """Create a new Window model."""
        super().__init__(parent)
        self.name = name

        self.Row2 = Row2("Row2", self)
        self.Row1 = Row1("Row1", self)
