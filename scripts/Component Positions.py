numbers = ["zero.dnom",
"one.dnom",
"two.dnom",
"three.dnom",
"four.dnom",
"five.dnom",
"six.dnom",
"seven.dnom",
"eight.dnom",
"nine.dnom",
]

for l in Glyphs.font.selectedLayers:
	for i in range(len(l.components)):
		c = l.components[i]
		c.automaticAlignment = False
		if i == 0:
			c.position = (-128, 0)
		elif i == 1:
			if c.componentName in numbers:
				c.position = (288, 512)
			else:
				c.position = (128, 0)
		elif i == 2:
			if c.componentName in numbers:
				c.position = (32, 128)
			else:
				c.position = (-128, -384)
		elif i == 3:
			if c.componentName in numbers:
				c.position = (288, 128)
			else:
				c.position = (128, -384)
	l.width = 448
