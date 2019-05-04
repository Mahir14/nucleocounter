import os
from tkinter import *
from tkinter import filedialog
from datetime import datetime
import time

x = Tk()
x.title("Nucleocounter")
x.iconbitmap('logo_6Pr_icon.ico')

def debugLog(t):
    global OUTPUT
    OUTPUT.insert(END,t)

def clearLog():
    OUTPUT.delete(1.0,END)

def compare():
    clearLog()
    
    file1 = filedialog.askopenfilename()
    file2 = filedialog.askopenfilename()

    if not file1.endswith('.txt') and not file1.endswith('.fasta'):
        print("Invalid filetype. Only .txt or .fasta files are supported.")
    elif not file2.endswith('.txt') and not file2.endswith('.fasta'):
        print("Invalid filetype. Only .txt or .fasta files are supported.")
    else:
        diff=0
        len1 =0
        len2 =0
        gene1 = open(file1)
        gene2 = open(file2)
        file1name = os.path.basename(file1)
        file2name = os.path.basename(file2)
        debugLog("Comparing "+file1name+" to "+file2name+"."+'\n')

        c1 = open(file1)
        c2 = open(file2)

        c1.readline()
        c2.readline()

        for line in c1:
            for c in line:
                len1 +=1

        for line in c2:
            for c in line:
                len2 +=1

        debugLog(file1name+" consists of "+str(len1)+" bases.\n")
        debugLog(file2name+" consists of "+str(len2)+" bases.\n")

        c1.close()
        c2.close()
        ##
        
        gene1.readline()
        gene2.readline()

        for line1,line2 in zip(gene1,gene2):
            for base1,base2 in zip(line1,line2):
                if base1.upper() != base2.upper():
                    diff += 1

        debugLog("There are "+str(diff)+" differences in base pairs."+'\n')
        gene1.close()
        gene2.close()

##
def openf():
    
    A=0
    T=0
    G=0
    C=0

    f = filedialog.askopenfilename()
    
    if not f.endswith('.txt') and not f.endswith('.fasta'):
            print("Invalid filetype. Only .txt or .fasta files are supported.")
                
    else:
        z=""
        gene = open(f,"r")
        gene.readline() #Skips first line
        for line in gene:
            line = line.upper()
            for base in line:
                if base == "G":
                    G+=1
                if base == "C":
                    C+=1
                if base == "A":
                    A+=1
                if base == "T":
                    T+=1

        clearLog()
        z="Adenine: "+str(A)+"\n"
        debugLog(z)
        z="Thymine: "+str(T)+"\n"
        debugLog(z)
        z="Guanine: "+str(G)+"\n"
        debugLog(z)
        z="Cytosine: "+str(C)+"\n"
        debugLog(z)
        GeneLen = A+G+C+T+0.
        
        GC = 100*(G+C+0.)/(GeneLen)
        AT = 100*(A+T+0.)/(GeneLen)
        debugLog("Percentage of G-C base pairs is "+str(round(GC,2))+"%"+"\n")
        debugLog("Pecentage of A-T base pairs is "+str(round(AT,2))+"%" )
        gene.close()

def phase():
    COVERIMAGE.destroy()
    START.destroy()
    CONVERTtext.lift()
    TITLE.lift()
    COMPARE.lift()
    COPR.lift()
    OUTPUT.lift()
    
def ENTER():
    print("Enter pressed")

DNAimg = PhotoImage(file="DNAstrand.png")

COVERIMAGE = Label(x, image=DNAimg)
COVERIMAGE.grid(row=1, column=0, columnspan=3, sticky=W)

START = Button(x, text="Start", fg="white", bg="red", font="Fixedsys 24 bold",borderwidth=0, command=lambda: phase() )
START.place(relx=0.5,rely=0.9, anchor=CENTER)
##


TITLE = Label(x, text="Nucleocounter", fg="black", bg="white", font="Fixedsys 30 bold")
TITLE.place(relx=0.5, rely=0.1, anchor=CENTER)
TITLE.lower()

CONVERTtext = Button(x, text="Open gene file", fg="white", bg="gray", font="Fixedsys 27 bold", borderwidth=0, command=lambda: openf() )
CONVERTtext.place(relx=0.7, rely=0.3, anchor=CENTER)
CONVERTtext.lower()

COMPARE = Button(x, text="Compare Genes", fg="white", bg="orange", font="Fixedsys 27 bold", borderwidth=0, command=lambda: compare())
COMPARE.place(relx=0.29, rely=0.3, anchor=CENTER)
COMPARE.lower()

COPR = Label(x, text="MahirTech MMXIX ©", fg="white", bg="green", font="Fixedsys 16")
COPR.place(relx=0.1, rely=0.05, anchor=CENTER)
COPR.lower()

OUTPUT = Text(x, width=50, height=6, wrap=WORD, background="white", font="System 26")
OUTPUT.place(relx=0.5, rely=0.65, anchor=CENTER)  
OUTPUT.lower()

x.mainloop()
