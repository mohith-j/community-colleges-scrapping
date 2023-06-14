import PyPDF2
import re

def extract(pdfs):
	with open(pdfs, "rb") as pdf:
		reader = PyPDF2.PdfReader(pdf, strict=False)
		text = []

		for page in reader.pages:
			content = page.extract_text()
			text.append(content)

		return text

extractedText = extract('completed colleges/laniertech.pdf')


pattern = r"[A-Z]{4} \d{4} [A-Z].+ \("
matches = []

for text in extractedText:
	match = re.findall(pattern, text)
	if match:
		matches.extend(match)


li = []
final = []
for m in matches:
	if m[0:9] not in li:
		li.append(m[0:9])
		final.append(m)
final = sorted(final)
currmjr = ""
for i in final:
	if currmjr != i[0:4]:
		print('---------------------------------')
		print(i[0:4])
	currmjr = i[0:4]
	if i[0:9] == "EMSP 2510":
		print("EMSP 2510 Clinical Applications for the Paramedic - I")
		continue
	if i[0:9] == "EMSP 2520":
		print("EMSP 2510 Clinical Applications for the Paramedic - II")
		continue
	if i[0:9] == "EMSP 2530":
		print("EMSP 2510 Clinical Applications for the Paramedic - III")
		continue
	i = i.strip("(")
	print(i)