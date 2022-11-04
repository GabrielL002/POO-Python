'''''
-----------
DESCRIÇÃO
-----------
João confecciona placas por encomenda. Como o volume dos pedidos tem aumentado, ele precisa de uma 
aplicação que controle o cadastro de seus clientes e os pedidos realizados.
Quando ele recebe uma encomenda, João anota o nome do cliente, seu endereço completo e seu telefone.
Para a encomenda, ele registra: a altura e largura da placa, a frase a ser escrita, a cor da placa
("branca" ou "cinza"), a cor da frase ("azul", "vermelha", "amarela", "preta" ou "verde").
Com base nessas informações ele calcula manualmente o valor da placa, utilizando as seguintes fórmulas:
área = altura x largura
custo do material = área x R$ 147,00
custo do desenho = quantidade de letras x R$ 0,35 (espaços devem ser desconsiderados)
valor final da placa = custo do material + custo do desenho

João deseja que o sistema controle os pedidos e calcule automaticamente o valor final das placas.
João deseja ainda manter um histórico de todos os pedidos realizados, a fim de verificar o seu faturamento.
A partir do cenário descrito e do diagrama de classes apresentado, implemente em Python
as classes solicitadas, aplicando os conceitos de programação orientada a objetos.
'''


class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Pedido:
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.valor_fixo_material = 147.00
        self.valor_fixo_letra = 0.35

    def calcular_total(self):
        letras = len(self.frase.replace(" ", ""))
        area = self.altura * self.largura
        custoMaterial = area * self.valor_fixo_material
        custoDesenho = letras * self.valor_fixo_letra
        total = custoMaterial + custoDesenho
        return total


class Historico:
    def __init__(self):
        self.pedidos = []

    def inserir_pedido(self, pedido):
        self.pedidos.append(pedido)

    def calcular_faturamento(self):
        total = 0
        for pedido in self.pedidos:
            total += pedido.calcular_total()
        return total
