class Veiculo:
  def __init__(self, modelo, local = None, vaga = None):
    self.modelo = modelo
    self.local = local
    self.vaga = vaga

  def retorno(self):
    if self.local:
      return f'O {self.modelo} está estacionado na vaga {self.vaga} no {self.local}!'
    else:
      return f'O {self.modelo} não está no estacionamento!'