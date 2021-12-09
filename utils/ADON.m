path = 'C:/Users/502/Desktop/1.png';
%path2 = 'C:/Users/502/Desktop/2.png';
img = imread(path);
%img2 = imread(path2);
img = img(:,:,1);
%img2 = img2(:,:,1);
[h,w] = size(img);

gray = 0;
white = 0;
for i = 1:h
    for j = 1:w
        if img(i,j)>100&&img(i,j)<200
            %disp(img(i,j));
            gray = gray+1;
        end
        if img(i,j)>200
            %disp(img(i,j));
            white = white+1;  
        end
    end
end
bili = gray/(gray+white);


        
                