#Wir erstellen einen Kunden login und eine Kunden account registrierung

print("Willkommen im Room 847")

#Es wird nach einer antwort gefragt
answer = input("Haben sie bereits ein Konto? (ja oder nein)\n")

#Wenn die antwort "ja" ist dann geht es zum login
if(answer == "ja"):

    print("\nWillkommen Zurück!")
    
    username = input("\nDein Benutzername: ")
    password = input("Geben sie ihr Passwort ein: ")

    print("\n" * 3 + "Willkommen im Room 847 " + username + "!")


    
#Wenn die antwort nicht ja war in der ersten abfrage: Versuche es mit elif und wenn die antwort nein ist geht es weiter mit der registrierung
elif(answer == "nein"): 
    
    
    print("\nHerzlich Willkommen. Erstelle bitte hier ein Konto!")

    email = input("\nGeben sie eine E-Mail adresse ein: ")
    username = input("Geben sie einen Benutzernamen ein: ")
    password = input("Geben sie ein Passwort ein: ")

    print("\n" *5 +  "Willkommen " + username + "! Dein Konto wurde erfolgreich mit der E-Mail adresse: " + email + " erstellt!")

#Wenn die antwort nicht ja und nicht nein ist: Komme hier her und gebe einen Syntax error aus!
elif(answer != "nein", answer != "ja"): {
    print("Syntax error: try yes or no")
}

else:
    print("Unknown error: Please try again. If it doesn't work contact anian@sollingers.de for help")
