#!/usr/bin/env python3

"""LaneDepartureDetection model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointBoolean,
    Model,
)


class LaneDepartureDetection(Model):
    """LaneDepartureDetection model.

    Attributes
    ----------
    IsEnabled: actuator
        Indicates if lane departure detection system is enabled. True = Enabled. False = Disabled.

    IsError: sensor
        Indicates if lane departure system incurred an error condition. True = Error. False = No Error.

    IsWarning: sensor
        Indicates if lane departure detection registered a lane departure.

    """

    def __init__(self, name, parent):
        """Create a new LaneDepartureDetection model."""
        super().__init__(parent)
        self.name = name

        self.IsEnabled = DataPointBoolean("IsEnabled", self)
        self.IsError = DataPointBoolean("IsError", self)
        self.IsWarning = DataPointBoolean("IsWarning", self)
