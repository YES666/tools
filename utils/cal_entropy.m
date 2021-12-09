
files = dir('Z:\DENSE\features\EC2\*.png');
path_excel = 'C:\Users\502\Desktop\entropy.xlsx';
position = 'F';
result = zeros(length(files),1);

for i  = 1:length(files)
    fileName = [files(i).folder '\' files(i).name];
    image   = imread(fileName);
    
    disp("Start");
    disp('---------------------------Analysis---------------------------');
    output = entropy(image);
    disp(['Done',num2str(i)]);
    result(i) = output;
end
xlswrite(path_excel,result,1,[position '3']);
