clc,clear;
num = 00:100;
URLs = cell(size(num));
folder_filenames = cell(size(num));
filenames = cell(size(num));
filenames1 = cell(size(num));
a = 1;
save_folder = 'C:/Users/502/Desktop/NEW_ATLAS/patient13/';
init_url = 'http://www.med.harvard.edu/aanlib/cases/case13/';

save_folder = [save_folder 'CT/'];
init_url = [init_url 'ct1/'];
if exist(save_folder,'dir')==0
    mkdir(save_folder)
end
%http://www.med.harvard.edu/aanlib/cases/case3/mr1-tc1/040.html
for idx  = 1:length(num)
    b = num2str(a,'%03d');
    URLs{idx} = sprintf([init_url,b,'.gif']);
    
     
    filenames{idx} = sprintf([save_folder,'%d.png'],a);
    a = a+1;
end

tic;
for idx = 1:length(num)
    fprintf(1,'正在下载%s...\n',filenames{idx});
    [f] = websave(filenames{idx},URLs{idx});

       

%     if status == 1
% %         fprintf(1,'%s成功下载！\n',filenames{idx});
%     else
%         fprintf(1,'%s下载失败！\n',filenames{idx});
%     end

end
etime = toc;
fprintf('总下载文件数：%d，总耗时：%fs\n',length(num),etime);