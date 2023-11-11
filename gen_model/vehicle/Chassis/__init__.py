#!/usr/bin/env python3

"""Chassis model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointUint16,
    DataPointUint8,
    Model,
)

from vehicle.Chassis.Accelerator import Accelerator
from vehicle.Chassis.Axle import Axle
from vehicle.Chassis.Brake import Brake
from vehicle.Chassis.ParkingBrake import ParkingBrake
from vehicle.Chassis.SteeringWheel import SteeringWheel


class Chassis(Model):
    """Chassis model.

    Attributes
    ----------
    Accelerator: branch
        Accelerator signals

    Axle: branch
        Axle signals

    AxleCount: attribute (uint8)
        Number of axles on the vehicle

    Brake: branch
        Brake system signals

    ParkingBrake: branch
        Parking brake signals

    SteeringWheel: branch
        Steering wheel signals

    Track: attribute (uint16)
        Overall wheel tracking, in mm.

        Unit: mm
    Wheelbase: attribute (uint16)
        Overall wheel base, in mm.

        Unit: mm
    """

    def __init__(self, name, parent):
        """Create a new Chassis model."""
        super().__init__(parent)
        self.name = name

        self.Accelerator = Accelerator("Accelerator", self)
        self.Axle = Axle("Axle", self)
        self.AxleCount = DataPointUint8("AxleCount", self)
        self.Brake = Brake("Brake", self)
        self.ParkingBrake = ParkingBrake("ParkingBrake", self)
        self.SteeringWheel = SteeringWheel("SteeringWheel", self)
        self.Track = DataPointUint16("Track", self)
        self.Wheelbase = DataPointUint16("Wheelbase", self)
