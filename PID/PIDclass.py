# Diskreetti PID-säädin

class PID:
	def __init__(self, Kp, Ki, Kd):
		self.Kp = Kp
		self.Ki = Ki
		self.Kd = Kd
		self.last_i = 0
		self.last_d = 0
	
	def process(self, set, curr):
		err = float(set - curr)
		
		valP = self.Kp * err # P-termi (proportional)
		
		i = float(self.last_i + err) # lasketaan tämän hetken i-termi
		self.last_i = i
		valI = Ki*i
		
		d = err - self.last_d-
		self.last_d = d
		valD = Kd*d
		
		PID = valP + valI + valD
		return PID