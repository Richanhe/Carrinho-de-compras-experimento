class Carrinho:
    def __init__(self):
        self.itens = []
    
    def adicionar_item(self, nome, preco, quantidade=1):
        if preco < 0 or quantidade <= 0:
            raise ValueError("Preço e quantidade devem ser positivos")

        if nome in [item['nome'] for item in self.itens]:
            for item in self.itens:
                if item['nome'] == nome:
                    item['quantidade'] += quantidade
                    break
        else:
            self.itens.append({'nome': nome, 'preco': preco, 'quantidade': quantidade})
    
    def remover_item(self, nome):
        if nome not in [item['nome'] for item in self.itens]:
            raise ValueError(f'Item {nome} não encontrado no carrinho')
        self.itens = [item for item in self.itens if item['nome'] != nome]
    
    def show(self):
        return self.itens
    
    def total(self):
        if not self.itens:
            return 0
        total = sum([item['preco'] * item['quantidade'] for item in self.itens])
        if total < 150:
            total += 20
        return total
    