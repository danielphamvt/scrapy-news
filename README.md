-# scrapy-news
# scrapy-news
## Các bước thực hiện:
1. Tải sourcecode về máy
2. Mở project bằng Pycharm
3. Tạo môi trường ảo bằng cách vào File-->preference (hoặc tạo môi trường ảo bằng terminal https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/).  Activate môi trường ảo.
Bỏ qua bước 3 nếu chạy trên môi trường Anaconda.

4. Cài đặt Scrapy, PyMongo: Mở terminal (Nếu chạy trên môi trường ảo thì môi trường này đã active). Chạy lệnh sau để cài các pakages cần thiết cho project:
```pip install -r requirements.txt```. Nếu sử dụng Anaconda chạy lệnh: ```conda install scrapy``` và ```conda install pymongo```

5. Để lưu dữ liệu dạng json, sử dụng các lệnh
```scrapy crawl vnexpress -o vn_express.json``` hoặc ```scrapy crawl thegioididong -o tgdd.json``` 

6. Để lưu dữ liệu vào Mongodb, thực hiện các bước sau:

- Cài đặt MongoDB từ website: <link>https://www.mongodb.com/try/download/community</link>
- Mở MongoDBcompass và tạo cơ sở dữ liệu có tên: ```news_bot``` và collection ```review```
- Sử dụng các lệnh: ```scrapy crawl vnexpress``` hoặc ```scrapy crawl thegioididong``` để crawl và lưu dữ liệu vào CSDL MongoDB 