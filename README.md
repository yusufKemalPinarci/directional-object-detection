Test veri seti ile istenilen çıktının alınması için atılacak adımlar:

1- PART3 klasörünün içine test klasörü taşınır.
2- main.py dosyası içinde "test_directory" değişkenine test klasörünün yolu yapıştırılır.
3- "python -m venv venv" ile virtual environment oluşturulur ve "venv/Scripts/activate.bat" ile environment çalıştırılır.
4- "pip install ultralytics" komutu ile gerekli paket yüklenir.
5- "python main.py" ile main dosyası çalıştırılır.
6- siniflandir.py dosyasındaki "predict_klasoru" değişkenine modelin tahminleri oluşturduğu klasörün ("runs\obb\predict\labels" gibi) yolu verilir.
7- Daha sonra "python siniflandir.py" ile istenilen formatta her class için text dosyaları ana dizinde oluşturulur.
