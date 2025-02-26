# SharpCap小行星标记数据的转换工具
# Asteroid Data Converter for SharpCap

该工具用于将 SkyChart 的小行星数据转换为 SharpCap 可识别的自定义星表文件（asteroid_for_sharpcap.csv），以便在 SharpCap 的深空影像标记中显示。

1）准备阶段：
在Windows电脑安装Python后，安装pandas模块(pip install pandas) 访问文件夹C:\Users\用户名\AppData\Roaming\SharpCap\AnnotationCatalogs，如果没有则创建文件夹，然后将以下文件复制进来： 
    - asteroids.txt，SkyChart保存"观测列表"，更新RA和DEC 
    - asteroid5000_convert.py，转换工具 
    - asteroid_for_sharpcap.csv，SharpCap能识别的自定义星表，每次运行py后会覆盖此文件 
 
2）定期更新SkyChart小行星数据更新 
    - 从https://minorplanetcenter.net/iau/MPCORB.html下载MPCORB.DAT (uncompressed) 
    - 进入设置-太阳系，Load MPC file，默认编号靠前的5000颗 
    - 从Or use a local files选择下载的DAT文件，等待处理和更新 
 
3）打开SkyChart   
    - 连好赤道仪 
    - 进入设置-星图和坐标，选择Equatorial coordinates、North和Astrometric J2000 
    - 进入观测列表，使用load键，导入asteroids.txt 
    - 点击Update coordinates，更新坐标 
    - 点击保存，txt文件被更新 

4）运行asteroid5000_convert.py 
    - 生成或覆盖asteroid_for_sharpcap.csv，里面是SharpCap可识别的结构

5）运行SharpCap（需要Pro版本，安装许可证序列号） 
    - 相机，打开相机，做好赤道仪解析 
    - 工具，打开深空影像标记 
    - 在Display中点击”Clear and Reload Custom Catalogs“，此时界面视图内坐标位置内会显示标记