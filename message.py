class Message :
    def __init__(self, mittente, destinatario) :
        self.mittente= mittente
        self.destinatario= destinatario
        self.testo= []
    def append (self,riga) :
        self.testo.append(riga)
    def toString (self):
        return "Mittente: "+self.mittente+ "\nDestinatario: "+ self.destinatario+ "\nMessaggio: \n  "+"\n  ".join(self.testo)
messaggio= Message("Christian","Lorenzo")   
messaggio.append("ciao Lorenzo")
messaggio.append("come mai oggi non sei venuto? ")
messaggio.append("rimettiti presto")
messaggio.append("saluti, Christian")
print(messaggio.toString())




