# CS103a_PA02

<h2>In this PA, we made a financial manager that uses a database and SQL queries.

Our script output is below:</h2>

Script started on 2022-03-24 19:24:30-04:00 [TERM="xterm-256color" TTY="/dev/pts/1" COLUMNS="101" LINES="26"]
[?2004h]0;matthew@penguin: ~/GitHub/CS103a_PA02[01;32mmatthew@penguin[00m:[01;34m~/GitHub/CS103a_PA02[00m$ exitpython tracker.py
[?2004l

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
12. summarize transactions by most expensive
13. clears the transactions table


> 5
Add A Transaction To The Database!
Please Input The Cost Of The Transaction: 6.00
Please Input The Name of Category: Peope le
Please Input The Date (yyyymmdd) This Item Was Bought: 2022 00124
Please Input The Description of the Item: test
('We Successfully Add Transction', 4, 'To The Database')
> 4


item #     amount     category   date       description                   
--------------------------------------------------
1          5.0        People     20221324   Matthew                       
2          6.0        People     20210223   Pedro                         
3          2.0        People     20220321   Jason                         
4          6.0        People     20200124   test                          
> 6
Please Input The Number Of The Transaction You're Deleting: 4
We Have Sucessfully Deleted The Transaction From The Database
> 4


item #     amount     category   date       description                   
--------------------------------------------------
1          5.0        People     20221324   Matthew                       
2          6.0        People     20210223   Pedro                         
3          2.0        People     20220321   Jason                         
> 7


item #     amount     category   date       description                   
--------------------------------------------------
2          6.0        People     20210223   Pedro                         
3          2.0        People     20220321   Jason                         
1          5.0        People     20221324   Matthew                       
> 8


item #     amount     category   date       description                   
--------------------------------------------------
2          6.0        People     20210223   Pedro                         
3          2.0        People     20220321   Jason                         
1          5.0        People     20221324   Matthew                       
> 9


item #     amount     category   date       description                   
--------------------------------------------------
1          5.0        People     20221324   Matthew                       
2          6.0        People     20210223   Pedro                         
3          2.0        People     20220321   Jason                         
> 10


item #     amount     category   date       description                   
--------------------------------------------------
1          5.0        People     20221324   Matthew                       
2          6.0        People     20210223   Pedro                         
3          2.0        People     20220321   Jason                         
> 11

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
12. summarize transactions by most expensive
13. clears the transactions table

> 12


item #     amount     category   date       description                   
--------------------------------------------------
2          6.0        People     20210223   Pedro                         
1          5.0        People     20221324   Matthew                       
3          2.0        People     20220321   Jason                         
> 13
All transactions were deleted
> 0
bye
[?2004h]0;matthew@penguin: ~/GitHub/CS103a_PA02[01;32mmatthew@penguin[00m:[01;34m~/GitHub/CS103a_PA02pytest
[?2004l
[1m======================================== test session starts ========================================[0m
platform linux -- Python 3.9.2, pytest-7.1.0, pluggy-1.0.0
rootdir: /home/matthew/GitHub/CS103a_PA02, configfile: pytest.ini
plugins: anyio-3.5.0
[1mcollecting ... [0m[1m
collected 10 items                                                                                  [0m

test_category.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                                         [ 40%][0m
test_transactions.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                                   [100%][0m

[32m======================================== [32m[1m10 passed[0m[32m in 5.76s[0m[32m =========================================[0m
pylint tracker.py 
[?2004l
************* Module tracker
tracker.py:29:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:117:43: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:125:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
tracker.py:126:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
tracker.py:130:0: W0311: Bad indentation. Found 9 spaces, expected 8 (bad-indentation)
tracker.py:133:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:182:0: C0305: Trailing newlines (trailing-newlines)
tracker.py:45:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:63:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
tracker.py:62:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:62:0: R0912: Too many branches (15/12) (too-many-branches)
tracker.py:62:0: R0915: Too many statements (54/50) (too-many-statements)
tracker.py:139:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:156:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:167:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:169:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:170:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:172:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:173:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:35:0: W0611: Unused import sys (unused-import)
tracker.py:35:0: C0411: standard import "import sys" should be placed before "from category import Category" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 7.61/10 (previous run: 7.61/10, +0.00)

[?2004h]0;matthew@penguin: ~/GitHub/CS103a_PA02[01;32mmatthew@penguin[00m:[01;34m~/GitHub/CS103a_PA02[00m$ pylint transactions.py 
[?2004l
************* Module transactions
transactions.py:17:0: C0301: Line too long (111/100) (line-too-long)
transactions.py:19:0: C0301: Line too long (111/100) (line-too-long)
transactions.py:58:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:64:0: C0301: Line too long (187/100) (line-too-long)
transactions.py:77:0: C0301: Line too long (130/100) (line-too-long)
transactions.py:109:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:118:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:123:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:133:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:136:19: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:143:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:148:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:153:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:162:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:16:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
transactions.py:65:8: W0622: Redefining built-in 'id' (redefined-builtin)
transactions.py:65:8: C0103: Variable name "id" doesn't conform to snake_case naming style (invalid-name)
transactions.py:110:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:119:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:129:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:139:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:149:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:158:4: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.89/10 (previous run: 7.89/10, +0.00)

[?2004h]0;matthew@penguin: ~/GitHub/CS103a_PA02[01;32mmatthew@penguin[00m:[01;34m~/GitHub/CS103a_PA02[00m$ wx[K[Kexit
[?2004l
exit

Script done on 2022-03-24 19:29:56-04:00 [COMMAND_EXIT_CODE="0"]
