#!/usr/bin/env python3

"""Powertrain model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointFloat,
    DataPointString,
    DataPointUint32,
    Model,
)

from vehicle.Powertrain.CombustionEngine import CombustionEngine
from vehicle.Powertrain.ElectricMotor import ElectricMotor
from vehicle.Powertrain.FuelSystem import FuelSystem
from vehicle.Powertrain.TractionBattery import TractionBattery
from vehicle.Powertrain.Transmission import Transmission


class Powertrain(Model):
    """Powertrain model.

    Attributes
    ----------
    AccumulatedBrakingEnergy: sensor
        The accumulated energy from regenerative braking over lifetime.

        Unit: kWh
    CombustionEngine: branch
        Engine-specific data, stopping at the bell housing.

    ElectricMotor: branch
        Electric Motor specific data.

    FuelSystem: branch
        Fuel system data.

    Range: sensor
        Remaining range in meters using all energy sources available in the vehicle.

        Unit: m
    TractionBattery: branch
        Battery Management data.

    Transmission: branch
        Transmission-specific data, stopping at the drive shafts.

    Type: attribute (string)
        Defines the powertrain type of the vehicle.

        For vehicles with a combustion engine (including hybrids) more detailed information on fuels supported can be found in FuelSystem.SupportedFuelTypes and FuelSystem.SupportedFuels.

        Allowed values: COMBUSTION, HYBRID, ELECTRIC
    """

    def __init__(self, name, parent):
        """Create a new Powertrain model."""
        super().__init__(parent)
        self.name = name

        self.AccumulatedBrakingEnergy = DataPointFloat("AccumulatedBrakingEnergy", self)
        self.CombustionEngine = CombustionEngine("CombustionEngine", self)
        self.ElectricMotor = ElectricMotor("ElectricMotor", self)
        self.FuelSystem = FuelSystem("FuelSystem", self)
        self.Range = DataPointUint32("Range", self)
        self.TractionBattery = TractionBattery("TractionBattery", self)
        self.Transmission = Transmission("Transmission", self)
        self.Type = DataPointString("Type", self)
