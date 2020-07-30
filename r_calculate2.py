import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import time
start_time = time.time()
print start_time
campdata0=pd.read_excel('new infection.xlsx',names=None)
new = np.array(campdata0['New infections'])
day = np.array(campdata0['Day'])
date = np.array(campdata0['Date']) 
P = np.array(campdata0['Cumulative infections'])
# raw data 
increase = []
iday = []
selectdate = []
for i in range(len(new)):
	if new[i] > 0:
		iday.append(i)
		increase.append(np.log(P[i]))
		selectdate.append(date[i])
plt.scatter(iday,increase)
iday = np.array(iday)
# phase I 
timex = 30
reg = LinearRegression().fit(iday[0:timex].reshape(-1,1),increase[0:timex])
r1=reg.score(iday[0:timex].reshape(-1,1),increase[0:timex])
x = iday[0:timex] 
date1 = selectdate[0:timex]
y = reg.coef_*iday[0:timex]+reg.intercept_

dp1 = np.exp(y)
plt.plot(x,y,label='phase I (Mar-04~Apri-09): '+'k1='+str(round(reg.coef_[0],2))+' r2= '+str(round(r1,2)))
#plt.plot(x,y,label='k1='+str(round(reg.coef_[0],2))+' r2= '+str(round(r1,2)))

# phase II 
time1 = 30
time2 = 60
reg1 = LinearRegression().fit(iday[time1:time2].reshape(-1,1),increase[time1:time2])
r2=reg1.score(iday[time1:time2].reshape(-1,1),increase[time1:time2])
x = iday[time1:time2] 
y = reg1.coef_*iday[time1:time2]+reg1.intercept_

date2 = selectdate[time1:time2] 
dp2 = np.exp(y)


plt.plot(x,y,label='phase II (April-10-May-09): '+'k2='+str(round(reg1.coef_[0],2))+' r2= '+str(round(r2,2)))
# phase III
time1 = 60
time2 = 110
reg2 = LinearRegression().fit(iday[time1:time2].reshape(-1,1),increase[time1:time2])
r3=reg2.score(iday[time1:time2].reshape(-1,1),increase[time1:time2])
x = iday[time1:time2] 
y = reg2.coef_*iday[time1:time2]+reg2.intercept_
dp3 = np.exp(y)

date3 = selectdate[time1:time2]
plt.plot(x,y,label='phase IV (May10-June8): '+'k3='+str(round(reg2.coef_[0],2))+' r2= '+str(round(r3,2)))
# phase IV
time1 = 110
time2 = -11
reg3 = LinearRegression().fit(iday[time1:time2].reshape(-1,1),increase[time1:time2])
r4=reg3.score(iday[time1:time2].reshape(-1,1),increase[time1:time2])
x = iday[time1:time2] 
y = reg3.coef_*iday[time1:time2]+reg3.intercept_
dp3 = np.exp(y)
print 'yyyyy2',dp3
print reg3.coef_,reg3.intercept_
date3 = selectdate[time1:time2]
print date3[0],date3[-1]
plt.plot(x,y,label='phase IV (June-9-July-20): '+'k3='+str(round(reg3.coef_[0],2))+' r2= '+str(round(r4,2)))

# phase V
time1 = -6
time2 = -1
reg4 = LinearRegression().fit(iday[time1:time2].reshape(-1,1),increase[time1:time2])
r5=reg4.score(iday[time1:time2].reshape(-1,1),increase[time1:time2])
x = iday[time1:time2] 
y = reg4.coef_*iday[time1:time2]+reg4.intercept_
dp4 = np.exp(y)
print 'yyyyy2',dp4
print reg4.coef_,reg4.intercept_
date4 = selectdate[time1:time2]
print date4[0],date4[-1]
plt.plot(x,y,label='phase IV (June-9-July-20): '+'k3='+str(round(reg4.coef_[0],2))+' r2= '+str(round(r5,2)))
plt.legend(scatterpoints=1, frameon=True, labelspacing=1,ncol=1,facecolor='white',edgecolor='white',fontsize='small',bbox_to_anchor=(0.1,1.0,1.0,0.2))

plt.legend()
plt.xlabel('days')
plt.ylabel('log(P)')
plt.title('log(P)~t')
#plt.savefig('Figure4.png')
plt.show()