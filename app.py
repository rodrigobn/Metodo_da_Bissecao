from tkinter import *
from copy import copy
from math import log10, ceil, fabs
import tkinter.messagebox as tkmsg


class Application():
    '''
    Classe que contem os controles que serão exibidos na tela
    '''
    def __init__(self, master=None):
        self.fontePadrao = ('Arial', '10')
        
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 10 # Padding (espaçamentos internos)
        self.primeiroContainer.pack()

        self.segundoConteiner = Frame(master)
        self.segundoConteiner['pady'] = 10
        self.segundoConteiner.pack()

        self.terceiroConteiner = Frame(master)
        self.terceiroConteiner['pady'] = 10
        self.terceiroConteiner.pack()

        self.quartoConteiner = Frame(master)
        self.quartoConteiner['pady'] = 10
        self.quartoConteiner.pack()

        self.quintoConteiner = Frame(master)
        self.quintoConteiner['pady'] = 10
        self.quintoConteiner.pack()

        self.sextoConteiner = Frame(master)
        self.sextoConteiner['pady'] = 20
        self.sextoConteiner.pack()
        
        self.setimoConteiner = Frame(master)
        self.setimoConteiner['pady'] = 10
        self.setimoConteiner.pack()

        self.titulo = Label(self.primeiroContainer, text = 'Metodo da Bisseção')
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()

        self.funcaoLabel = Label(self.segundoConteiner, text = 'Função = ', font=self.fontePadrao)
        self.funcaoLabel.pack(side=LEFT)

        self.funcao = Entry(self.segundoConteiner)
        self.funcao['width'] = 30
        self.funcao['font'] = self.fontePadrao
        self.funcao.pack(side=LEFT)

        self.intervaloALabel = Label(self.terceiroConteiner, text = 'Intervalo A [', font=self.fontePadrao)
        self.intervaloALabel.pack(side=LEFT)

        self.intervaloA = Entry(self.terceiroConteiner)
        self.intervaloA['width'] = 5
        self.intervaloA['font'] = self.fontePadrao
        self.intervaloA.pack(side=LEFT)

        self.intervaloALabel = Label(self.terceiroConteiner, text = '] Intervalo B', font=self.fontePadrao)
        self.intervaloALabel.pack(side=RIGHT)
        
        self.intervaloB = Entry(self.terceiroConteiner)
        self.intervaloB['width'] = 5
        self.intervaloB['font'] = self.fontePadrao
        self.intervaloB.pack(side=RIGHT)

        self.toleranciaLabel = Label(self.quartoConteiner, text = 'Tol = ', font=self.fontePadrao)
        self.toleranciaLabel.pack(side=LEFT)
        
        self.tolerancia = Entry(self.quartoConteiner)
        self.tolerancia['width'] = 10
        self.tolerancia['font'] = self.fontePadrao
        self.tolerancia.pack()

        self.calcula = Button(self.quintoConteiner)
        self.calcula['text'] = 'Calcular'
        self.calcula['font'] = ('Calibri', '8')
        self.calcula['width'] = 12
        self.calcula['command'] = self.resultado
        self.calcula.pack()

        self.reseta = Button(self.quintoConteiner)
        self.reseta['text'] = 'reseta'
        self.reseta['font'] = ('Calibri', '8')
        self.reseta['width'] = 12
        self.reseta['command'] = self.limparTela
        self.reseta.pack()

        #self.mostraIntervalos = Entry(self.quartoConteiner)

    def resultado(self):
        if self.funcao.get() != '' and self.intervaloA.get() != '' and self.intervaloB.get() != '' and self.tolerancia.get() != '':
            funcao = self.funcao.get()
            intervaloA = float(self.intervaloA.get())
            intervaloB = float(self.intervaloB.get())
            tolerancia = float(self.tolerancia.get())

            # Pega o retorno da função para colocar no container da resposta
            resposta = self.biseccao(funcao, [intervaloA, intervaloB], tolerancia)
            
            #Cria a mensagem e plota na tela no container passado por parametro
            self.mensagem = Label(self.sextoConteiner, text=resposta, font=self.fontePadrao)
            self.mensagem.pack()
    
    def limparTela(self):
        #Limpa os campos
        self.funcao.delete(0, 'end')
        self.intervaloA.delete(0, 'end')
        self.intervaloB.delete(0, 'end')
        self.tolerancia.delete(0, 'end')
        
        #Destroi o container da resposta e restaura o espaço
        self.sextoConteiner.destroy()
        self.sextoConteiner = Frame()
        self.sextoConteiner['pady'] = 30
        self.sextoConteiner.pack()
    
    def _fa(self, funcao, x):
        '''
        Resultado da função f(a) no ponto A do intervalo [a,b]

        Parametro:\n
        a = ponto a do intervalo [a,b]
        '''
        return eval(funcao)

    def _fb(self, funcao, x):
        '''
        Resultado da função f(b) no ponto B do intervalo [a,b]

        Parametro:\n
        b = ponto b do intervalo [a,b]
        '''
        return eval(funcao)

    def _fxn(self, funcao, x):
        '''
        Resultado da função f(xn) no ponto medio do intervalo [a,b]
        
        Parametro:\n
        xn = ponto medio entre o intervalo [a,b]
        '''
        return eval(funcao)

    def verificaSeTemRaiz(self, fa, fb):
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

    def biseccao(self, equacao, intervalo, condParada):
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

        if self.verificaSeTemRaiz(self._fa(funcao, a), self._fb(funcao, b)):
            
            # Cria um label e imprime o intervalo definido pelo usuario
            self.intervalosLabel = Label(self.sextoConteiner, text="Intervalo = [{}, {}]".format(a,b), font=self.fontePadrao)
            self.intervalosLabel.pack()

            # Cria um label e imprime um separador pontilhado
            self.separadorLabel = Label(self.sextoConteiner, text='-' * 50, font=self.fontePadrao)
            self.separadorLabel.pack()
            

            #ceil(k) Arredonda pra cima o numero de iterações k
            for i in range(ceil(k)-1):

                #xn = ponto Medio do intervalo, subistituindo o x da função principal
                xn = (a+b)/2

                # Verifica se a função com o ponto medio f(xn) ja é a raiz
                if self._fxn(funcao, xn) == 0:
                    return "Raiz = {}".format(xn)

                # novo intervalo dividido ao meio dependendo da condição. [a, xn] ou [xn, b]
                elif self.verificaSeTemRaiz(self._fa(funcao, a), self._fxn(funcao, xn)):
                    b = xn							
                elif self.verificaSeTemRaiz(self._fb(funcao, b), self._fxn(funcao, xn)):
                    a = xn
                
                #Cria e imprime um label com as interações do metodo
                self.iteraçõesLabel = Label(self.sextoConteiner, text="{} iteração: [{}, {}]".format(i+1,a,b), font=self.fontePadrao)
                self.iteraçõesLabel.pack()
                print("{} iteração: [{}, {}]".format(i+1,a,b))
            
            # Enquanto o resultado aproximado da raiz da função f(xn) for negativo ou maior que a condição de parada, continua iterando
            while(self._fxn(funcao, xn) < 0):			
                #xn = ponto Medio do intervalo, subistituindo o x da função principal
                xn = (a+b)/2			
                
                # Verifica se a função com o ponto medio f(xn) ja é a raiz
                if self._fxn(funcao, xn) == 0:
                    return "Raiz = ", xn

                # novo intervalo dividido ao meio dependendo da condição. [a, xn] ou [xn, b]
                elif self.verificaSeTemRaiz(self._fa(funcao, a), self._fxn(funcao, xn)):
                    b = xn							
                elif self.verificaSeTemRaiz(self._fb(funcao, b), self._fxn(funcao, xn)):
                    a = xn
                
                print("iteração extra: [{:.6f}, {:.6f}]".format(a,b))
            
            print('-' * 50)
            print("Ponto no eixo x = ", b)
            print('-' * 50)
            print("Valor aproximado da raiz nesse ponto = ", self._fxn(funcao, xn))
            
            return 'Ponto no eixo x = {} \n Raiz aproximada = {}'.format(b, self._fxn(funcao, xn))
        else:
            print("Não tem raiz no intervalo[{},{}]".format(a, b))

            return "Não tem raiz no intervalo[{},{}]".format(a, b)


# instanciando a classe TK() para que os widgets possam ser utilizados na aplicação
root = Tk()
Application(root)
# exibir a tela. Sem o event loop, a interface não será exibida
root.mainloop()