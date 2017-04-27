#!/usr/bin/env python
# encoding: utf-8
class Peca:

	#perfuracao, polimento e evernizamento são listas com dois elementos
	#onde o primeiro elemento é a média e o segundo o desvio padrão
	def __init__(self, media_cheg, perfuracao, polimento, envernizamento):
		self.media_cheg = media_cheg
		self.perfuracao = perfuracao
		self.polimento = polimento
		self.evernizamento = envernizamento



class PecaA(Peca):

	def __init__(self, media_cheg, perfuracao, polimento, envernizamento, n_serv_per, n_serv_pol, n_serv_env):
		Peca.__init__(self, media_cheg, perfuracao, polimento, envernizamento)
		self.n_servicos_perfuracao = n_serv_per
		self.n_servicos_polimento = n_serv_pol
		self.n_servicos_envernizamento = n_serv_env
		self.nome = 'PECA A'
		self.seed = 0

class PecaB(Peca):

	def __init__(self, media_cheg, perfuracao, polimento, envernizamento, n_serv_per, n_serv_pol, n_serv_env):
		Peca.__init__(self, media_cheg, perfuracao, polimento, envernizamento)
		self.n_servicos_perfuracao = n_serv_per
		self.n_servicos_polimento = n_serv_pol
		self.n_servicos_envernizamento = n_serv_env
		self.nome = 'PECA B'
		self.seed = 15

