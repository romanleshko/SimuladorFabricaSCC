#!/usr/bin/env python
# encoding: utf-8
import fila
import lista
import eventos


class Simulador:
    def insereEvento(self, event):
        self.event_list.insert_event(event)

    # Construtor
    def __init__(self):
        # M�dias das distribui��es de chegadas e de atendimento no servi�o
        self.media_cheg = 1
        self.media_serv = 1.5
        # N�mero de clientes que v�o ser atendidos
        self.n_clientes = 100

        # Rel�gio de simula��o - vari�vel que cont�m o valor do tempo em cada instante
        self.instant = 0  # valor inicial a zero

        # Servi�o - pode haver mais do que um num simulador
        self.client_queue = fila.Fila(self)
        # Lista de eventos - onde ficam registados todos os eventos que v�o ocorrer na simula��o
        # Cada simulador s� tem uma
        self.event_list = lista.Lista(self)

        # Agendamento da primeira chegada
        # Se n�o for feito, o simulador n�o tem eventos para simular
        self.insereEvento(eventos.Chegada(self.instant, self))

    def executa(self):
        """M�todo executivo do simulador"""
        # Enquanto n�o atender todos os clientes
        while (self.client_queue.atendidos < self.n_clientes):
            print (self.event_list)  # Mostra lista de eventos - desnecess�rio; � apenas informativo
            event = self.event_list.remove_event()  # Retira primeiro evento (� o mais iminente) da lista de eventos
            self.instant = event.instant  # Actualiza rel�gio de simula��o
            self.act_stats()  # Actualiza valores estat�sticos
            event.executa(self.client_queue)  # Executa evento
        self.relat()  # Apresenta resultados de simula��o finais

    def act_stats(self):
        """M�todo que actualiza os valores estat�sticos do simulador"""
        self.client_queue.act_stats()

    def relat(self):
        """M�todo que apresenta os resultados de simula��o finais"""
        print ("\n\n------------FINAL RESULTS---------------\n\n")
        self.client_queue.relat()


# programa principal

# Cria um simulador e
s = Simulador()
# p�e-o em marcha
s.executa()
