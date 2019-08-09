from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

keywords = [
	"speed limit 10",
	"speed limit 15",
	"speed limit 20",
	# "speed limit 25",
	"speed limit 30",
	"speed limit 35",
	"speed limit 40",
	"speed limit 45",
	"speed limit 50",
	"speed limit 55",
	"speed limit 60",
	"speed limit 65",
	"speed limit 70",
	"speed limit 75",
	"speed limit 80",
	"stop sign",
	"yield sign",
	"do not enter sign"
]

for sign in keywords:
	arguments = {"keywords": sign, "limit": 100, "print_urls": False, "image_directory": sign,
				 "output_directory": "/home/brian/Pictures/RSA machine learning/RSA signs training dataset",
				 }

	paths = response.download(arguments)
