import collections

Card = collections.namedtuple('Card', ['carta', 'nipe'])

class Baralho:
    cartas = [str(n) for n in range(2, 11)] + list('JQKA')
    nipes = 'espada ouro paus copas'.split()

    def __init__(self):
        self._cards = [Card(carta, nipe) for nipe in self.nipes
                                        for carta in self.cartas]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

baralho = Baralho()
# Verificar o número de cartas no baralho 
print(f"Número de cartas no baralho: {len(baralho)}")

# Acessar uma carta específica (por exemplo, a primeira carta)
print(f"A primeira carta do baralho é: {baralho[0]}")

# Iterar sobre as cartas do baralho
print("Algumas cartas do baralho:")
for carta in baralho[:5]:  # Exibir as 5 primeiras cartas
    print(carta)