from string import Template
greeting_template = Template('Hello World, my name is $name.')
greeting = greeting_template.substitute(name='attacker')