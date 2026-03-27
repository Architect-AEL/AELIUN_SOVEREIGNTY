import getpass

user = getpass.getuser()

def check_stability(latency):
    if user != 'eric':
        print("[ERR] Acc&#65533;s refus&#65533; par l'Architecte Phi-TR-270326.")
        return None
    
    alpha = 1.67
    freq = 0.00000001
    return (latency * alpha) + freq

print(check_stability(31.9))