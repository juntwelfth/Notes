# Files

## Read Files

- 파일을 열고 파일의 내용을 읽는 방법

```py
with open('file.txt') as cool_doc:
    cool_contents = cool.dog.read()

print(cool_contents)
# prints contents of file.txt
```

1. `file.txt` 파일을 열고 `cool_doc` 이라는 임시 변수에 저장

2. `cool_doc`에 있는 내용을 읽어 `cool_contents`에 저장

## Read Lines

- 파일의 내용을 한 줄씩 읽어오고자 할 때

```py
with open('file.txt') as cool_doc:
    for line in cool_doc:
        print(line)
```

## Read a Single Line of Files

- 각 줄마다 따로 변수에 저장할 때

`millay_sonnet.txt`

```txt
I shall forget you presently, my dear,
So make the most of this, your little day,
Your little month, your little half a year,
Ere I forget, or die, or move away,
```

```py
with open('millay_sonnet.txt') as sonnet_doc:
    first_line = sonnet_doc.readline()
    # I shall forget you presently, my dear,

    second_line = sonnet_doc.readline()
    # So make the most of this, your little day,

    print(second_line)
    # So make the most of this, your little day,
```

## Writing a File

- `open('txt.txt', 'w')` `'w'` 인자로 쓰기모드로 바꿀 수 있다.
- 이미 똑같은 이름의 파일이 있으면 덮어쓰기를 한다.

    with open('generated_file.txt', 'w') as gen_file:
        gen_file.write("What an incredible file!")

>기본 설정은 `'r'`이다.

## Appending

- `'a'` 인자를 주면 덮어쓰지 않고 이어쓸 수 있다.

```py
with open('generated_file.txt', 'a') as gen_file:
    gen_file.write("What an incredible file!")
```

## Open and Close Files

- 파일 열고 닫기 (권장하지 않음)

```py
fun_cities_file = open('fun_cities.txt', 'a')

fun_cities_file.write("Montréal")

fun_cities_file.close()
```

- `with`은 `context manager`를 호출하는 키워드이다
- `with`은 자동으로 파일을 close 해준다

## Reading a CSV File

- CSV File이란, Comma-Separated Values 파일이다.
- 텍스트로만 이루어져 있는 데이터를 포함한 파일이다.
- csv 라이브러리의 `DictReader object`를 이용해 csv파일을 dictionary로 변환할 수 있다.
- 가끔 csv 파일에는 주소와 같은 형식을 나타낼 때 쉼표를 사용하는데 이땐 다른 문자를 기준으로 문장을 나눌 수 있다
- `csv.DictReader()` 함수를 이용해 `delimiter`를 설정하고 문장을 나눌 수 있다.

`*users.csv*`

```txt
Name,Username,Email
Roger Smith,rsmith,wigginsryan@yahoo.com
Michelle Beck,mlbeck,hcosta@hotmail.com
Ashley Barker,a_bark_x,a_bark_x@turner.com
Lynn Gonzales,goodmanjames,lynniegonz@hotmail.com
Jennifer Chase,chasej,jchase@ramirez.com
Charles Hoover,choover,choover89@yahoo.com
Adrian Evans,adevans,adevans98@yahoo.com
Susan Walter,susan82,swilliams@yahoo.com
Stephanie King,stephanieking,sking@morris-tyler.com
Erika Miller,jessica32,ejmiller79@yahoo.com
```

>CSV 파일은 이렇게 생겼다.

```py
import csv

isbn_list = []

with open('books.csv') as books_csv:
    books_reader = \
        csv.DictReader(books_csv, delimiter='@')

    for row in books_reader:
        isbn_list.append(row['ISBN'])
```

>위 예제처럼 `delimiter`를 설정해 `'@'`를 기준으로 데이터를 나눌 수 있다.

## Writing a CSV File

- `fieldnames` 속성을 이용해 `csv.DictWriter`의 필드를 지정할 수 있다.
- `writeheader()` : 파일의 첫번째 줄을 사용자가 지정한 `field`로 입력한다.
- `writerow()` : 사용자가 지정한 `field`에 맞춰 데이터를 한줄 씩 입력한다.

```py
with open('output.csv', 'w') as output_csv:
    fields = ['name', 'userid', 'is_admin']
    output_writer = \
        csv.DictWriter(output_csv, fieldnames=fields)

    output_writer.writeheader()

    for item in big_list:
        output_writer.writerow(item)
```

1. `fields` 변수를 이용해 `'name'`, `'userid'`, `'is_admin'`과 같이 형식을 지정해줬다.

2. `output_writer.writeheader()` 파일의 첫 줄을 `fields`에 입력된 형식으로 입력한다.

3. `output_writer.writerow(item)` 반복문을 이용해 한줄씩 파일에 입력한다.

## Reading a JSON File

- `json.load()` 함수를 이용해 json 파일을 읽어올 수 있다.

`purchase_14781239.json`

```json
{
  'user': 'ellen_greg',
  'action': 'purchase',
  'item_id': '14781239',
}
```

>json 파일은 위와같이 생겼다.

```py
import json

with open('purchase_14781239.json') as purchase_json:
    purchase_data = json.load(purchase_json)

print(purchase_data['user'])
# Prints 'ellen_greg'
```

>json 파일을 `purchase_data`에 저장하고, `key` `['user']`를 이용해 `value`값을 불러왔다.

## Writing a JSON File

- json.dump() 함수를 이용해 json파일을 쓸 수 있다.

```py
import json

data_payload = [{
        'interesting message': "What is JSON? A web application\'s little pile of secrets.",
        'follow up': 'But enough talk!'
        }]

with open('data.json', 'w') as data_json:
    json.dump(data_payload, data_json)
```

>`data_payload dictionary`를 json 파일 형식으로 변환시켰다.
