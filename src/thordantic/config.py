from pydantic import BaseModel, ConfigDict

class ThorModel(BaseModel):
    model_config = ConfigDict(
        extra='forbid',             # match API strictly
        validate_by_name=True,      # allow alias values
        serialize_by_alias=True,    # serialise to alias
        arbitrary_types_allowed = True
    )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ThorModel):
            return NotImplemented
        return self.model_dump(by_alias=True, exclude_none=True) == \
            other.model_dump(by_alias=True, exclude_none=True)