#!/usr/bin/env python3

"""Pos3 model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointInt8,
    DataPointUint16,
    DataPointUint8,
    Model,
)

from vehicle.Cabin.Seat.Row1.Pos3.Airbag import Airbag
from vehicle.Cabin.Seat.Row1.Pos3.Backrest import Backrest
from vehicle.Cabin.Seat.Row1.Pos3.Headrest import Headrest
from vehicle.Cabin.Seat.Row1.Pos3.Occupant import Occupant
from vehicle.Cabin.Seat.Row1.Pos3.Seating import Seating
from vehicle.Cabin.Seat.Row1.Pos3.Switch import Switch


class Pos3(Model):
    """Pos3 model.

    Attributes
    ----------
    Airbag: branch
        Airbag signals.

    Backrest: branch
        Describes signals related to the backrest of the seat.

    Headrest: branch
        Headrest settings.

    Heating: actuator
        Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat.

        Value range: [-100, 100]
        Unit: percent
    Height: actuator
        Seat position on vehicle z-axis. Position is relative within available movable range of the seating. 0 = Lowermost position supported.

        Value range: [0, ]
        Unit: mm
    IsBelted: sensor
        Is the belt engaged.

    IsOccupied: sensor
        Does the seat have a passenger in it.

    Massage: actuator
        Seat massage level. 0 = off. 100 = max massage.

        Value range: [0, 100]
        Unit: percent
    Occupant: branch
        Occupant data.

    Position: actuator
        Seat position on vehicle x-axis. Position is relative to the frontmost position supported by the seat. 0 = Frontmost position supported.

        Value range: [0, ]
        Unit: mm
    Seating: branch
        Describes signals related to the seating/base of the seat.

        Seating is here considered as the part of the seat that supports the thighs. Additional cushions (if any) for support of lower legs is not covered by this branch.

    Switch: branch
        Seat switch signals

    Tilt: actuator
        Tilting of seat relative to vehicle z-axis. 0 = seating is flat, seat and vehicle z-axis are parallel. Positive degrees = seat tilted backwards, seat z-axis is tilted backward.

        Unit: degrees
    """

    def __init__(self, name, parent):
        """Create a new Pos3 model."""
        super().__init__(parent)
        self.name = name

        self.Airbag = Airbag("Airbag", self)
        self.Backrest = Backrest("Backrest", self)
        self.Headrest = Headrest("Headrest", self)
        self.Heating = DataPointInt8("Heating", self)
        self.Height = DataPointUint16("Height", self)
        self.IsBelted = DataPointBoolean("IsBelted", self)
        self.IsOccupied = DataPointBoolean("IsOccupied", self)
        self.Massage = DataPointUint8("Massage", self)
        self.Occupant = Occupant("Occupant", self)
        self.Position = DataPointUint16("Position", self)
        self.Seating = Seating("Seating", self)
        self.Switch = Switch("Switch", self)
        self.Tilt = DataPointFloat("Tilt", self)
