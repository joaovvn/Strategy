from vagas import Veiculo

veiculo1 = Veiculo('Ford Ka', local = 'Edificio Garagem', vaga = '15')
veiculo2 = Veiculo('Chevrolet Onix')
veiculo3 = Veiculo('Toyota Corolla')
veiculo4 = Veiculo('Volkswagen Gol', local = 'Estacionamento Externo', vaga = '103')

print(veiculo1.retorno())
print(veiculo2.retorno())
print(veiculo3.retorno())
print(veiculo4.retorno())