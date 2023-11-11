#!/usr/bin/env python3

"""Row1 model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointFloat,
    DataPointUint16,
    DataPointUint8,
    Model,
)

from vehicle.Chassis.Axle.Row1.Wheel import Wheel


class Row1(Model):
    """Row1 model.

    Attributes
    ----------
    TireAspectRatio: attribute (uint8)
        Aspect ratio between tire section height and tire section width, as per ETRTO / TRA standard.

        Unit: percent
    TireDiameter: attribute (float)
        Outer diameter of tires, in inches, as per ETRTO / TRA standard.

        Unit: inch
    TireWidth: attribute (uint16)
        Nominal section width of tires, in mm, as per ETRTO / TRA standard.

        Unit: mm
    Wheel: branch
        Wheel signals for axle

    WheelCount: attribute (uint8)
        Number of wheels on the axle

    WheelDiameter: attribute (float)
        Diameter of wheels (rims without tires), in inches, as per ETRTO / TRA standard.

        Unit: inch
    WheelWidth: attribute (float)
        Width of wheels (rims without tires), in inches, as per ETRTO / TRA standard.

        Unit: inch
    """

    def __init__(self, name, parent):
        """Create a new Row1 model."""
        super().__init__(parent)
        self.name = name

        self.TireAspectRatio = DataPointUint8("TireAspectRatio", self)
        self.TireDiameter = DataPointFloat("TireDiameter", self)
        self.TireWidth = DataPointUint16("TireWidth", self)
        self.Wheel = Wheel("Wheel", self)
        self.WheelCount = DataPointUint8("WheelCount", self)
        self.WheelDiameter = DataPointFloat("WheelDiameter", self)
        self.WheelWidth = DataPointFloat("WheelWidth", self)
