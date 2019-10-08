from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"plains", "limit":99, "format":"jpg","output_directory":"plains2"}
paths=response.download(arguments)
