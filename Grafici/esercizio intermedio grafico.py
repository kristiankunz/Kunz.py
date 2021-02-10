dall'importazione casuale randint
f = open ("dati.txt", 'w')
dati = ""
per riga nella gamma (100):
    per elemento in range (1):
        dati = dati + str (randint (1,100)) + "," + str (randint (1,100))
    dati = dati + "\ n"
stampa (dati)
f.write (dati)
f.close ()

importa numpy come np
importa matplotlib.pyplot come plt


f = open ("dati.txt", 'r')
coordX = []
coordY = []

per riga in f:
    valori = str (f.readline ())  
    Nval = len (valori)          
    valori = valori.strip ('\ n') 
    valori = valori.split (',')  
    valori = list (valori)       
    print (valori)
    coordX.append (int (valori [0])) 
    coordY.append (int (valori [1])) 

f.close ()  

print ("X:", coordX)
print ("Y:", coordY)

coordX.sort ()
coordY.sort ()

print ("liste ordinate:") 
print ("X:", coordX)
print ("Y:", coordY)

print (tipo (coordX))
print (tipo (coordY))


plt.scatter (coordX, coordY)
plt.ylabel ('alcuni numeri')
plt. mostra ()
