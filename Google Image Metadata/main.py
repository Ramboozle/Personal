from PIL import Image, ExifTags
img = Image.open("/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Python/Personal/Google Image Metadata/Tester Photos/2.jpg")
exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
print(exif)