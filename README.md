## Synopsis

A website for submitting and reviewing applications to HackRice 2017. More info at hack.rice.edu.

## Instructions

1. Checkout the repository
  ```
  git clone https://github.com/hack-rice/hackrice_webapp.git
  cd hackrice_webapp
  ```
  
2. Install flask
  ```
  pip install flask
  ```

3. Set the `FLASK_APP` environment variable by adding the following to your `.bashrc` or `.zshrc` or whatever you're using
  ``` 
  export FLASK_APP=/path/to/hackrice_webapp/hackrice.py
  ```

4. Run the app from the main project directory
  ```
  flask run
  ```

5. Point your browser to either `http://127.0.0.1:5000/` or `http://localhost:5000/`

## Contributors

[@jarroddunne](http://github.com/jarroddunne)

[@smahesh1](http://github.com/smahesh1)

[@prb2](http://github.com/prb2)

## License

MIT License

Copyright (c) 2016-2017 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
