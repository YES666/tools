path = 'C:/Users/502/Desktop/BW/T2';
savepath = 'C:/Users/502/Desktop/BrainWeb/T2';
if ~exist(savepath,'dir')
    mkdir(savepath);
end
dir1 = dir(path);
n = 0;
for i = 1:(length(dir1)-2)
    rawb_path = fullfile(path,dir1(i+2).name);
    fid = fopen(rawb_path);
    temp = fread(fid, 181 * 217 * 181);
    images = reshape(temp, 181 , 217, 181);
    for j = 1:181
        img = images(:,:,j);
        img = uint8(imrotate(img, 90));
        imwrite(img,fullfile(savepath,[num2str(n) '.png']));
        n = n+1;
    end
end





function g = readrawb(filename, num)
% ����readrawb(filename, num)�еĵ�һ������filename������ȡ��rawb�ļ����ļ������ڶ�������num���ǵڶ����š�
fid = fopen(filename);
% ������ȡ181*217*181�����ݣ���ʱ��temp��һ������Ϊ181*217*181��������
% �Ƚ�rawb�е��������ݴ��ݸ�temp���飬Ȼ��tempreshape��ͼƬ����
temp = fread(fid, 181 * 217 * 181);
% ���԰��������һ��181*217�У�181�е����飬�������Ĵ��룬�����181��ͼƬ�����ݣ�ÿһ�ж�Ӧһ��ͼ��
% ����ͼƬ�����顣ͼƬ��images������ÿһ�б�ʾһ��ͼƬ��
images = reshape(temp, 181 * 217, 181);  
% ��ȡ�����еĵ�num�У��õ�������reshape��ͼƬԭ����������������181*217��
image = images(:, num);
image = reshape(image, 181, 217);
g = image;
fclose(fid);
end

function init_image(filename,num)
% ����init_image(filename,num)�еĵ�һ������filename������ȡ��rawb�ļ����ļ������ڶ�������num���ǵڶ����š����Ϊԭʼͼ��δ����
%���磺init_image('t1_icbm_normal_1mm_pn0_rf0.rawb',90)�� init_image('phantom_1.0mm_normal_csf.rawb',90)
read=readrawb(filename, num);
% ��ת90�㲢��ʾ����
read=imrotate(read, 90);                                       
imshow(uint8(read));
end