llista = []

def seleccionar_accio():
    while True:
        accio = input('Escull entre Afegir, Eliminar i Sortir: ')

        # Si aquesta opció es selecciona sortirem del programa
        if accio == 'Sortir':
            print('Programa finalitzat')
            return f'Aquesta és la llista després de les modificacions: {llista}'
            break
        if accio == 'Afegir':
            # Mentres l'input de l'usuari sigui un int, li seguirem demanant d'afegir codis
            while True:
                try:
                    afegir = int(input("Afegeix un codi d'infracció: "))
                    if afegir not in llista:
                        llista.append(afegir)
                        print(llista)
                except ValueError:
                    break                    
        elif accio == 'Eliminar':
            # Cada cop que s'elimini un codi, es tornarà al menú principal
            eliminar = int(input('Elimina una infracció: '))
            if eliminar not in llista:
                print('El codi que ha seleccionat no està a la llista.')
            else:
                llista.remove(eliminar)
                print(llista)
            
             
                
print(seleccionar_accio())