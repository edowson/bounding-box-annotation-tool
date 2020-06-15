import glob, os

# ============================== Config ========================================

DATA_PATH             = 'data/obj/'      # Directory where the data will reside, relative to 'darknet.exe'
VALIDATION_PERCENTAGE = 30               # Validation Image Percentage
IMAGE_FORMAT          = 'jpg'            # Image Format of your data [jpg / png / jpeg]

# ============================== Config ========================================


def process():
	# Create and/or truncate train.txt and val.txt
	file_train      = open('train.txt', 'w')
	file_validation = open('val.txt'  , 'w')

	# Populate train.txt and val.txt
	counter = 1
	index_validation = round(100 / VALIDATION_PERCENTAGE)
	filesPresent = False

	for pathAndFilename in glob.iglob(os.path.join(DATA_PATH, str("*." + IMAGE_FORMAT) )):
		title, ext = os.path.splitext(os.path.basename(pathAndFilename))
		filesPresent = True
		if counter == index_validation:
			counter = 1
			file_validation.write(DATA_PATH + title + '.' + IMAGE_FORMAT + "\n")
		else:
			file_train.write(DATA_PATH + title + '.' + IMAGE_FORMAT + "\n")
			counter = counter + 1

	if not filesPresent:
		print("No Files Present in the Directory : ", DATA_PATH)

	return


if __name__ == "__main__":
	process()
