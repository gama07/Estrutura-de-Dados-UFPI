class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.anterior = None
        self.proximo = None

class Agenda:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def adicionar_contato(self, nome, telefone):
        novo_contato = Contato(nome, telefone)
        if not self.primeiro:
            self.primeiro = novo_contato
            self.ultimo = novo_contato
        else:
            novo_contato.anterior = self.ultimo
            self.ultimo.proximo = novo_contato
            self.ultimo = novo_contato

    def remover_contato(self, nome):
        atual = self.primeiro
        while atual:
            if atual.nome == nome:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.primeiro = atual.proximo
                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.ultimo = atual.anterior
                print(f"Contato removido: {nome}")
            

    def exibir_contatos(self):
        if not self.primeiro:
            print("A agenda está vazia.")
            return
        atual = self.primeiro
        while atual:
            print(f"Nome: {atual.nome}, Telefone: {atual.telefone}")
            atual = atual.proximo

# Criar agenda de contatos
agenda = Agenda()

# Adicionar contatos
agenda.adicionar_contato("Dream", "123456789")
agenda.adicionar_contato("Sky", "777720357")
agenda.adicionar_contato("Astro", "111223344")

# Exibir contatos
print("Contatos na agenda:")
agenda.exibir_contatos()


