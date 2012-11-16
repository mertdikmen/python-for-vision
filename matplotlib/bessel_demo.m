x = 0:0.01:10;

figure;
hold on;

Y = zeros(0,length(x));

for k = 0.5:5.0
    Y(end+1,:) = besselj(k, x);
    f = @(x) -besselj(k,x);
    fmax = fminunc(f, 1);
    plot(fmax, besselj(k,fmax),'ok','MarkerFaceColor','red');
end
plot(x,Y','LineWidth',1);
grid();
ylim([-.4,0.8]);
set(gca,'XTick',2:2:10);
title('Different Bessel functions and their local maxima');
