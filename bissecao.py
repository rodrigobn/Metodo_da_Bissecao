# -*- coding: utf-8 -*-
from copy import copy
from math import log10, ceil, fabs

def _fa(funcao, x):
	'''
	Resultado da função f(a) no ponto A do intervalo [a,b]

	Parametro:\n
	a = ponto a do intervalo [a,b]
	'''
	return eval(funcao)

def _fb(funcao, x):
	'''
	Resultado da função f(b) no ponto B do intervalo [a,b]

	Parametro:\n
	b = ponto b do intervalo [a,b]
	'''
	return eval(funcao)

def _fxn(funcao, x):
	'''
	Resultado da função f(xn) no ponto medio do intervalo [a,b]
	
	Parametro:\n
	xn = ponto medio entre o intervalo [a,b]
	'''
	return eval(funcao)

def verificaSeTemRaiz(fa, fb):
	'''
	Verifica se tem raiz entre duas funções. Se o resultado da multiplicação entre elas for negativo
	
	Parametros:\n
	fa = o resultado de uma função no ponto 'a' do intervalo [a,b]\n
	fb = o resultado de uma função no ponto 'b' do intervalo [a,b]

	Retorno: boolean
	'''
	if fa * fb < 0:
		return True
	else:
		return False

def biseccao(equacao, intervalo, condParada):
	'''
	Metodo usado para encontrar o ponto, aproximado, da raiz de uma função polinomial -> f(x) ~= 0.0

	Parametros: \n
	intervalo = Intervalo [a,b] onde se encontra a raiz da função \n
	condParada = Valor que satisfaça a aproximação do valor da raiz ex: 0,001 ou 10**-3

	Retorno: Ponto aproximado onde esta a raiz / valor da aproximação da raiz. -> f(x) ~= 0
	'''
	
	# formula para numero aproximado de iterações
	k = (log10(intervalo[1] - intervalo[0])	- log10(condParada)) / log10(2)
	
	a = intervalo[0]
	b = intervalo[1]	
	funcao = equacao

	if verificaSeTemRaiz(_fa(funcao, a), _fb(funcao, b)):
		print("Intervalo = [{}, {}]".format(a,b))
		print('-' * 50)
		#ceil(k) Arredonda pra cima o numero de iterações k
		for i in range(ceil(k)-1):

			#xn = ponto Medio do intervalo, subistituindo o x da função principal
			xn = (a+b)/2

			# Verifica se a função com o ponto medio f(xn) ja é a raiz
			if _fxn(funcao, xn) == 0:
				return "Raiz = {}".format(xn)

			# novo intervalo dividido ao meio dependendo da condição. [a, xn] ou [xn, b]
			elif verificaSeTemRaiz(_fa(funcao, a), _fxn(funcao, xn)):
				b = xn							
			elif verificaSeTemRaiz(_fb(funcao, b), _fxn(funcao, xn)):
				a = xn
			
			print("{} iteração: [{}, {}]".format(i+1,a,b))
		
		# Enquanto o resultado aproximado da raiz da função f(xn) for negativo ou maior que a condição de parada, continua iterando
		while(_fxn(funcao, xn) < 0):			
			#xn = ponto Medio do intervalo, subistituindo o x da função principal
			xn = (a+b)/2			
			
			# Verifica se a função com o ponto medio f(xn) ja é a raiz
			if _fxn(funcao, xn) == 0:
				return "Raiz = ", xn

			# novo intervalo dividido ao meio dependendo da condição. [a, xn] ou [xn, b]
			elif verificaSeTemRaiz(_fa(funcao, a), _fxn(funcao, xn)):
				b = xn							
			elif verificaSeTemRaiz(_fb(funcao, b), _fxn(funcao, xn)):
				a = xn
			
			print("iteração extra: [{:.6f}, {:.6f}]".format(a,b))
		
		print('-' * 50)
		print("Ponto no eixo x = ", b)
		print('-' * 50)
		print("Valor aproximado da raiz nesse ponto = ", _fxn(funcao, xn))
		
		return 'Ponto no eixo x = {} \n Raiz aproximada = {}'.format(b, _fxn(funcao, xn))
	else:
		print("Não tem raiz no intervalo[{},{}]".format(a, b))

		return "Não tem raiz no intervalo[{},{}]".format(a, b)

