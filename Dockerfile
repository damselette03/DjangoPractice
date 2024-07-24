# 使用 Python 官方映像檔作為基礎映像檔
FROM python:3.12

# 設定工作目錄
WORKDIR /dockerapp

# 複製需求文件到工作目錄
COPY requirements.txt .

# 安裝依賴
RUN pip install -r requirements.txt

# 複製專案文件到工作目錄
COPY . .

# 設置環境變量
ENV DJANGO_SETTINGS_MODULE=MyProject.settings
ENV PYTHONUNBUFFERED=1

# 暴露應用程式的運行端口
EXPOSE 8000

# 運行遷移命令並啟動 Django 開發伺服器
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
