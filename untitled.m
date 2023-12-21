[y,fs1] = audioread('music1u-32.wav');

% 设计FIR低通滤波器
% 定义滤波器参数
fc = 6900; % 截止频率
fs = fs1; % 采样频率
M =1001; % 滤波器长度
% 计算归一化截止频率
wc = 2*pi*fc/fs;
% 设计滤波器
n = -(M-1)/2:(M-1)/2;
hd = sin(wc*n)./(pi*n);
hd((M+1)/2) = wc/pi; % 窗口校正
% 应用不同的窗口函数
w1 = rectwin(M)';
w2 = bartlett(M)';
w3 = hamming(M)';
w4 = hann(M)';
w5 = blackman(M)';
h1 = hd.*w1;
h2 = hd.*w2;
h3 = hd.*w3;
h4 = hd.*w4;
h5 = hd.*w5;
% 绘制频率响应
[H1, f1] = freqz(h1, 1, 1024, fs);
[H2, f2] = freqz(h2, 1, 1024, fs);
[H3, f3] = freqz(h3, 1, 1024, fs);
[H4, f4] = freqz(h4, 1, 1024, fs);
[H5, f5] = freqz(h5, 1, 1024, fs);
figure;
plot(f1, abs(H1), f2, abs(H2), f3, abs(H3), f4, abs(H4), f5, abs(H5));
xlabel('Frequency (Hz)');
ylabel('Magnitude');
legend('Rectangular', 'Bartlett', 'Hamming', 'Hann', 'Blackman');
% 应用滤波器
y1 = filter(H1, 1, y);
y2 = filter(H2, 1, y);
y3 = filter(H3, 1, y);
y4 = filter(H4, 1, y);
y5 = filter(H5, 1, y);
y4_normalized = y4 / max(abs(y4)); % 将音频数据归一化

% 将音频数据写入.wav文件
audiowrite('output3.wav', real(y4_normalized), fs1);


