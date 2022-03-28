import pandas as pd
from workalendar.america import Spain
cal = Spain()
feriados=cal.holidays(2022)

df=pd.DataFrame(feriados,columns=['fecha','nombre'])
df['fecha']=pd.to_datetime(df['fecha'])
df['fecha'] = df['fecha'].dt.day_name()
df=df.groupby('fecha').count().sort_values('nombre',ascending = False)
print(df)
