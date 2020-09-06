from typing import Any
from .validator import Validator

class EagerValidator(Validator):
  '''An EagerValidator marks fields for initialization and set stage validation.
  This is used usually before heavy transforming validators.
  '''

  def validate(self, value: Any, key_path: str, root: Any, all_fields: bool):
    pass
