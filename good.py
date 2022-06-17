# Open Closed Principle
# Dependecy Inversion

from abc import ABC, abstractmethod

class AddGroupController:
  
  def __init__(self, validation):
    self.__validation = validation

  def add(self):
    self.__validation.validate()

class Validation(ABC):
  @abstractmethod
  def validate() -> None:
    pass



class PhoneValidation(Validation):
  @staticmethod
  def validate():
    print('Phone Validate Successfull')

class RequiredFieldValidation(Validation):
  @staticmethod
  def validate():
    print('Validate Required Successfull')

class EmailValidation(Validation):
  @staticmethod
  def validate():
    print('Email Validate Successfull')

class AddGroupValidationComposite(Validation):
  def __init__(self, fields: list[Validation]) -> None:
    self.__fieldValidation = fields
    
  def validate(self) -> None:
    for field in self.__fieldValidation:
      field.validate()

# Composition Root = Criar instancia de todas as classes
requiredFieldValidation = RequiredFieldValidation()
phoneValidation = PhoneValidation()
emailValidation = EmailValidation()

composite = AddGroupValidationComposite([requiredFieldValidation, phoneValidation, emailValidation])
controller = AddGroupController(composite)
controller.add()

a=1
