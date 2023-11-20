from pydantic import BaseModel, ConfigDict

class DoneResponse(BaseModel):
    id: int
    model_config = ConfigDict(orm_mode=True)
