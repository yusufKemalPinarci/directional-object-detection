import os

predict_klasoru = "runs\obb\predict\labels"
vehicle_txt = "vehicle.txt"  # Çalışma dizininde oluşturulacak veya üzerine yazılacak
plane_txt = "plane.txt" 
bridge_txt = "bridge.txt" 
harbor_txt = "harbor.txt" 
ship_txt = "ship.txt" 
# predict9 klasöründeki txt dosyalarını listeleme
for dosya in os.listdir(predict_klasoru):
    if dosya.endswith(".txt"):
        dosya_yolu = os.path.join(predict_klasoru, dosya)
        with open(dosya_yolu, 'r') as dosya_oku:
            for satir in dosya_oku:
                sütunlar = satir.strip().split()
                if sütunlar[0] == "0":
                    temp = sütunlar[-1]
                    sütunlar.pop(0)
                    sütunlar.insert(0, temp)
                    sütunlar.pop()

                    # vehicle.txt dosyasına ekleme yapma
                    with open(vehicle_txt, 'a') as vehicle_dosya:
                        vehicle_dosya.write(f"{dosya[:-4]} {' '.join(sütunlar)}\n")
                    break  # Dosyanın kontrolü tamamlandıktan sonra diğer dosyaya geçer
                elif sütunlar[0] == "1":
                    temp = sütunlar[-1]
                    sütunlar.pop(0)
                    sütunlar.insert(0, temp)
                    sütunlar.pop()

                    # vehicle.txt dosyasına ekleme yapma
                    with open(plane_txt, 'a') as plane_dosya:
                        plane_dosya.write(f"{dosya} {' '.join(sütunlar)}\n")
                    break  # Dosyanın kontrolü tamamlandıktan sonra diğer dosyaya geçer
                elif sütunlar[0] == "2":
                    temp = sütunlar[-1]
                    sütunlar.pop(0)
                    sütunlar.insert(0, temp)
                    sütunlar.pop()

                    # vehicle.txt dosyasına ekleme yapma
                    with open(bridge_txt, 'a') as bridge_dosya:
                        bridge_dosya.write(f"{dosya} {' '.join(sütunlar)}\n")
                    break  # Dosyanın kontrolü tamamlandıktan sonra diğer dosyaya geçer
                elif sütunlar[0] == "3":
                    temp = sütunlar[-1]
                    sütunlar.pop(0)
                    sütunlar.insert(0, temp)
                    sütunlar.pop()

                    # vehicle.txt dosyasına ekleme yapma
                    with open(harbor_txt, 'a') as harbor_dosya:
                        harbor_dosya.write(f"{dosya} {' '.join(sütunlar)}\n")
                    break  # Dosyanın kontrolü tamamlandıktan sonra diğer dosyaya geçer
                elif sütunlar[0] == "4":
                    temp = sütunlar[-1]
                    sütunlar.pop(0)
                    sütunlar.insert(0, temp)
                    sütunlar.pop()

                    # vehicle.txt dosyasına ekleme yapma
                    with open(ship_txt, 'a') as ship_dosya:
                        ship_dosya.write(f"{dosya} {' '.join(sütunlar)}\n")
                    break  # Dosyanın kontrolü tamamlandıktan sonra diğer dosyaya geçer

