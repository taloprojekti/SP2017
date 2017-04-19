# Diskreetti PID-säädin

class PID:
	def __init__(self, Kp, Ki, Kd, Imax, Imin):
		self.Kp = Kp
		self.Ki = Ki
		self.Kd = Kd
		self.Imax = Imax
		self.Imin = Imin
		self.last_i = 0
		self.last_d = 0
	
	def process(self, set_T, curr):
		err = float(set_T - curr)
		
		valP = self.Kp * err # P-termi (proportional)
		
		i = float(self.last_i + err) # I-termi (integral)
		self.last_i = i
		
		if i >= self.Imax: # Estetään I-termin rajaton kasvu ja pienentyminen
			i = self.Imax
		if i <= self.Imin:
			i = self.Imin
		valI = self.Ki*i
		
		d = err - self.last_d # D-termi (derivative)
		self.last_d = d
		valD = self.Kd*d
		
		PID = valP + valI + valD
		return PID
