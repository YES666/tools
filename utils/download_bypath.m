% clc,clear;
% filepath = 'E:\WorkSpace\Image Fusion Based on SCM\SourceImage1\series4\downloadMRT2.txt';
% targetpath = 'E:\WorkSpace\Image Fusion Based on SCM\SourceImage1\series4\MRT2series\';
function failuarelist = download_bypath(filepath,targetpath)
% num = 1:111;
% URLs = cell(size(num));
% filenames = cell(size(num));
% for idx  = 1:length(num);
%     URLs{idx} = sprintf('ftp://figment.csee.usf.edu/pub/DDSM/cases/normals/normal_01/',num(idx));
%     filenames{idx} = sprintf('%dflx.2011.avrg.grib',num(idx));
% end

%% �Ѿ��ºõĲ���������
% alreadyfile = dir(fullfile( 'E:\WorkSpace\PCANet_Classifier\Data\CostaRica_Butterflies\Butterflies\', '*.jpg' ));
% filenum = size(alreadyfile,1);
% downfilelist = [];
% count = 1:filenum; i = 1;
% for i = count
% % filescell = struct2cell(alreadyfile);
% % [~,filesnum]=size(filescell);
% downfilelist(i) = alreadyfile(i,1).name;
% % donelist= reshape(filescell(1,:),[filesnum,1]);
% % donelist = cell2mat(donelist);
% end
% filepath = 'E:\WorkSpace\PCANet_Classifier\Data\CostaRica_Butterflies\downloadlinks.txt';
tic;
URLs = importdata(filepath);
num = length(URLs);
cnt = 0;
failuarelist = [];
for idx = 029:029;
    URL =  URLs{idx,1};
    dlmpos = strfind(URL,'/');
    filenames = URL(dlmpos(end)+1:length(URL));
%     if exist(filenames,'file')~=0 
%         continue
%     end
    fprintf(1,'��������%s...\n',filenames);
    [gifpic, status] = urlwrite(URLs{idx},[targetpath, filenames]);
    pause(1);
    if status == 1;
        fprintf(1,'%s�ɹ����أ�\n',filenames);
        gifpic
    else
        fprintf(1,'%s����ʧ�ܣ�\n',filenames);
        cnt = cnt+1;
        failuarelist(cnt,:) =   URL;
    end
end
etime = toc;
fprintf('�������ļ�����%d���ܺ�ʱ��%fs\n',length(num),etime);