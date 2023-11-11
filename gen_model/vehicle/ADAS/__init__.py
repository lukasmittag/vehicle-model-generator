#!/usr/bin/env python3

"""ADAS model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointString,
    Model,
)

from vehicle.ADAS.ABS import ABS
from vehicle.ADAS.CruiseControl import CruiseControl
from vehicle.ADAS.EBA import EBA
from vehicle.ADAS.EBD import EBD
from vehicle.ADAS.ESC import ESC
from vehicle.ADAS.LaneDepartureDetection import LaneDepartureDetection
from vehicle.ADAS.ObstacleDetection import ObstacleDetection
from vehicle.ADAS.TCS import TCS


class ADAS(Model):
    """ADAS model.

    Attributes
    ----------
    ABS: branch
        Antilock Braking System signals.

    ActiveAutonomyLevel: sensor
        Indicates the currently active level of autonomy according to SAE J3016 taxonomy.

        Follows https://www.sae.org/news/2019/01/sae-updates-j3016-automated-driving-graphic taxonomy. For SAE levels 3 and 4 the system is required to alert the driver before it will disengage. Level 4 systems are required to reach a safe state even if a driver does not take over. Only level 5 systems are required to not rely on a driver at all. While level 2 systems require the driver to be monitoring the system at all times, many level 2 systems, often termed "level 2.5" systems, do warn the driver shortly before reaching their operational limits, therefore we also support the DISENGAGING state for SAE_2.

        Allowed values: SAE_0, SAE_1, SAE_2_DISENGAGING, SAE_2, SAE_3_DISENGAGING, SAE_3, SAE_4_DISENGAGING, SAE_4, SAE_5
    CruiseControl: branch
        Signals from Cruise Control system.

    EBA: branch
        Emergency Brake Assist (EBA) System signals.

    EBD: branch
        Electronic Brakeforce Distribution (EBD) System signals.

    ESC: branch
        Electronic Stability Control System signals.

    LaneDepartureDetection: branch
        Signals from Lane Departure Detection System.

    ObstacleDetection: branch
        Signals form Obstacle Sensor System.

    SupportedAutonomyLevel: attribute (string)
        Indicates the highest level of autonomy according to SAE J3016 taxonomy the vehicle is capable of.

        Allowed values: SAE_0, SAE_1, SAE_2, SAE_3, SAE_4, SAE_5
    TCS: branch
        Traction Control System signals.

    """

    def __init__(self, name, parent):
        """Create a new ADAS model."""
        super().__init__(parent)
        self.name = name

        self.ABS = ABS("ABS", self)
        self.ActiveAutonomyLevel = DataPointString("ActiveAutonomyLevel", self)
        self.CruiseControl = CruiseControl("CruiseControl", self)
        self.EBA = EBA("EBA", self)
        self.EBD = EBD("EBD", self)
        self.ESC = ESC("ESC", self)
        self.LaneDepartureDetection = LaneDepartureDetection("LaneDepartureDetection", self)
        self.ObstacleDetection = ObstacleDetection("ObstacleDetection", self)
        self.SupportedAutonomyLevel = DataPointString("SupportedAutonomyLevel", self)
        self.TCS = TCS("TCS", self)
