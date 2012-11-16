X = reshape(randn(5000,2), [5,1000,2]) * .3;

means = [[0,0];[1,1];[1,0];[0,1];[0.5,0.5]];
figure();
hold on;

colors = {'r','g','b','m','y'};

for i = 1:length(means)
    X(i,:,:) = bsxfun(@plus, squeeze(X(i,:,:)), means(i,:));
    plot(X(i,:,1), X(i,:,2),'o', 'MarkerFaceColor', colors{i}, 'MarkerEdgeColor', colors{i});
end

xlim([-1,2]);
ylim([-1,2]);