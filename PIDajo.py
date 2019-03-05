# PID-ajo

def update(Kp, Ki, Kd, Tset, Tcur): # Kp, Ki ja Kd ovat PID-säätimen gain-arvot. Tset on lämpötilan haluttu arvo  ja Tcur mitattu lämpötila-arvo.
    import PIDclass
    PIDajo = PIDclass.PID(Kp, Ki, Kd)
    PID = PIDajo.process(Tset, Tcur)
    print(PID)
