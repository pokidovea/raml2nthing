# raml2nthing
A tool for converting RAML to anything

It can convert a RAML-file to any other format. You should only prepare a corresponding template in Jinja2 format or use predefined one.

## Usage
```
raml2nthing -i path/to/source.raml -t path/to/my_html_template.j2 -o path/to/destination.html
```
or
```
raml2nthing -i path/to/source.raml -t markdown -o path/to/destination.md
```

## Predefined templates
Now it only supports markdown format
