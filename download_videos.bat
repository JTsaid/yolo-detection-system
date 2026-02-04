@echo off
chcp 65001 >nul
echo ========================================
echo   下载演示视频
echo ========================================
echo.

if not exist demo_videos mkdir demo_videos

echo [1/3] 下载交通场景视频...
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/intel-iot-devkit/sample-videos/raw/master/car-detection.mp4' -OutFile 'demo_videos/traffic.mp4'"
if %errorlevel% equ 0 (
    echo ✓ 交通场景视频下载成功
) else (
    echo ✗ 交通场景视频下载失败
)
echo.

echo [2/3] 下载人员检测视频...
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/intel-iot-devkit/sample-videos/raw/master/people-detection.mp4' -OutFile 'demo_videos/people.mp4'"
if %errorlevel% equ 0 (
    echo ✓ 人员检测视频下载成功
) else (
    echo ✗ 人员检测视频下载失败
)
echo.

echo [3/3] 下载监控场景视频...
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/intel-iot-devkit/sample-videos/raw/master/bolt-detection.mp4' -OutFile 'demo_videos/monitoring.mp4'"
if %errorlevel% equ 0 (
    echo ✓ 监控场景视频下载成功
) else (
    echo ✗ 监控场景视频下载失败
)
echo.

echo ========================================
echo   下载完成！
echo ========================================
echo.
echo 视频保存在 demo_videos 目录
echo.
pause
