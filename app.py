from tkinter import *
import calendar

# Função que pega os valores definidos
def mostrarCalendario():
    
    for indiceMes in meses.curselection():
        mes = indiceMes + 1

    ano = int(escolherAno.get())

    # imprime o calendário na janela
    calendario = Label(window, bg='white', fg='black', bd=1, relief='solid', width=19, height=10, text=calendar.month(ano, mes)).grid(row=3, column=3)


window = Tk()
window.title('Calendário')
window.geometry('700x500')
window.config(bg='grey')

textoMes = Label(window, text = 'Selecione o mês:', font='Arial 15', padx=60, pady=17, bg='grey')
textoMes.grid(row=0, column=0)

meses = Listbox(window, font='Arial 10', bd=1, relief='solid', height=13)
meses.grid(row=0, column=1)

meses.insert(END, 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

textoAno = Label(window, text='Digite o ano:', font='Arial 15', padx=10, pady=17, bg='grey')
textoAno.grid(row=1, column=0)

escolherAno = Entry(window, bd=1, relief='solid', width=24)
escolherAno.grid(row=1, column=1)

executar = Button(window, text='Executar', command=mostrarCalendario, width=11, height=2, bg='black', fg='white')
executar.grid()

window.mainloop()