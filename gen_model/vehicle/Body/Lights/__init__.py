#!/usr/bin/env python3

"""Lights model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointBoolean,
    Model,
)


class Lights(Model):
    """Lights model.

    Attributes
    ----------
    IsBackupOn: actuator
        Is backup (reverse) light on?

    IsBrakeOn: actuator
        Is brake light on?

    IsFrontFogOn: actuator
        Is front fog light on?

    IsHazardOn: actuator
        Are hazards on?

    IsHighBeamOn: actuator
        Is high beam on?

    IsLeftIndicatorOn: actuator
        Is left indicator flashing?

    IsLowBeamOn: actuator
        Is low beam on?

    IsParkingOn: actuator
        Is parking light on?

    IsRearFogOn: actuator
        Is rear fog light on?

    IsRightIndicatorOn: actuator
        Is right indicator flashing?

    IsRunningOn: actuator
        Are running lights on?

    """

    def __init__(self, name, parent):
        """Create a new Lights model."""
        super().__init__(parent)
        self.name = name

        self.IsBackupOn = DataPointBoolean("IsBackupOn", self)
        self.IsBrakeOn = DataPointBoolean("IsBrakeOn", self)
        self.IsFrontFogOn = DataPointBoolean("IsFrontFogOn", self)
        self.IsHazardOn = DataPointBoolean("IsHazardOn", self)
        self.IsHighBeamOn = DataPointBoolean("IsHighBeamOn", self)
        self.IsLeftIndicatorOn = DataPointBoolean("IsLeftIndicatorOn", self)
        self.IsLowBeamOn = DataPointBoolean("IsLowBeamOn", self)
        self.IsParkingOn = DataPointBoolean("IsParkingOn", self)
        self.IsRearFogOn = DataPointBoolean("IsRearFogOn", self)
        self.IsRightIndicatorOn = DataPointBoolean("IsRightIndicatorOn", self)
        self.IsRunningOn = DataPointBoolean("IsRunningOn", self)
