
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

