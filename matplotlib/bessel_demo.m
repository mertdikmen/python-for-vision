x = 0:0.01:10;

figure;
hold on;

for k = 0.5:5.5
    y = besselj(k, x);
    plot(y)
end

title('Different Bessel functions and their local maxima');
