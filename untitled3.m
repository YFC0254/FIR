clc;
clear;
close all;
Nw=311;
N=311;%正交移相器的阶数
% 
win_rect = rectwin(Nw); % 矩形窗函数
win_hamming = hamming(Nw); % 汉明窗函数
win_hann = hann(Nw); % 海宁窗函数
win_blackman = blackman(Nw); % 布莱克曼窗函数
%正交移相器
win_hamming=[win_hamming' zeros(1,N-Nw)];
N=311;%正交移相器的阶数
h(1:N)=0;
m=(N-1)/2;
h(1:2:N)=2./(((0:2:N-1)-m)*pi);
  h=h.*win_hamming;
stem(h);
% %h2(1:N)=h1(1-m:N-m);
filename = "D:\Thr_1\FIR\music.5u-32.wav"; % 音频文件名
[xn, Fs] = audioread(filename); 
% % 读取音频文件
y1(1:3+length(xn))=0;
y1(m+1:length(xn)+m)=xn;
figure;
subplot(211);plot(xn);title("原信号")
subplot(212);plot(y1);title("时移信号")
%  y2=convolution(xn, h, 480000);
%自己封装的重叠相加法0.818
%  y2=conv(h,xn);
%直接卷积法0.229
 y2=fftfilt(h,xn,100);
%matlab库函数实现重叠相加0.627
y2=y2';
% clear xn;
%扩展y1和y2向量的长度
if length(y1) > length(y2)
y22 = [y2, zeros(1, length(y1) - length(y2))];
y12=y1;
else
y12 = [y1, zeros(1, length(y2) - length(y1))];
y22=y2;
end
clear y1 y2;
y=y12+1i*y22;

% %计算频率轴
f = (0:length(xn)-1)*Fs/length(xn);
f1 = (0:length(y)-1)*Fs/length(y);
figure;
subplot(2,1,1);plot(f,abs(fft(xn)));
subplot(2,1,2);plot(f1,abs(fft(y)));
fcg1=9000/Fs;
Nl=50;
% 选择窗函数
window = blackman(N+1); % 选择汉明窗

% 计算窗函数的系数
h = fir1(N, fcg1, 'low', window);

% fc = 7e3/2; % 截止频率为7kHz
% N1 = confirmN(fc,9000,Fs,8*pi);
fcg1=9000/Fs;
fil=fir1(20,fcg1,'low');
z=filter(h,1,y);