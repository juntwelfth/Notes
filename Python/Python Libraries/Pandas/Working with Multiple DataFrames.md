# Working with Multiple DataFrames

## Multiple DataFrames

- 중복되는 column들이 있을 때 큰 부류로 나눌 수 있다.

    ```py
    order_id
    customer_id
    customer_name
    customer_address
    customer_phone_number
    product_id
    product_description
    product_price
    quantity
    timestamp
    ```

- 이러한 정보들이 있을 때 같은 물건을 두번 사거나, 한사람이 여러 물건을 사면 정보들이 중복된다. 따라서 좀 더 큰 범주로 분류를 해야한다.

    ```py
    orders
    order_id
    product_id
    customer_id
    quantity
    timestamp

    products
    product_id
    product_description
    product_price

    customers
    customer_id
    customer_name
    customer_address
    customer_phone_number
    ```

    > 이런식으로 묶어줄 수 있다.

## Inner Merge

- 여러개의 데이터를 보고 매칭시키기 힘들 때
- `pd.merge(DataFrame1, DataFrame2)` 메소드를 사용할 수 있다.
- 두개이상의 데이터를 체인할 땐 `DataFrame1.merge(DataFrame2).merge(DataFrame3)` 이런식으로 할 수 있다.

```py
new_df = pd.merge(orders, customers)

new_df = orders.merge(customers).merge(products)
```

> 자동으로 두개 이상의 데이터프레임을 merge해준다.

## Merge on Specific Columns I

- 두개의 데이터프레임이 같은 이름의 column을 가지고 있을 때 merge를 하면 데이터가 꼬여버린다.
- 이를 피하기 위한 방법으로 첫번째는 `rename`을 사용하는 것이다.

```py
pd.merge(
    orders,
    customers.rename(columns={'id': 'customer_id'}))
```

```py
import pandas as pd

orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')


orders_products = pd.merge(orders,
products.rename(columns={'id': 'product_id'}))
```

## Merge on Specific Columns II

- `rename`을 쓰고 싶지 않으면 `left_on`과 `right_on`을 사용할 수도 있다.
- `suffixes`를 쓰지 않으면 `id_x`, `id_y`라고 나온다.

아래 코드는 `orders`의 `customer_id`와 `customers`의 `id`를 일치시켜주고, merge를 시켜준다.

```py
pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id',
suffixes=['_orders', '_products'])
```

- 위 product_id와 아래 id를 매칭시켜준다.

- merge하려는데 서로 일치하지 않으면 건너뛴다.

## Outer Merge

- Inner Merge는 일치하지 않는 데이터는 merge를 하지않는다. 일치하지 않는 데이터들까지 살리고 싶을 땐 Outer Merge를 사용해야 한다.

- 서로 조금씩 다른 데이터프레임이 있을 때

`company_a`

```txt
name             email
Sally Sparrow    sally.sparrow@gmail.com
Peter Grant      pgrant@yahoo.com
Leslie May       leslie_may@gmail.com
```

`company_b`

```txt
name             phone
Peter Grant      212-345-6789
Leslie May       626-987-6543
Aaron Burr       303-456-7891
```

- 두 데이터를 merge하고싶은데 데이터를 잃고싶지 않을 때 how를 사용해주면 되고, 빈공간은 None 혹은 nan으로 채워진다.

```txt
name             email                        phone
Sally Sparrow    sally.sparrow@gmail.com      nan
Peter Grant      pgrant@yahoo.com             212-345-6789
Leslie May       leslie_may@gmail.com         626-987-6543
Aaron Burr       nan                          303-456-7891
```

## Left and Right Merge

- 핸드폰번호가 없는 고객이 누구인지를 보고싶을 때 Left Merge를 해줄 수 있다.
- Left Merge는 첫번째 데이터를 전부 포함하고 첫번째 데이터와 일치하는 두번째 데이터를 merge해주는 방법이다.
- Left Merge는 인자의 순서가 중요하다.

```py
pd.merge(company_a, company_b, how='left')
```

아래와 같이 나온다.

```txt
name            email                       phone
Sally Sparrow   sally.sparrow@gmail.com     None
Peter Grant     pgrant@yahoo.com            212-345-6789
Leslie May      leslie_may@gmail.com        626-987-6543
```

- Left Merge의 정확히 반대되는 Right Merge도 사용법이 동일하다.

```py
pd.merge(company_a, company_b, how='left')
```

아래와 같이 나온다.

```txt
name            email                      phone
Peter Grant     pgrant@yahoo.com           212-345-6789
Leslie May      leslie_may@gmail.com       626-987-6543
Aaron Burr      None                       303-456-7891
```

## Concatenate DataFrames

- 때때로 데이터셋은 여러 테이블로 나눠져있다. 예를들면 데이터들은 보통 여러개의 CSV파일들로 나눠져있다. (더 작은 용량을 위해)
- `pd.concat([df1, df2, df2, ...])` 메소드를 이용해 합쳐줄 수 있다.
- 이 메소드는 모든 column들이 동일할 때에만 적용된다.

`df1`

```txt
name                email
Katja Obinger       k.obinger@gmail.com
Alison Hendrix      alisonH@yahoo.com
Cosima Niehaus      cosi.niehaus@gmail.com
Rachel Duncan       rachelduncan@hotmail.com
```

`df2`

```txt
name                email
Jean Gray           jgray@netscape.net
Scott Summers       ssummers@gmail.com
Kitty Pryde         kitkat@gmail.com
Charles Xavier      cxavier@hotmail.com
```

위 두 데이터를 합치고 싶으면

```py
pd.concat([df1, df2])
```

```txt
name                email
Katja Obinger       k.obinger@gmail.com
Alison Hendrix      alisonH@yahoo.com
Cosima Niehaus      cosi.niehaus@gmail.com
Rachel Duncan       rachelduncan@hotmail.com
Jean Gray           jgray@netscape.net
Scott Summers       ssummers@gmail.com
Kitty Pryde         kitkat@gmail.com
Charles Xavier      cxavier@hotmail.com
```
