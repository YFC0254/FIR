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