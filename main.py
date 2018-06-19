from tkinter import *
from urls import *



dialg = Tk()
dialg.geometry('400x300+200+200')
dialg.title('Conversor de Moedas')

def btfunf():
    lbdisp['text'] = 'R$:{:.2f} sera convertido em'.format(float(enDig.get()))
    lbdolar['text'] = 'Dolar: ${:.2f}'.format(float(enDig.get())/valordolar)
    lbeuro['text'] = 'Euro: {:.2f}'.format(float(enDig.get())/valoreuro)
    lbbit['text'] = 'Bitcoin: {:.8f}'.format(float(enDig.get())/valorint)
    lbltc['text'] = 'Litecoin: {:.8f}'.format(float(enDig.get())/valorltc)
    lbiota['text'] ='IOTA: {:.4f}'.format(float(enDig.get())/valoriota)
    lbnem['text'] ='NEM: {:.2f}'.format(float(enDig.get())/valornem)
    lbdog['text'] ='Dogecoin: {:.1f}'.format(float(enDig.get())/valordge)

    #Componentes
lbNum = Label(dialg, text='Real:')
lbdisp= Label(dialg, text='')
enDig = Entry(dialg, width=8)
btBut = Button(dialg, text='Converter', command=btfunf)

#Cotação Atual

btcdisp = Label(dialg, text='Bitcoin: {}'.format(valorint) )
ltcdisp = Label(dialg, text='Litecoin: {}'.format(valorltc))
dogdisp= Label(dialg, text='Dogecoin: {}'.format(valordge))
nemdisp= Label(dialg, text='NEM: {}'.format(valornem))
iotadisp= Label(dialg, text='IOTA: {}'.format(valoriota))
dolardisp= Label(dialg, text='Dolar: {}'.format(valordolar))
eurodisp= Label(dialg, text='Euro: {}'.format(valoreuro))


# Moedas convertidas

lbdolar = Label(dialg, text="Dolar:")
lbeuro = Label(dialg, text="Euro:")
lbbit = Label(dialg, text="Bitcoin: ")
lbltc = Label(dialg, text="Litecoin")
lbiota = Label(dialg, text="IOTA")
lbnem = Label(dialg, text="NEM")
lbdog = Label(dialg, text="Dogecoin")
#posição da tela
lbdolar.place(x=10, y=80)
lbeuro.place(x=10, y=100)
lbbit.place(x=10, y=120)
lbltc.place(x=10, y=140)
lbiota.place(x=10, y=160)
lbnem.place(x=10, y=180)
lbdog.place(x=10, y=200)

#Posições
lbdisp.place(x=100, y=10)
lbNum.place(x=10, y=40)
enDig.place(x=50, y=40)
btBut.place(x=130, y=38)
btcdisp.place(x=10, y=280)
ltcdisp.place(x=130, y=280)
dogdisp.place(x=250, y=280)
nemdisp.place(x=10, y=260)
iotadisp.place(x=100, y=260)
dolardisp.place(x=180, y=260)
eurodisp.place(x=280, y=260)

dialg.mainloop()