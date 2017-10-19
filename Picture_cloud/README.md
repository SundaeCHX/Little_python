# Picture_cloud

依赖库 PIL numpy numexpr 等。

图片云拼接层叠程序，将目标图片拷贝至 Picture_cloud/ 目录下，示例中为 target.png 。

新建 photos/ 目录，将图片群拷贝至 Picture_cloud/photos/ 目录下。

设置 picture.py 参数，图片num、size、alpha等。

运行 python picture.py 即可生成六种转换后的图片。

备注：图片num数量与 photos/ 目录下图片数量相关，图片越多效果越好。

     比如有400张图片，可设置 W_num = 20 H_num = 20



Dependent library PIL numpy numexpr and so on.

Image cloud stitching cascade program, copy the target image to Picture_cloud / directory, in the example target.png.

Create a new photo / directory and copy the picture group to the Picture_cloud / photos / directory.

Set picture.py parameter, image num, size, alpha and so on.

Run python picture.py to generate six converted images.

Note: The number of pictures num and photos / catalog number of pictures related to the picture the more the better results.

    For example, there are 400 pictures, you can set W_num = 20 H_num = 20
    
    

原始图片  Original Image

![image](https://github.com/SundaeCHX/Little_python/blob/master/Picture_cloud/target.png)

转换图片  Convert Image

![image](https://github.com/SundaeCHX/Little_python/blob/master/Picture_cloud/imgcloud.jpg)
