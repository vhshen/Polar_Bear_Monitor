from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"snowman", "limit":80, "format":"jpg","output_directory":"snowimgs"}
paths=response.download(arguments)
