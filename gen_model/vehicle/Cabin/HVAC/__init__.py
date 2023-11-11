#!/usr/bin/env python3

"""HVAC model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointBoolean,
    DataPointFloat,
    Model,
)

from vehicle.Cabin.HVAC.Station import Station


class HVAC(Model):
    """HVAC model.

    Attributes
    ----------
    AmbientAirTemperature: sensor
        Ambient air temperature inside the vehicle.

        Unit: celsius
    IsAirConditioningActive: actuator
        Is Air conditioning active.

    IsFrontDefrosterActive: actuator
        Is front defroster active.

    IsRearDefrosterActive: actuator
        Is rear defroster active.

    IsRecirculationActive: actuator
        Is recirculation active.

    Station: branch
        HVAC for single station in the vehicle

    """

    def __init__(self, name, parent):
        """Create a new HVAC model."""
        super().__init__(parent)
        self.name = name

        self.AmbientAirTemperature = DataPointFloat("AmbientAirTemperature", self)
        self.IsAirConditioningActive = DataPointBoolean("IsAirConditioningActive", self)
        self.IsFrontDefrosterActive = DataPointBoolean("IsFrontDefrosterActive", self)
        self.IsRearDefrosterActive = DataPointBoolean("IsRearDefrosterActive", self)
        self.IsRecirculationActive = DataPointBoolean("IsRecirculationActive", self)
        self.Station = Station("Station", self)
