from Factory import AbstractAPIFactory, TransportDataFactory, SecurityDataFactory

def client_code(factory: AbstractAPIFactory):
  api_fortal = factory.create_api_fortal()
  api_ceara  = factory.create_api_ce()

  print(api_fortal.collect_data())
  print(api_ceara.collect_data_by_city("Iguatu"))

if __name__ == "__main__":
  token_ce = "CE12345"
  token_fortal = "FO12345"

  print("Coletando dados de Transporte")
  client_code(TransportDataFactory(token_fortal, token_ce))
  
  print("Coletando dados de Segurança")
  client_code(SecurityDataFactory(token_fortal, token_ce))