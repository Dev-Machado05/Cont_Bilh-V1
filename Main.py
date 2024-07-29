from src import Time
from src import User
from src import M_txt
from src import U_select
import time
Lt = Time.Lc_time()

M_txt.Ex_td()

if Lt == 0:
    per = "Bom Dia"
elif Lt == 1:
    per = "Boa Tarde"
elif Lt == 2:
    per = "Boa Noite"
else: 
    per = "Olá"


val = float(M_txt.read()[2:-2])

User = User.getUser()
while True:
    print(f"{per} {User}, o seu saldo é atualmente de {val}R$")
    U_select.An_txt()

time.sleep(5)