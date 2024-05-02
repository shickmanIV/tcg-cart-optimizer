# tcg-cart-optimizer
A site for buying and selling trading cards. Currently only magic the gathering is functional.

Team Members:
- Kenan Anderson
- Kyle Grentz
- Samuel Hickman
- Shiv Malhotra
- Ethan Knigge
- Austin Tarrach

Usage Instrucitons (in terminal)
  Setup:
  1.  From within the tcg-cart-optimizer directory, setup a virtual environment:   $  python3 -m venv .venv
  2.  Activate the virtual environment:  $  . .venv/bin/activate
  4.  Install dependencies:  $  pip install flask
                             $  pip install flask_cors
                             $  pip install mtgsdk
                             $  pip install mysql 
  Running the Program:
  1.  Activate the virtual environment.   $  . .venv/bin/activate
  2.  Enter ShopTCG directory:  $  cd ShopTCG
  3.  Run main.py  $  python main.py
  4.  Visit the link in the console to view the site. Example: http://127.0.0.1:5000

  - Press CTRL + C to stop hosting site
  - type 'exit' to quit virtural environment
