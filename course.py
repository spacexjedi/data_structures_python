from professor import Professor

class Course:
  def __init_(self, name, code, max, min, professor):
    self.name = name
    self.code = code
    self.max = max
    self.min = min
    self.professors = []

    if isinstance(professor, Professor):
      self.addresses.append(professor)
    elif isinstance(professor, List):
      for entry in professor:
        if not isinstance(entry, professor):
          raise Error("Invalid Professor...")
      
      self.professors = professor
    else:
      raise Error("Invalid Address...")
