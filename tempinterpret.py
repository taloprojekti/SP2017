def lampoyhtalo(Tvar, Tmin):
    #tähän laskut 


#Tarkastellaan kuinka lämpimäksi lämmitetään ennen kallista aikaväliä, eli missä vaihtoehdossa kuluu vähiten rahaa
def tempinterpret(tDec, priceNow, Qprice, tStart, tEndh): #tDec = T decision, eli ajanhetki jolla aletaan lämmittää ennen "aikaväliä"
    import tempread
    import setup
    import lukeminen
    C = jtn #määritettävä
    Tfav = setup.Tfav()
    Tmax = setup.Tmax()
    Tmin = setup.Tmin()
    Tin = tempread.read_temp_in()
    TVar = tIn + 0.1
    plist[] = lukeminen.main()
    Tout = tempread.read_temp_out()    
    P = 100 #(Wattia)
    mondic = {}
    c = 0 #vakio joka on vielä määritettävä
    while(Tvar < Tmax):
        tLp = lampoyhtalo(TVar, Tmin) #lämpöyhtälö, joka antaa vastauksenaan leikkausajankohdan eli kuinka monta sekuntia tStartista
        tEsth = tStart + tLp // 3600
        tEstm = (tLp - (tLp // 3600 * 3600)) // 60
        if tEsth > tEnd:
            return Tvar
        mon0 = C * (Tvar - Tin) * priceNow #kuinka paljon kuluu rahaa lämmittää ennen aikaväliä haluttuun lämpötilaan
        for i in range(tEstm, 60):
                if  (i % Prat = 0): #Prat siis jäähtymis- ja lämmitystehojen suhde, joka joudutaan vielä määrittämään
                    mon1 += 60 * P * plist[tEsth]
                mon1 = 60 * P * plist[tEsth] #jossa P on lämmittimen teho , kertoo kuinka paljon aikavälillä kuluu rahaa
        for j in range(tEsth + 1, tEnd):
            mon1 += (3600 // Prat) * P * plist[j] #jossa P on lämmittimen teho
        mon = mon0 + mon1 #rahaa yhteensä
        mondic[float(Tvar)] = float(mon)
        Tvar += 0.1
    Tvar = min(mondic, key = mondic.get)    
        
    return Tvar #HUOM! ajastimeen on tehtävä vielä erillinen haara joka tarkastelee onko sen hetkinen aika em. T decision aikavälillä ja
                #onko sen hetkinen lämpötila yli vai alle Tvarin
    
    
