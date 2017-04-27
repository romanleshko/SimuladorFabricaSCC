#!/usr/bin/env python
# encoding: utf-8
import fila
import lista
import eventos
import cliente

import time

class Simulador:

    def insereEvento(self, event):
        self.event_list.insert_event(event)

    # Construtor
    def __init__(self, pecaA, pecaB):

        # Relógio de simulação - variável que contém o valor do tempo em cada instante
        self.instant = 0  # valor inicial a zero

        # Serviço - pode haver mais do que um num simulador
        self.fila_envernizamento = fila.Fila(self, 'envernizamento', 30, pecaA.n_servicos_envernizamento)

        self.fila_polimento_A = fila.Fila(self, 'polimento', 45, pecaA.n_servicos_polimento, self.fila_envernizamento)
        self.fila_polimento_B = fila.Fila(self, 'polimento', 60, pecaB.n_servicos_polimento, self.fila_envernizamento)

        self.fila_perfuracao_A = fila.Fila(self, 'perfuracao', 75, pecaA.n_servicos_perfuracao, self.fila_polimento_A)
        self.fila_perfuracao_B = fila.Fila(self, 'perfuracao', 90, pecaB.n_servicos_perfuracao, self.fila_polimento_B)
        # Lista de eventos - onde ficam registados todos os eventos que vão ocorrer na simulação
        # Cada simulador só tem uma
        self.event_list = lista.Lista(self)

        # Agendamento da primeira chegada
        # Se n�o for feito, o simulador n�o tem eventos para simular
        self.insereEvento(eventos.Chegada(self.instant, self, self.fila_perfuracao_A, pecaA))
        self.insereEvento(eventos.Chegada(self.instant, self, self.fila_perfuracao_B, pecaB))


    def executa(self, t):


        t_inicial = int(time.time())


        """M�todo executivo do simulador"""
        # Enquanto n�o atender todos os clientes
        #while (self.fila_envernizamento.atendidos < self.n_clientes):
        while self.instant < t  :

            #print (self.event_list)  # Mostra lista de eventos - desnecessário; é apenas informativo
            event = self.event_list.remove_event()  # Retira primeiro evento (é o mais iminente) da lista de eventos
            self.instant = event.instant  # Actualiza relógio de simulação
            self.act_stats(event.fila)  # Actualiza valores estatísticos
            event.executa()  # Executa evento
        self.relat()  # Apresenta resultados de simula��o finais

    def act_stats(self, fila):
        """M�todo que actualiza os valores estat�sticos do simulador"""
        fila.act_stats()



    def relat(self):
        """M�todo que apresenta os resultados de simula��o finais"""
        print ("\n------------FINAL RESULTS PECA A---------------")
        self.fila_perfuracao_A.relat()
        self.fila_polimento_A.relat()
        print("\n\n------------FINAL RESULTS PECA B---------------")
        self.fila_perfuracao_B.relat()
        self.fila_polimento_B.relat()
        print("\n\n------------FINAL RESULTS ENVERNIZAMENTO---------------")
        self.fila_envernizamento.relat()


#programa principal

#dados originais
chegA = 5
perfA = [2, 0.7]
polA = [4, 1.2]

n_ser_perfA = 1
n_ser_polA = 1


chegB = 1.33
perfB = [0.75, 0.3]
polB = [3, 1]
n_ser_perfB = 1
n_ser_polB = 2

env = [1.4, 0.3]
n_ser_env = 2


pecaA = cliente.PecaA(chegA, perfA, polA, env, n_ser_perfA, n_ser_polA, n_ser_env)
pecaB = cliente.PecaB(chegB, perfB, polB, env, n_ser_perfB, n_ser_polB, n_ser_env)

#tempo de simulação em minutos
t = 8*20*60
# Cria um simulador e
s = Simulador(pecaA, pecaB)
# põe-o em marcha
s.executa(t)
