from abc  import ABC, abstractmethod
from APIs import APiFortalTransport, APiFortalSecurity, APICearaTransport, APICearaSecurity

class AbstractAPIFactory(ABC):
  def __init__(self, token_fortal, token_ce):
    self.token_fortal = token_fortal
    self.token_ce = token_ce
  
  @abstractmethod
  def create_api_fortal(self):
    pass

  @abstractmethod
  def create_api_ce(self):
    pass

class TransportDataFactory(AbstractAPIFactory):
  def create_api_fortal(self):
    return APiFortalTransport(self.token_fortal)
  
  def create_api_ce(self):
    return APICearaTransport(self.token_ce)

class SecurityDataFactory(AbstractAPIFactory):
  def create_api_fortal(self):
    return APiFortalSecurity(self.token_fortal)
  
  def create_api_ce(self):
    return APICearaSecurity(self.token_ce)