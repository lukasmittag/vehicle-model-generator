#!/usr/bin/env python3

"""VehicleIdentification model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointString,
    DataPointUint16,
    Model,
)


class VehicleIdentification(Model):
    """VehicleIdentification model.

    Attributes
    ----------
    AcrissCode: attribute (string)
        The ACRISS Car Classification Code is a code used by many car rental companies.

    BodyType: attribute (string)
        Indicates the design and body style of the vehicle (e.g. station wagon, hatchback, etc.).

    Brand: attribute (string)
        Vehicle brand or manufacturer.

    DateVehicleFirstRegistered: attribute (string)
        The date in ISO 8601 format of the first registration of the vehicle with the respective public authorities.

    KnownVehicleDamages: attribute (string)
        A textual description of known damages, both repaired and unrepaired.

    MeetsEmissionStandard: attribute (string)
        Indicates that the vehicle meets the respective emission standard.

    Model: attribute (string)
        Vehicle model.

    ProductionDate: attribute (string)
        The date in ISO 8601 format of production of the item, e.g. vehicle.

    PurchaseDate: attribute (string)
        The date in ISO 8601 format of the item e.g. vehicle was purchased by the current owner.

    VIN: attribute (string)
        17-character Vehicle Identification Number (VIN) as defined by ISO 3779.

    VehicleConfiguration: attribute (string)
        A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'.

    VehicleInteriorColor: attribute (string)
        The color or color combination of the interior of the vehicle.

    VehicleInteriorType: attribute (string)
        The type or material of the interior of the vehicle (e.g. synthetic fabric, leather, wood, etc.).

    VehicleModelDate: attribute (string)
        The release date in ISO 8601 format of a vehicle model (often used to differentiate versions of the same make and model).

    VehicleSeatingCapacity: attribute (uint16)
        The number of passengers that can be seated in the vehicle, both in terms of the physical space available, and in terms of limitations set by law.

    VehicleSpecialUsage: attribute (string)
        Indicates whether the vehicle has been used for special purposes, like commercial rental, driving school.

    WMI: attribute (string)
        3-character World Manufacturer Identification (WMI) as defined by ISO 3780.

    Year: attribute (uint16)
        Model year of the vehicle.

    """

    def __init__(self, name, parent):
        """Create a new VehicleIdentification model."""
        super().__init__(parent)
        self.name = name

        self.AcrissCode = DataPointString("AcrissCode", self)
        self.BodyType = DataPointString("BodyType", self)
        self.Brand = DataPointString("Brand", self)
        self.DateVehicleFirstRegistered = DataPointString("DateVehicleFirstRegistered", self)
        self.KnownVehicleDamages = DataPointString("KnownVehicleDamages", self)
        self.MeetsEmissionStandard = DataPointString("MeetsEmissionStandard", self)
        self.Model = DataPointString("Model", self)
        self.ProductionDate = DataPointString("ProductionDate", self)
        self.PurchaseDate = DataPointString("PurchaseDate", self)
        self.VIN = DataPointString("VIN", self)
        self.VehicleConfiguration = DataPointString("VehicleConfiguration", self)
        self.VehicleInteriorColor = DataPointString("VehicleInteriorColor", self)
        self.VehicleInteriorType = DataPointString("VehicleInteriorType", self)
        self.VehicleModelDate = DataPointString("VehicleModelDate", self)
        self.VehicleSeatingCapacity = DataPointUint16("VehicleSeatingCapacity", self)
        self.VehicleSpecialUsage = DataPointString("VehicleSpecialUsage", self)
        self.WMI = DataPointString("WMI", self)
        self.Year = DataPointUint16("Year", self)
