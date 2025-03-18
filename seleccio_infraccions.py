llista = []

def seleccionar_accio():
    while True:
        accio = input('Escull entre Afegir, Eliminar i Sortir: ')

        # Si aquesta opció es selecciona sortirem del programa
        if accio.lower() == 'sortir':
            print('Programa finalitzat')
            return f'Aquesta és la llista després de les modificacions: {llista}'
            
        if accio.lower() == 'afegir':
            # Mentres l'input de l'usuari sigui un int, li seguirem demanant d'afegir codis
            while True:
                try:
                    codi = int(input("Afegeix un codi d'infracció: "))
                    if codi not in llista:
                        llista.append(codi)
                        print(llista)
                    else:
                        print('Aquest codi ja hi és a la llista')
                        print(llista)
                except ValueError:
                    break                   
        elif accio.lower() == 'eliminar':
            try:
                # Cada cop que s'elimini un codi, es tornarà al menú principal
                infraccio = int(input('Elimina una infracció: '))
                if infraccio not in llista:
                    print('El codi que ha seleccionat no està a la llista.')
                else:
                    llista.remove(infraccio)
                    print(llista)
                    
            except ValueError:
                    print('Has d\'escriure un codi vàlid')
                
                    
                
print(seleccionar_accio())
