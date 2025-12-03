# -*- coding: utf-8 -*-

from .Location import Location
import json

from pydantic import BaseModel

class Unicorn(BaseModel):
    '''
    En enkel klass för att representera en enhörning
    '''

    id: int = 0
    name: str = ""
    description: str = ""
    reportedBy: str = ""
    spottedWhere: Location  =  Location()
    spottedWhen: str | None = None
    image: str = ""

    def from_db(self, data: list) -> None:
        '''
        Populerar en enhörning med data från en databasförfrågan.
        '''

        self.id = data[0]
        self.name = data[1]
        self.description = data[2]
        self.reportedBy = data[3]
        self.spottedWhere.name = data[4]
        self.spottedWhere.lat = data[5]
        self.spottedWhere.lon = data[6]
        self.spottedWhen = data[7]
        self.image = data[8]

    def to_dict(self, nested = False):
        '''
        Skapar en dictionary med värden från denna enhörning. Bra att använda
        när man matar in enhörningar i databaser.

        Med en liten fix kan vi göra den här lämplig även för JSON-representation.
        '''

        if nested:
            location = {
                'name': self.spottedWhere.name,
                'lat': self.spottedWhere.lat,
                'lon': self.spottedWhere.lon
            }
            unicorn =  {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'reportedBy': self.reportedBy,
                'spottedWhere': location,
                'spottedWhen': self.spottedWhen,
                'image': self.image
            }
        else:
            unicorn =  {
                    'id': self.id,
                    'name': self.name,
                    'description': self.description,
                    'reportedBy': self.reportedBy,
                    'spottedWhereName': self.spottedWhere.name,
                    'spottedWhereLat': self.spottedWhere.lat,
                    'spottedWhereLon': self.spottedWhere.lon,
                    'spottedWhen': self.spottedWhen,
                    'image': self.image
                }

        return unicorn
