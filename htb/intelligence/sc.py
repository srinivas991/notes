
# http://10.10.10.248/documents/2020-01-01-upload.pdf

for j in range(1,13):
	for k in range(1,32):
		ext = "2020-{}-{}-upload.pdf".format((j if j > 9 else "0{}".format(j)), (k if k > 9 else "0{}".format(k)))
		print(ext)