from bissecao import *
from tkinter import * # importanto toda a biblioteca

class Application:
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
        self.sextoConteiner['pady'] = 10
        self.sextoConteiner.pack()

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
        self.calcula['command'] = self.bicessao
        self.calcula.pack()

        self.reseta = Button(self.quintoConteiner)
        self.reseta['text'] = 'reseta'
        self.reseta['font'] = ('Calibri', '8')
        self.reseta['width'] = 12
        self.reseta['command'] = self.limpar
        self.reseta.pack()

    def bicessao(self):
        if self.funcao.get() != '' and self.intervaloA.get() != '' and self.intervaloB.get() != '' and self.tolerancia.get() != '':
            funcao = self.funcao.get()
            intervaloA = float(self.intervaloA.get())
            intervaloB = float(self.intervaloB.get())
            tolerancia = float(self.tolerancia.get())

            # Pega o retorno da função para colocar no container da resposta
            resposta = biseccao(funcao, [intervaloA, intervaloB], tolerancia)
            
            #Cria a mensagem e plota na tela no container passado por parametro
            self.mensagem = Label(self.sextoConteiner, text=resposta, font=self.fontePadrao)
            self.mensagem.pack()
    
    def limpar(self):
        #Limpa os campos
        self.funcao.delete(0, 'end')
        self.intervaloA.delete(0, 'end')
        self.intervaloB.delete(0, 'end')
        self.tolerancia.delete(0, 'end')
        
        #Destroi o container da resposta e restaura o espaço
        self.sextoConteiner.destroy()
        self.sextoConteiner = Frame()
        self.sextoConteiner['pady'] = 30
        self.sextoConteiner.pack(side=LEFT)

# instanciando a classe TK() para que os widgets possam ser utilizados na aplicação
root = Tk()
Application(root)
# exibir a tela. Sem o event loop, a interface não será exibida
root.mainloop()