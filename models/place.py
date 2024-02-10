#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel
from typing import List


class Place(BaseModel):
    """Represents a place in the application.

    Attributes:
        city_id (str): The unique identifier for the City associated with the place.
        user_id (str): The unique identifier for the User associated with the place.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can accommodate.
        price_by_night (int): The price per night to stay at the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (List[str]): A list of unique identifiers for amenities associated with the place.
    """

    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: List[str] = []

