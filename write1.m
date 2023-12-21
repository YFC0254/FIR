A=csvread('D:\Thr_1\FIR\data.csv');
% 生成示例音频数据
Fs = 32000; % 采样率

% 将音频数据写入.wav文件
audiowrite('output.wav', A, Fs);
