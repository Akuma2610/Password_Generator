import string
import secrets
import tkinter
import tkinter.simpledialog
import tkinter.messagebox

alphabet = string.ascii_letters + string.digits + string.punctuation

def generer_un_mdp(longueur):
    mdp=""
    if longueur<6:
        tkinter.messagebox.showerror('Insufficient length', 'Please enter a bigger number of characters (Minimum 6)')
        return
    while True:
        for x in range(longueur):
            mdp+=secrets.choice(alphabet)
        if (any(c.islower() for c in mdp)
                and any(c.isupper() for c in mdp)
                and any(c in string.punctuation for c in mdp)
                and sum(c.isdigit() for c in mdp) >= 3):
            break
        else:
            mdp=''
    return(mdp)
mon_mot_de_passe = generer_un_mdp(tkinter.simpledialog.askinteger('', 'Number of characters :            '))
if mon_mot_de_passe:
    tkinter.messagebox.showinfo('Mot de passe', 'Voici votre mot de passe :' + mon_mot_de_passe)