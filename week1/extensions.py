def main():
	filename = input('File name: ').rstrip().lower()
	print(get_media_type(filename))


def get_media_type(filename):
	default_media_type = 'application/octet-stream'
	ext_index = filename.rfind('.')
	if ext_index == -1:
		return default_media_type
	ext = filename[ext_index:]
	match ext:
		case '.gif':
			return 'image/gif'
		case '.jpg' | '.jpeg':
			return 'image/jpeg'
		case '.png':
			return 'image/png'
		case '.pdf':
			return 'application/pdf'
		case '.txt':
			return 'text/plain'
		case '.zip':
			return 'application/zip'
		case _:
			return default_media_type


main()
