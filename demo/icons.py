# This is a program that makes a simple JSON list of fontawesome
# icons and produces json. re-run it when you upgrade the icon set
import json
hand = open("font-awesome-4.3.0/less/icons.less")
icons = list()
prefix = '.@{fa-css-prefix}-'
for line in hand:
	if ( not line.startswith(prefix) ) : continue
	endpos = line.find(':', len(prefix))
	if ( endpos < 1 ) : continue
	name = line[len(prefix):endpos]
	icons.append("fa-"+name)

icons.sort()
f = open('icons.json', 'w')
f.write(json.dumps(icons, sort_keys=True, indent=4))
print('Output is on icons.json')
