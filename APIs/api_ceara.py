from abc import ABC, abstractmethod

class AbstractCearaAPI(ABC):
  def __init__(self, token):
    self.token = token 
  
  @abstractmethod
  def collect_data(self):
    pass

  @abstractmethod
  def collect_data_by_city(self, city):
    pass

class APICearaTransport(AbstractCearaAPI):
  def collect_data(self):
    return f"Dados Coletados 'APICearaTransport' por meio do token: {self.token}"
  
  def collect_data_by_city(self, city):
    return f"Dados Coletados da cidade {city} 'APICearaTransport' por meio do token: {self.token}"

class APICearaSecurity(AbstractCearaAPI):
  def collect_data(self):
    return f"Dados Coletados 'APICearaSecurity' por meio do token: {self.token}"
  
  def collect_data_by_city(self, city):
    return f"Dados Coletados da cidade {city} 'APICearaSecurity' por meio do token: {self.token}"
