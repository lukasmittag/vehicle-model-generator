#!/usr/bin/env python3

"""Backrest model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointBoolean,
    Model,
)

from vehicle.Cabin.Seat.Row1.Pos1.Switch.Backrest.Lumbar import Lumbar
from vehicle.Cabin.Seat.Row1.Pos1.Switch.Backrest.SideBolster import SideBolster


class Backrest(Model):
    """Backrest model.

    Attributes
    ----------
    IsReclineBackwardEngaged: actuator
        Backrest recline backward switch engaged (SingleSeat.Backrest.Recline).

    IsReclineForwardEngaged: actuator
        Backrest recline forward switch engaged (SingleSeat.Backrest.Recline).

    Lumbar: branch
        Switches for SingleSeat.Backrest.Lumbar.

    SideBolster: branch
        Switches for SingleSeat.Backrest.SideBolster.

    """

    def __init__(self, name, parent):
        """Create a new Backrest model."""
        super().__init__(parent)
        self.name = name

        self.IsReclineBackwardEngaged = DataPointBoolean("IsReclineBackwardEngaged", self)
        self.IsReclineForwardEngaged = DataPointBoolean("IsReclineForwardEngaged", self)
        self.Lumbar = Lumbar("Lumbar", self)
        self.SideBolster = SideBolster("SideBolster", self)
