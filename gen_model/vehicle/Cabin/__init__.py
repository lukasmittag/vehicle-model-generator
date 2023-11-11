#!/usr/bin/env python3

"""Cabin model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointUint8,
    DataPointUint8Array,
    Model,
)

from vehicle.Cabin.Convertible import Convertible
from vehicle.Cabin.Door import Door
from vehicle.Cabin.HVAC import HVAC
from vehicle.Cabin.Infotainment import Infotainment
from vehicle.Cabin.Lights import Lights
from vehicle.Cabin.RearShade import RearShade
from vehicle.Cabin.RearviewMirror import RearviewMirror
from vehicle.Cabin.Seat import Seat
from vehicle.Cabin.Sunroof import Sunroof


class Cabin(Model):
    """Cabin model.

    Attributes
    ----------
    Convertible: branch
        Convertible roof.

    Door: branch
        All doors, including windows and switches.

    DoorCount: attribute (uint8)
        Number of doors in vehicle.

    DriverPosition: attribute (uint8)
        The position of the driver seat in row 1.

        Default value is position 1, i.e. a typical LHD vehicle.

    HVAC: branch
        Climate control

    Infotainment: branch
        Infotainment system.

    Lights: branch
        Interior lights signals and sensors.

    RearShade: branch
        Rear window shade.

    RearviewMirror: branch
        Rearview mirror.

    Seat: branch
        All seats.

    SeatPosCount: attribute (uint8[])
        Number of seats across each row from the front to the rear.

        Default value corresponds to two seats in front row and 3 seats in second row.

    SeatRowCount: attribute (uint8)
        Number of seat rows in vehicle.

        Default value corresponds to two rows of seats.

    Sunroof: branch
        Sun roof status.

    """

    def __init__(self, name, parent):
        """Create a new Cabin model."""
        super().__init__(parent)
        self.name = name

        self.Convertible = Convertible("Convertible", self)
        self.Door = Door("Door", self)
        self.DoorCount = DataPointUint8("DoorCount", self)
        self.DriverPosition = DataPointUint8("DriverPosition", self)
        self.HVAC = HVAC("HVAC", self)
        self.Infotainment = Infotainment("Infotainment", self)
        self.Lights = Lights("Lights", self)
        self.RearShade = RearShade("RearShade", self)
        self.RearviewMirror = RearviewMirror("RearviewMirror", self)
        self.Seat = Seat("Seat", self)
        self.SeatPosCount = DataPointUint8Array("SeatPosCount", self)
        self.SeatRowCount = DataPointUint8("SeatRowCount", self)
        self.Sunroof = Sunroof("Sunroof", self)
