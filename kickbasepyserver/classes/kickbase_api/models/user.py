from datetime import datetime
from typing import List
from kickbase_api.models.base_model import BaseModel
import json
from json import JSONEncoder


class User(BaseModel):
    id: str = None
    perms: List[str] = None
    email: str = None
    vemail: str = None
    name: str = None
    notifications: int = None
    profile_image_path: str = None
    profile_cover_path: str = None
    flags: str = None
    trialExpiry: datetime = None
    
    
    def __init__(self, d: dict = {}):
        self._json_mapping = {
            "profile": "profile_image_path",
            "cover": "profile_cover_path",
            "email": "email",
            "flags": "flags",
            "vemail": "vemail",
            "trialExpiry": "trialExpiry",
            "id": "id",
            "name": "name",
            "perms": "perms"
        }
        super().__init__(d)

    def toJson(self):
        return json.dumps(self, cls=UserJSONEncoder)
        
class UserJSONEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__