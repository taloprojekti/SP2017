def sisalampotila():
    sisanyt = tempread.read_temp_in()
    return sisanyt
    
def main(day, month, year, hour):
    # Setup-osa
    import lukeminen

    #Muodostetaan str-tyyppinen päiväys muodossa "dd.mm.yy" Nordpoolin hintatietojen lukemiseksi
    if day < 10:
        day = str(day)
        day = str("0"+day)
    if month < 10:
        month = str(month)
        month = str("0"+month)

    pvm = str("{}.{}.{}".format(day, month, year))
    print(pvm)

    tiedot = lukeminen.luetiedot(pvm)
    minimi = lukeminen.minimi(tiedot)
    min_delta = lukeminen.min_delta(tiedot, minimi)
    
    # Etsitään ohjelma-tilan alut ja loput

    print("emptying csv-file\n")
    open("tasklists/tasklist-prog.csv", "w").close()

    print("entering loop")
    h=0
    while(True):
        print("h=", h)
        for rivi in min_delta[h:]:
            print(rivi)
            h+=1
            print("h=", h)
            if rivi > 0.19:

                f = open("tasklists/tasklist-prog.csv", "w") # Tähän alkuhetken tallennus
                f.write("start,{:d}-{:d}-{:d},{:d}:{:d}:{:d}\n".format(int(year), int(month), int(day), h-1, 0, 0))

                for rivi in min_delta[h-1:]:
                    print(rivi)
                    h+=1
                    if rivi < 0.19:
                        f = open("tasklists/tasklist-prog.csv", "a") # Tähän päättymishetken tallennus
                        f.write("end,{:d}-{:d}-{:d},{:d}:{:d}:{:d}\n".format(int(year), int(month), int(day), h-1, 0, 0))
                        print("stop") # Tähän päättymishetken tallennus
                        break
                break
            
        # ongelmatilanne, jossa päivän viimeinen luku ei ole alle Pd tai Pdd, jolloin looppi jää avoimeksi.
        
        if h==24:
            break

#Ratkaistaan prog-tilan aikaväli, jonka jälkeen lasketaan mihin lämpötilaan rakennus pitää lämmittää ennen välin alkua.
#Välin aikana lasketaan milloin pitää lämmittää lisää jotta lämpötila pysyy Tmin yläpuolella.
