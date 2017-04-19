#!/usr/bin/env python
# encoding: utf-8
import random
import math
import numpy.random as np

# Classe para gera��o de n�meros aleat�rios segundos v�rias distribui��es
# Apenas a distribui��o exponencial negativa est� definida


def exponencial(media):
	# """Gera um número segundo uma distribui��o exponencial negativa de m�dia m"""
	return (-media*math.log(random.random()))

def normal(vals):
	return np.normal(vals[0], vals[1])

#print Aleatorio().exponencial(2) #test