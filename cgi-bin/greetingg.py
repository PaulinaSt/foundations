#!/usr/bin/env python3
print('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello Python!</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
    
    <!-- import the webpage's javascript file -->
    <script src="/script.js" defer></script>
  </head>  
  <body>
    <h1>Hi!</h1>
    
    <p>
      <form action="" method="get" class="form-example">
      <div class="form-example">
      <label for="name">Enter your name: </label>
      <input type="text" name="name" id="name" required>
      </div>
      </form>
    </p>
  </body>
</html>
''')