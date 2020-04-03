# CSS-File-Generator

### Usuage

```bash
./cssgen.py <input html file> <css file output>
```

### Example I/O

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>title</title>
    <meta name="author" content="name">
    <meta name="description" content="description here">
    <meta name="keywords" content="keywords,here">
  </head>
  <body>
    <div class="helloworld">
    </div>

    <a class="link">
    </a>

    <p class='test-single-quote'>
    </p>

    <span class="test-twice">
    </span>
    <span class="test-twice">
    </span>

    <div class="nested">
        <span class="nested-component"></span>
    </div>
  </body>
</html>
```

> The classes here are all different to test how well the script is working. Some classes have single quotes, hypens 
> in the middle, nested classes

#### Output CSS

```css
.helloworld { }

.link { }

.nested-component { }

.nested { }

.test-single-quote { }

.test-twice { }
```
