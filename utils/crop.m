%path = 'C:\Users\502\Desktop\ATLAS RESULT\Nestfuse\CM\257.png';
%path = 'C:\Users\502\Desktop\ATLAS RESULT\Nestfuse\SPECT_\004.png';

path = ['C:\Users\502\Desktop\图像融合\PAPER\DARTS对比FDARTS用图片\DARTS057.png'];
save_path = ['C:\Users\502\Desktop\图像融合\PAPER\DARTS对比FDARTS用图片\DARTS057_.png'];
img  = imread(path);
if length(size(img)) ==3
    img1 = img(:,:,:);
else
    img1 = img(128:256,:);
end
imwrite(img1,save_path);
