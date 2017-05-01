from tkinter import *

import simulador

class Application(Frame):
    def __init__(self, master=None):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        Frame.__init__(self, master)
        self.pack()


def save():
    simulador.chegA = mediaChegA.get()
    simulador.chegB = mediaChegB.get()
    simulador.perfA[0] = mediaPerfA.get()
    simulador.perfB[0] = mediaPerfB.get()
    simulador.perfA[1] = desvioPerfA.get()
    simulador.perfB[1] = desvioPerfB.get()
    simulador.env[0] = mediaEnv.get()
    simulador.env[1] = desvioEnv.get()
    simulador.n_ser_perfA = nServPerfA.get()
    simulador.n_ser_polA = nServPolA.get()
    simulador.n_ser_perfB = nServPerfB.get()
    simulador.n_ser_polB = nServPolB.get()
    simulador.n_ser_env = nServEnv.get()
    simulador.polA[0] = mediaPolA.get()
    simulador.polA[1] = desvioPolA.get()
    simulador.polB[0] = mediaPolB.get()
    simulador.polB[1] = desvioPolB.get()
    simulador.s.executa(simulador.t)



root = Tk()
app = Application(root)


msg = Label(app, text="Tempo Medio de Chegada - Tipo A:")
msg.pack()
mediaChegA = StringVar()
passEntry = Entry(app, textvariable=mediaChegA)
passEntry.insert(0, simulador.chegA)
passEntry.pack()

msg = Label(app, text="Tempo Medio de Chegada - Tipo B:")
msg.pack()
mediaChegB = StringVar()
passEntry = Entry(app, textvariable=mediaChegB)
passEntry.insert(0, simulador.chegB)
passEntry.pack()

msg = Label(app, text="Tempo Medio de Perfuracao - Tipo A:")
msg.pack()
mediaPerfA = StringVar()
passEntry = Entry(app, textvariable=mediaPerfA)
passEntry.insert(0, simulador.perfA[0])
passEntry.pack()

msg = Label(app, text="Tempo Medio de Perfuracao - Tipo B:")
msg.pack()
mediaPerfB = StringVar()
passEntry = Entry(app, textvariable=mediaPerfB)
passEntry.insert(0, simulador.perfB[0])
passEntry.pack()

msg = Label(app, text="Desvio Padrao de Perfuracao - Tipo A:")
msg.pack()
desvioPerfA = StringVar()
passEntry = Entry(app, textvariable=desvioPerfA)
passEntry.insert(0, simulador.perfA[1])
passEntry.pack()

msg = Label(app, text="Desvio Padrao de Perfuracao - Tipo B:")
msg.pack()
desvioPerfB = StringVar()
passEntry = Entry(app, textvariable=desvioPerfB)
passEntry.insert(0, simulador.perfB[1])
passEntry.pack()

msg = Label(app, text="Tempo Medio de Polimento - Tipo A:")
msg.pack()
mediaPolA = StringVar()
passEntry = Entry(app, textvariable=mediaPolA)
passEntry.insert(0, simulador.polA[0])
passEntry.pack()

msg = Label(app, text="Desvio Padrao de Polimento - Tipo A:")
msg.pack()
desvioPolA = StringVar()
passEntry = Entry(app, textvariable=desvioPolA)
passEntry.insert(0, simulador.polA[1])
passEntry.pack()

msg = Label(app, text="Tempo Medio de Polimento - Tipo B:")
msg.pack()
mediaPolB = StringVar()
passEntry = Entry(app, textvariable=mediaPolB)
passEntry.insert(0, simulador.polB[0])
passEntry.pack()

msg = Label(app, text="Desvio Padrao de Polimento - Tipo B:")
msg.pack()
desvioPolB = StringVar()
passEntry = Entry(app, textvariable=desvioPolB)
passEntry.insert(0, simulador.polB[1])
passEntry.pack()

msg = Label(app, text="Tempo Medio Envernizamento:")
msg.pack()
mediaEnv = StringVar()
passEntry = Entry(app, textvariable=mediaEnv)
passEntry.insert(0, simulador.env[0])
passEntry.pack()

msg = Label(app, text="Desvio Padrao Envernizamento:")
msg.pack()
desvioEnv = StringVar()
passEntry = Entry(app, textvariable=desvioEnv)
passEntry.insert(0, simulador.env[1])
passEntry.pack()

msg = Label(app, text="Num Servico Filas Perfuracao - Tipo A:")
msg.pack()
nServPerfA = StringVar()
passEntry = Entry(app, textvariable=nServPerfA)
passEntry.insert(0, simulador.n_ser_perfA)
passEntry.pack()

msg = Label(app, text="Num Servico Filas Polimento - Tipo A:")
msg.pack()
nServPolA = StringVar()
passEntry = Entry(app, textvariable=nServPolA)
passEntry.insert(0, simulador.n_ser_polA)
passEntry.pack()

msg = Label(app, text="TNum Servico Filas Perfuracao - Tipo B:")
msg.pack()
nServPerfB = StringVar()
passEntry = Entry(app, textvariable=nServPerfB)
passEntry.insert(0, simulador.n_ser_perfB)
passEntry.pack()

msg = Label(app, text="Num Servico Filas Polimento - Tipo B:")
msg.pack()
nServPolB = StringVar()
passEntry = Entry(app, textvariable=nServPolB)
passEntry.insert(0, simulador.n_ser_polB)
passEntry.pack()

msg = Label(app, text="Num Servico Filas Envernizamento:")
msg.pack()
nServEnv = StringVar()
passEntry = Entry(app, textvariable=nServEnv)
passEntry.insert(0, simulador.n_ser_env)
passEntry.pack()

submit = Button(app, text='Save', command=save).pack(side=LEFT)

app.bye = Button(app, text="Bye", command=app.quit)
app.bye.pack()


app.master.title("SCC: Estudo do funcionamento dum sector duma fábrica")
app.master.geometry("800x800+350+0")

root.mainloop()