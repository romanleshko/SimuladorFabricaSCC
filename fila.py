#!/usr/bin/env python
# encoding: utf-8
import eventos
import cliente
import aleatorio

class Fila:
    # """Classe que representa um serviço com uma fila de espera associada"""

    # Construtor
    def __init__(self, sim, nome, seed, prox_fila = None):
        self.fila = []  # Fila de espera do serviço
        self.simulator = sim  # Referência para o simulador a que pertence o servi�o
        self.estado = 0  # Vari�vel que regista o estado do servi�o: 0 - livre; 1 - ocupado
        self.temp_last = sim.instant  # Tempo que passou desde o �ltimo evento. Neste caso 0, porque a simula��o ainda n�o come�ou.
        self.atendidos = 0  # N�mero de clientes atendidos at� ao momento
        self.soma_temp_esp = 0
        self.soma_temp_serv = 0
        self.nome = nome
        self.prox_fila = prox_fila
        self.seed = seed

    def num_servicos(self, client):
        if self.nome == 'perfuracao':
            return client.n_servicos_perfuracao

        if self.nome == 'polimento':
            return client.n_servicos_polimento

        if self.nome == 'envernizamento':
            return client.n_servicos_envernizamento

    def tmp_serv(self, client):
        if self.nome == 'perfuracao':
            return client.perfuracao

        if self.nome == 'polimento':

            return client.polimento

        if self.nome == 'envernizamento':
            return client.evernizamento

    def insereClient(self, client):
        # """Método que insere cliente (client) no servi�o"""
        
        if (self.estado < self.num_servicos(client)): # Se servi�o livre,

            self.estado = self.estado + 1  # fica ocupado e
            # agenda saída do cliente c para daqui a self.simulator.media_serv instantes

            tmp_serv = self.tmp_serv(client)

            self.simulator.insereEvento(
                    eventos.Saida(self.simulator.instant + aleatorio.normal(self.seed, tmp_serv), self.simulator, self, client))
        else:
            self.fila.append(client)  # Se servi�o ocupado, o cliente vai para a fila de espera

    def removeClient(self, fila, peca):

        # """Método que remove cliente do serviço"""
        self.atendidos = self.atendidos + 1  # Regista que acabou de atender + 1 cliente

        if self.prox_fila:
            self.prox_fila.insereClient(peca)

        if (self.fila == []):  # Se a fila est� vazia,
            self.estado = self.estado - 1  # liberta o servi�o
        else:  # Se não,
            # vai buscar pr�ximo cliente � fila de espera e
            cl = self.fila.pop(0)
            # agenda a sua saida para daqui a self.simulator.media_serv instantes
            self.simulator.insereEvento(
                eventos.Saida(self.simulator.instant + aleatorio.normal(self.seed, self.tmp_serv(cl)), self.simulator, fila, peca))

    def act_stats(self):
        # """Método que calcula valores para estat�sticas, em cada passo da simula��o ou evento"""
        # Calcula tempo que passou desde o �ltimo evento
        temp_desd_ult = self.simulator.instant - self.temp_last
        # Actualiza vari�vel para o pr�ximo passo/evento
        self.temp_last = self.simulator.instant
        # Contabiliza tempo de espera na fila
        # para todos os clientes que estiveram na fila durante o intervalo
        self.soma_temp_esp = self.soma_temp_esp + (len(self.fila) * temp_desd_ult)
        # Contabiliza tempo de atendimento
        self.soma_temp_serv = self.soma_temp_serv + (self.estado * temp_desd_ult)

    def relat(self):
        # """Método que calcula valores finais estatísticos"""
        # Tempo m�dio de espera na fila
        temp_med_fila = self.soma_temp_esp / (self.atendidos + len(self.fila))
        # Comprimento m�dio da fila de espera
        # self.simulator.instant neste momento � o valor do tempo de simula��o,
        # uma vez que a simula��o come�ou em 0 e este método s� � chamdo no fim da simula��o
        comp_med_fila = self.soma_temp_esp / self.simulator.instant
        # Tempo m�dio de atendimento no servi�o
        utilizacao_serv = self.soma_temp_serv / self.simulator.instant

        # Apresenta resultados
        print("\nFila ", self.nome)
        print("Tempo medio de espera", temp_med_fila)
        print("Comp. medio da fila", comp_med_fila)
        print("Utilizacao do servico", utilizacao_serv)
        print("Tempo de simulacao", self.simulator.instant)
        print("Numero de clientes atendidos", self.atendidos)
        print("Numero de clientes na fila", len(self.fila))
        print('Estado da fila: ', self.estado)
