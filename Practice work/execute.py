print("Photo Gallery")
gallery={
    1:"beach.png",
    2:"birthday.png",
    3:"selfie.png",
    4:"party.jpg",
    5:"mountain.jpg"
}
for i in gallery:
    print(f'{i}.{gallery[i]}')
selected_photos =set(map(int,input("select photos to share:").split()))
print("Sharing the following photos:")
for i in selected_photos:
    if i<=i<=8:
        print(gallery[i])
    else:
        print(f"Unable to fetch the image for this id={i}")