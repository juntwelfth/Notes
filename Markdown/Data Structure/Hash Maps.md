# Hash Maps: Conceptual

## Tables

데이터 구조의 주요기능은 사람들이 해당 데이터를 사용하는 방식과 유사한 방식으로 데이터를 표현할 수 있도록하는 것이다. 때때로 해당 데이터의 주요기능은 list와 같이 순서가 지정되게하여 데이터구조를 linked list와 같이 쉽게 반복할 수 있게하는 것이다. 다른 경우엔 데이터 내에서 상호 관계를 지정하는것이 유용하다.

테이블 형식의 데이터는 row 요소간의 관계가 존재한다. 각 column은 row의 다른 기능들을 보여준다.

State|State Flower
-|-
Alabama|Camellia
Hawaii|Hibiscus
Mississippi|Magnolia
New York|Rose
West Virginia|Rhododendron

왼쪽에 있는 각각의 `State`는 오른쪽에 존재하는 `State Flower`에 대응한다. 예를들어 "New York"은 "Rose"와 짝이맞는다. 두개의 column만 존재하는 이와같은 테이블 형식은 "map"이라고 불리우는 특별한 관계를 나타낸다. 현재 이 테이블은 `State`와 `State Flower`를 나타내지만 많은 다른 관계를 맵으로 모델링 할 수 있다.

![table](https://s3.amazonaws.com/codecademy-content/courses/hash-maps-concepts/hashmaps1.png)

## Maps

*Map*이 된다는 것은 두가지 정보를 매칭시키는 것을 의미한다.

Musician|State of Birth
-|-
Miles Davis|Illinois
John Coltrane|North Carolina
Duke Ellington|Ohio
Dizzy Gillespie|South Carolina
Thelonious Monk|North Carolina

위의 테이블에서 재즈 뮤지션을 그들이 태어난 고향과 매칭시켰다. Map에 대해 이야기 할 때 input(뮤지션)을 맵의 keys라고 얘기를 하고 output(고향)을 value라고 얘기를 한다.

Map이 되기 위해 사용되는 모든 key는 단일값의 key만 될 수 있다. 위 예제에선 모든 음악가가 고향이 하나밖에 없으므로 가능하다. 모든 key에 대해 value가 필요한것은 아니며 주어진 key에 대해 value값이 두개 이상일 수는 없다.

만약 위 테이블을 다른 방식으로 보았을 때, 예를들면 states를 key로, 뮤지션의 고향을 value로 설정한다면 map이 성립되지 않는다. 위 예에서 "North Carolina"를 보고 해당 주의 뮤지션이 누구인지 얻으려고하면 매우 어려울 것이다. 왜냐하면 "John Coltrane", "Thelonious Monk" 둘 다 그 곳 출신이기 때문이다.

그래도 여전히 테이블과의 관계는 설명할 수 있지만 map이 아니므로 hash map을 사용하여 그러한 관계를 저장할 수 없다.

![map](https://s3.amazonaws.com/codecademy-content/courses/hash-maps-concepts/hashmaps2.png)

## Hash Map Methodology

![hash map](https://s3.amazonaws.com/codecademy-content/courses/hash-maps-concepts/hashmaps3.png)

두 데이터 사이의 map의 경우 데이터의 정확한 *sequence*(순서)는 그다지 중요하지 않다. Input이 주어졌을 때 ouput을 정확하게 제공해주는 것이 중요하다. 이러한 데이터 구조를 개발하는 것은 까다롭다. 왜냐하면 컴퓨터는 관계보다 value값에 더 관심이 있기 때문이다. 컴퓨터는 위 그림에 나와있는 친구들의 별자리는 중요하게 생각하지 않는다.

