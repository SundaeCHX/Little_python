#Picture_cloud

依赖库 PIL numpy numexpr 等。

图片云拼接层叠程序，将目标图片拷贝至Picture_cloud/目录下，示例中为target.png。

新建photos/目录，将图片群拷贝至Picture_cloud/photos/目录下。

设置picture.py参数，图片num、size、alpha等。

运行 python picture.py 即可生成六种目标图片。

备注：图片num数量与photos/目录下图片数量相关，图片越多效果越好，比如有400张图片，可设置 W_num = 20 H_num = 20


原始图片

![image](https://github.com/SundaeCHX/Little_python/blob/master/Picture_cloud/target.png)

转换后图片

![image](https://github.com/SundaeCHX/Little_python/blob/master/Picture_cloud/imgcloud.jpg)
