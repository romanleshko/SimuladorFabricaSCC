#!/usr/bin/env python
# encoding: utf-8
import random
import math
import numpy.random as np
import rand_generator as rg
# Classe para gera��o de n�meros aleat�rios segundos v�rias distribui��es
# Apenas a distribui��o exponencial negativa est� definida


def exponencial(seed, media):
	# """Gera um número segundo uma distribui��o exponencial negativa de m�dia m"""
	rnd = rg.rand(seed)
	return (-media * math.log(rnd))
	#return (-media*math.log(random.random()))


def normal(seed, vals):
	i = random.randint(0,1)
	m = vals[0]
	d = vals[1]
	x1 = 0

	while(True):
		v1 = 2 * rg.rand(seed) - 1

		v2 = 2 * rg.rand(seed) - 1

		w = v1 ** 2 + v2 ** 2
		if w <1:
			break

	aux = math.sqrt(((-2*(math.log(w)))/w))
	y1 = v1*aux
	y2 = v2*aux
	x1 = m + y1*d
	x2 = m + y2*d
	if i==0:
		return x1
	else:
		return x2


#print Aleatorio().exponencial(2) #test
