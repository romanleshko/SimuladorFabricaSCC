#!/usr/bin/env python
# encoding: utf-8
import cliente
import aleatorio

class Evento:
	# """Classe de onde v�o ser derivados todos os eventos.
	# Contem apenas os atributos e m�todos comuns a todos os eventos.
	# N�o haver� inst�ncias desta classe num simulador."""

	#construtor
	def __init__(self,i,sim, fila, peca):
		self.instant = i		#Instante de ocorrencia do evento
		self.simulator = sim	#Simulador onde ocorre o evento
		self.fila = fila
		self.peca = peca


	def __lt__(self, other):
		# """Método de compara��o entre dois eventos.
		# Determina se o evento corrente ocorre primeiro, ou n�o, do que o evento e1
		# Se sim, devolve true; se n�o, devolve false
		# Usado para ordenar por ordem crescente de instantes de ocorr�ncia a lista de eventos do simulador"""
		return self.instant < other.instant




class Chegada(Evento):

	# """Classe que representa a chegada de um cliente. Deriva de Evento."""
	#Construtor
	def __init__(self,i,sim, fila, peca):
		Evento.__init__(self,i,sim, fila, peca)

	def __str__(self):
		# """Método que descreve o evento.
		# Para ser usado na listagem da lista de eventos."""
		return "Chegada\t["+str(self.instant)+"]"

	def executa(self):
		self.fila.act_stats()
		# """Método que executa as acções correspondentes à chegada de um cliente"""
		#Coloca cliente no serviço - na fila ou a ser atendido, conforme o caso
		self.fila.insereClient(self.peca)
		#Agenda nova chegada para daqui a aleatorio.exponencial(self.simulator.media_cheg) instantes
		self.simulator.insereEvento(Chegada(self.simulator.instant+aleatorio.Aleatorio().exponencial(self.peca.seed, self.peca.media_cheg),self.simulator,
											self.fila, self.peca))


class Saida(Evento):

	# """Classe que representa a saída de um cliente. Deriva de Evento."""
	#Construtor
	def __init__(self,i,sim, fila, peca):
		Evento.__init__(self,i,sim, fila, peca)

	def __str__(self):
		# """Método que descreve o evento.
		# Para ser usado na listagem da lista de eventos."""
		return "Saida\t\t["+str(self.instant)+"]"

	
	def executa(self):
		self.fila.act_stats()
		# """Método que executa as acções correspondentes é saída de um cliente"""
		self.fila.removeClient(self.peca) #Retira cliente do serviço

