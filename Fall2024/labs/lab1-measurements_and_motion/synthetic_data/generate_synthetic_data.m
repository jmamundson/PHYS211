t = [0:0.1:10]';

% data set 1
x = 0.2*t -0.3 + 0.2*sin(t) + 0.01*randn(size(t));

data = [t,x];

save data1.txt data -ascii

% data set 2

x = -0.2*t - t.*log10(t) + sqrt(t).*exp(-t) + 0.01*randn(size(t));

data = [t,x];
save data2.txt data -ascii


plotyy(t,x,t,gradient(x,t(2)))

% data set 3

x = tanh(t).*sqrt(t) + 0.005*randn(size(t));

data = [t,x];
save data3.txt data -ascii




