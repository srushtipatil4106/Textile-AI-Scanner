import cv2


img = cv2.imread("sample.jpg")

if img is not None:
    print("\n=============================================")
    print("[SUCCESS] OpenCV successfully loaded the image matrix!")
    print(f"Matrix Grid Dimensions (H x W x C): {img.shape}")
    print("=============================================\n")
else:
    print("\n[ERROR] Could not find or read 'sample.jpg'.")
    print("Make sure it's sitting right inside the 'Textile_AI' folder!")
