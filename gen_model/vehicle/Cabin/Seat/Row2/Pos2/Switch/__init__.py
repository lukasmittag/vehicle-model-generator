#!/usr/bin/env python3

"""Switch model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointBoolean,
    Model,
)

from vehicle.Cabin.Seat.Row2.Pos2.Switch.Backrest import Backrest
from vehicle.Cabin.Seat.Row2.Pos2.Switch.Headrest import Headrest
from vehicle.Cabin.Seat.Row2.Pos2.Switch.Massage import Massage
from vehicle.Cabin.Seat.Row2.Pos2.Switch.Seating import Seating


class Switch(Model):
    """Switch model.

    Attributes
    ----------
    Backrest: branch
        Describes switches related to the backrest of the seat.

    Headrest: branch
        Switches for SingleSeat.Headrest.

    IsBackwardEngaged: actuator
        Seat backward switch engaged (SingleSeat.Position).

    IsCoolerEngaged: actuator
        Cooler switch for Seat heater (SingleSeat.Heating).

    IsDownEngaged: actuator
        Seat down switch engaged (SingleSeat.Height).

    IsForwardEngaged: actuator
        Seat forward switch engaged (SingleSeat.Position).

    IsTiltBackwardEngaged: actuator
        Tilt backward switch engaged (SingleSeat.Tilt).

    IsTiltForwardEngaged: actuator
        Tilt forward switch engaged (SingleSeat.Tilt).

    IsUpEngaged: actuator
        Seat up switch engaged (SingleSeat.Height).

    IsWarmerEngaged: actuator
        Warmer switch for Seat heater (SingleSeat.Heating).

    Massage: branch
        Switches for SingleSeat.Massage.

    Seating: branch
        Describes switches related to the seating of the seat.

    """

    def __init__(self, name, parent):
        """Create a new Switch model."""
        super().__init__(parent)
        self.name = name

        self.Backrest = Backrest("Backrest", self)
        self.Headrest = Headrest("Headrest", self)
        self.IsBackwardEngaged = DataPointBoolean("IsBackwardEngaged", self)
        self.IsCoolerEngaged = DataPointBoolean("IsCoolerEngaged", self)
        self.IsDownEngaged = DataPointBoolean("IsDownEngaged", self)
        self.IsForwardEngaged = DataPointBoolean("IsForwardEngaged", self)
        self.IsTiltBackwardEngaged = DataPointBoolean("IsTiltBackwardEngaged", self)
        self.IsTiltForwardEngaged = DataPointBoolean("IsTiltForwardEngaged", self)
        self.IsUpEngaged = DataPointBoolean("IsUpEngaged", self)
        self.IsWarmerEngaged = DataPointBoolean("IsWarmerEngaged", self)
        self.Massage = Massage("Massage", self)
        self.Seating = Seating("Seating", self)
