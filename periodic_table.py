def parse_line(string):
	parse_list = []
	parse_list = string.split(",")
	parse_list = list(parse_list)
	parse_list = [s.lstrip(" ").replace("\n", "") for s in parse_list]
	name = (parse_list[0].split())[0]
	position = ((parse_list[0].split())[2].split(":"))[1]
	number = (parse_list[1].split(":"))[1]
	small = (parse_list[2].split(": "))[1]
	molar = (parse_list[3].split(":"))[1]
	electron = (parse_list[4].split(":"))[1]
	return name, position, number, small, molar, electron

flag = 1
content = ""
test_data = open("preiodic_table.txt", "r")
lines = test_data.readlines()
position = 0
content += "<tr>"
content += "<td>"
content += "</td>"
for i in range(1, 19):
	content += "<td>"
	content += f"<p>{i}</p>"
	content += "</td>"
content += "</tr>"
for line in lines:
	last_position = position
	name, position, number, small, molar, electron = parse_line(line)
	if position == "0":
		content += "<tr>"
		content += "<td>"
		content += f"<p>{flag}</p>"
		content += "</td>"
		flag += 1
	for _ in range(int(position) - int(last_position) - 1):
		content += "<td>"
		content += "</td>"
	content += "<td>"
	content += "<table style='width: 100%;font-size: 3px;'>"
	content += "<tr>"
	if number in ["1", "2", "7", "8", "9", "10", "16", "17", "18", "35", "36", "53", "54", "86"]:
		content += "<td style='border: 1px solid black; background-color: #ffa500'>"
	elif number in ["5", "6", "14", "15", "32", "33", "34", "51", "52", "83", "84", "85"]:
		content += "<td style='border: 1px solid black; background-color: #ffff00'>"
	elif int(number) <= 88:
		content += "<td style='border: 1px solid black; background-color: #7fffd4'>"
	else:
		content += "<td style='border: 1px solid black;'>"
	content += f"<h4 style='text-align: center'> {name}</h4>"
	content += "<ul style='list-style: none;text-align: left;padding-left: 8px;'>"
	content += f"<li><i class='fas fa-wrench'></i> No {number}</li>"
	content += f"<li><i class='fas fa-atom'></i> {small}</li>"
	content += f"<li><i class='fas fa-balance-scale'></i> {molar}</li>"
	content += f"<li><i class='fab fa-phabricator'></i> {electron}</li>"
	content += "</ul>"
	content += "</td>"
	content += "</tr>"
	content += "</table>"
	content += "</td>"
	if position == "17":
		content += "</tr>"
test_data.close()

html = f"""
<!DOCTYPE html>
<html lang="ja">
	<head>
		<meta charset="utf-8">
		<link href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" rel="stylesheet">
	</head>
	<body style="width: 100%; height: 100%; text-align: center">
		<h1><i class='fas fa-atom'></i> The Periodic Table</h1>
		<table>
			{content}
		</table>
	</body>
</html>
"""

with open("periodic_table.html", "wb") as f:
	f.write(html.encode('utf-8'))
