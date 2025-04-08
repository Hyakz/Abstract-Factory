from abc import ABC, abstractmethod

class AbstractFortalAPI(ABC):
  def __init__(self, token):
    self.token = token 
  
  @abstractmethod
  def collect_data(self):
    pass

class APiFortalTransport(AbstractFortalAPI):
  def collect_data(self):
    return f"Dados Coletados 'APiFortalTransport' por meio do token: {self.token}"

class APiFortalSecurity(AbstractFortalAPI):
  def collect_data(self):
    return f"Dados Coletados 'APiFortalTransport' por meio do token: {self.token}"