import logging
from typing import Any
from jinja2.filters import do_pprint as jinja2_do_pprint
from pydantic import BaseModel, conlist, TypeAdapter, ValidationError, field_validator

class Quantity(BaseModel):
    value: float
    unit: str

    def __str__(self):
        return f"{self.value} {self.unit}"

class Coding(BaseModel):
    code: str
    display: str| None = None
    system: str
    
    def __str__(self) -> str:

        return self.display or f"{self.system}#{self.code}"

class CodeableConcept(BaseModel):
    text: str | None = None
    coding: None | conlist(Coding,min_length=1)  = None # type: ignore

    @field_validator("coding",mode="before")
    def coerce_empty_list(cls, value):
        if isinstance(value,list) and len(value) == 0:
            return None
        return value

    def __str__(self):
        if self.text is not None:
            return self.text
        if self.coding is not None:
            return str(self.coding[0])
        return str(None)

Printable = TypeAdapter(Quantity | CodeableConcept| str)
def do_pprint(value: Any):
    """Pretty-print a value."""
    try:
        value = Printable.validate_python(value)
        logging.debug(f"Value {value} is printable.")
        return str(value)
    except ValidationError:
        logging.debug(f"Value {value} is not printable.")
        return jinja2_do_pprint(value)