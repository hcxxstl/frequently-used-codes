
% figures
figure;
subplot(1,3,1); hold on;
plot(data(:,1)', data(:,2)','o-');
plot(data(:,1)', data(:,3)','o-');
% xlim([0 5]); 
ylim([-1 255]);
xlabel("xxx");
ylabel("yyy");
legend('set1','set2');
title('ttt');
hold off;
subplot(1,3,2); hold on;
plot(data7(:,1)', data7(:,3)','o-');
plot(data7(:,1)', data7(:,5)','o-');
hold off;

% import data from txt
run = importdata('result.txt');
data = [run.data];

% import data from csv
w7= xlsread('waveform7.csv');
w8= xlsread('waveform8.csv');
w7nl = xlsread('wave_delay7_nolast.csv');
w7nb = xlsread('wave_delay7_nobuffer.csv');
w7gd = xlsread('wave_delay7.csv');
output = xlsread('output_90ps_all.csv');
outtt = dlmread('log.txt', '\t', [2 0 707 2]);
outff = dlmread('log.txt', '\t', [712 0 1302 2]);
outss = dlmread('log.txt', '\t', [1307 0 2189 2]);
outsf = dlmread('log.txt', '\t', [2194 0 2897 2]);
outfs = dlmread('log.txt', '\t', [2902 0 3614 2]);


% reshape
data = importdata('core10.txt');
data1 = [data.data];	data1 = data1(1:16,:);
power1 = reshape(data1(:,5),[4,4]); 	%p1 = power1/max(power1,[],'all');
area1 = reshape(data1(:,6),[4,4]);

% repmat
data = importdata('core1.txt');
data3 = [data.data];	data3 = data3(1:20,:);
cc1 = repmat(data3(:,7),1,16);
cc2 = repmat(data2(:,7),1,20)';
