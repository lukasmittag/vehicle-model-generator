#!/usr/bin/env python3

"""Vehicle model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointInt16,
    DataPointString,
    DataPointUint16,
    Model,
)

from vehicle.ADAS import ADAS
from vehicle.Acceleration import Acceleration
from vehicle.AngularVelocity import AngularVelocity
from vehicle.Body import Body
from vehicle.Cabin import Cabin
from vehicle.Chassis import Chassis
from vehicle.Connectivity import Connectivity
from vehicle.CurrentLocation import CurrentLocation
from vehicle.Door import Door
from vehicle.Driver import Driver
from vehicle.Exterior import Exterior
from vehicle.Music import Music
from vehicle.OBD import OBD
from vehicle.Powertrain import Powertrain
from vehicle.Service import Service
from vehicle.Shade import Shade
from vehicle.Trailer import Trailer
from vehicle.Trunk import Trunk
from vehicle.VehicleIdentification import VehicleIdentification
from vehicle.VersionVSS import VersionVSS
from vehicle.Window import Window


class Vehicle(Model):
    """Vehicle model.

    Attributes
    ----------
    ADAS: branch
        All Advanced Driver Assist Systems data.

    Acceleration: branch
        Spatial acceleration. Axis definitions according to ISO 8855.

    AngularVelocity: branch
        Spatial rotation. Axis definitions according to ISO 8855.

    AverageSpeed: sensor
        Average speed for the current trip.

        Unit: km/h
    Body: branch
        All body components.

    Cabin: branch
        All in-cabin components, including doors.

    CargoVolume: attribute (float)
        The available volume for cargo or luggage. For automobiles, this is usually the trunk volume.

        Value range: [0, ]
        Unit: l
    Chassis: branch
        All data concerning steering, suspension, wheels, and brakes.

    Connectivity: branch
        Connectivity data.

    CurbWeight: attribute (uint16)
        Vehicle curb weight, including all liquids and full tank of fuel, but no cargo or passengers.

        Unit: kg
    CurrentLocation: branch
        The current latitude and longitude of the vehicle.

    CurrentOverallWeight: sensor
        Current overall Vehicle weight. Including passengers, cargo and other load inside the car.

        Unit: kg
    Driver: branch
        Driver data.

    EmissionsCO2: attribute (int16)
        The CO2 emissions.

        Unit: g/km
    Exterior: branch
        Information about exterior measured by vehicle.

    GrossWeight: attribute (uint16)
        Curb weight of vehicle, including all liquids and full tank of fuel and full load of cargo and passengers.

        Unit: kg
    Height: attribute (uint16)
        Overall vehicle height.

        Unit: mm
    IsBrokenDown: sensor
        Vehicle breakdown or any similar event causing vehicle to stop on the road, that might pose a risk to other road users. True = Vehicle broken down on the road, due to e.g. engine problems, flat tire, out of gas, brake problems. False = Vehicle not broken down.

        Actual criteria and method used to decide if a vehicle is broken down is implementation specific.

    IsMoving: sensor
        Indicates whether the vehicle is stationary or moving.

    Length: attribute (uint16)
        Overall vehicle length.

        Unit: mm
    LowVoltageSystemState: sensor
        State of the supply voltage of the control units (usually 12V).

        Allowed values: UNDEFINED, LOCK, OFF, ACC, ON, START
    MaxTowBallWeight: attribute (uint16)
        Maximum vertical weight on the tow ball of a trailer.

        Unit: kg
    MaxTowWeight: attribute (uint16)
        Maximum weight of trailer.

        Unit: kg
    OBD: branch
        OBD data.

    Powertrain: branch
        Powertrain data for battery management, etc.

    RoofLoad: attribute (int16)
        The permitted total weight of cargo and installations (e.g. a roof rack) on top of the vehicle.

        Unit: kg
    Service: branch
        Service data.

    Speed: sensor
        Vehicle speed.

        Unit: km/h
    Trailer: branch
        Trailer signals.

    TravelledDistance: sensor
        Odometer reading, total distance travelled during the lifetime of the vehicle.

        Unit: km
    TripMeterReading: sensor
        Current trip meter reading.

        Unit: km
    VehicleIdentification: branch
        Attributes that identify a vehicle.

    VersionVSS: branch
        Supported Version of VSS.

    Width: attribute (uint16)
        Overall vehicle width.

        Unit: mm
    Door: branch


    Shade: branch
        Controlling shade

    Music: branch
        Play Music =1; Stop Music =0

    Destination: actuator
        'setyour destination'

    Trunk: branch


    Window: branch


    """

    def __init__(self, name):
        """Create a new Vehicle model."""
        super().__init__()
        self.name = name

        self.ADAS = ADAS("ADAS", self)
        self.Acceleration = Acceleration("Acceleration", self)
        self.AngularVelocity = AngularVelocity("AngularVelocity", self)
        self.AverageSpeed = DataPointFloat("AverageSpeed", self)
        self.Body = Body("Body", self)
        self.Cabin = Cabin("Cabin", self)
        self.CargoVolume = DataPointFloat("CargoVolume", self)
        self.Chassis = Chassis("Chassis", self)
        self.Connectivity = Connectivity("Connectivity", self)
        self.CurbWeight = DataPointUint16("CurbWeight", self)
        self.CurrentLocation = CurrentLocation("CurrentLocation", self)
        self.CurrentOverallWeight = DataPointUint16("CurrentOverallWeight", self)
        self.Driver = Driver("Driver", self)
        self.EmissionsCO2 = DataPointInt16("EmissionsCO2", self)
        self.Exterior = Exterior("Exterior", self)
        self.GrossWeight = DataPointUint16("GrossWeight", self)
        self.Height = DataPointUint16("Height", self)
        self.IsBrokenDown = DataPointBoolean("IsBrokenDown", self)
        self.IsMoving = DataPointBoolean("IsMoving", self)
        self.Length = DataPointUint16("Length", self)
        self.LowVoltageSystemState = DataPointString("LowVoltageSystemState", self)
        self.MaxTowBallWeight = DataPointUint16("MaxTowBallWeight", self)
        self.MaxTowWeight = DataPointUint16("MaxTowWeight", self)
        self.OBD = OBD("OBD", self)
        self.Powertrain = Powertrain("Powertrain", self)
        self.RoofLoad = DataPointInt16("RoofLoad", self)
        self.Service = Service("Service", self)
        self.Speed = DataPointFloat("Speed", self)
        self.Trailer = Trailer("Trailer", self)
        self.TravelledDistance = DataPointFloat("TravelledDistance", self)
        self.TripMeterReading = DataPointFloat("TripMeterReading", self)
        self.VehicleIdentification = VehicleIdentification("VehicleIdentification", self)
        self.VersionVSS = VersionVSS("VersionVSS", self)
        self.Width = DataPointUint16("Width", self)
        self.Door = Door("Door", self)
        self.Shade = Shade("Shade", self)
        self.Music = Music("Music", self)
        self.Destination = DataPointString("Destination", self)
        self.Trunk = Trunk("Trunk", self)
        self.Window = Window("Window", self)


vehicle = Vehicle("Vehicle")
