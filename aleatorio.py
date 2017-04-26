#!/usr/bin/env python
# encoding: utf-8
import random
import math
import numpy.random as np
import rand_generator as rg
# Classe para gera��o de n�meros aleat�rios segundos v�rias distribui��es
# Apenas a distribui��o exponencial negativa est� definida

class Aleatorio:

	nX1 = 0
	nX2 = 0
	rX2 = False
	seed = 0


	def exponencial(self, seed, media):
		# """Gera um número segundo uma distribui��o exponencial negativa de m�dia m"""
		rnd = rg.rand(seed)
		return (-media * math.log(rnd))
		#return (-media*math.log(random.random()))


	def normal(self, seed, vals):

		if Aleatorio.rX2 and seed == Aleatorio.seed:

			Aleatorio.rX2 = False
			return Aleatorio.nX2

		Aleatorio.seed = seed

		i = random.randint(0,1)
		m = vals[0]
		d = vals[1]


		while(True):
			v1 = 2 * rg.rand(seed) - 1

			v2 = 2 * rg.rand(seed) - 1

			w = v1 ** 2 + v2 ** 2
			if w <1:
				break

		aux = math.sqrt(((-2*(math.log(w)))/w))
		y1 = v1*aux
		y2 = v2*aux
		Aleatorio.nX1 = m + y1*d
		Aleatorio.nX2 = m + y2*d

		Aleatorio.rX2 = True
		#print('Aleatório rX1: ', Aleatorio.nX1)
		return Aleatorio.nX1



	#print Aleatorio().exponencial(2) #test
