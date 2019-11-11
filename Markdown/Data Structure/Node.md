# Node란

Node란 많은 컴퓨터과학 데이터구조의 기본 구성요소이다. Linked Lists, Stacks, Queues, Trees 등등 데이터 구조들이 Node를 기반으로 하고있다.

각각의 노드는 데이터를 포함하고 있고, 다른 노드와 연결되어있다. 각각의 데이터 구조는 원하는 구조를 만들기 위해 추가적인 제약이나 행동을 추가한다.

![node](https://s3.amazonaws.com/codecademy-content/courses/learn-nodes-general/diagram_1.svg)

위 그림에서 `node_`는 데이터(숫자 `5`)를 포함하고 있고 또 다른 노드 `node_b`에 연결되어있다.

## Nodes Detail

노드에 포함된 데이터는 사용중인 언어에 따라 형태가 달라질 수 있다. 위 그림에선 정수 (숫자 `5`)였지만 문자열(`"five"`)이 될 수도, 실수(`5.1`), 배열(`[5, 3, 4]`), 심지어 없음(`null`)이 될 수도 있다.

노드 내의 링크를 *pointers*라고도한다. 다른 노드를 "point"(가리키기)하기 때문이다.

일반적으로 데이터구조는 하나 이상의 링크가 있는 노드를 구현한다. 만약 이러한 링크가 `null`인 경우 이전에 따라가고 있던 노드의 링크가 끝에 도달했음을 뜻한다.

![node2](https://s3.amazonaws.com/codecademy-content/courses/learn-nodes-general/diagram_2.svg)

## Node Linking

가끔씩 데이터구조로 인해 노드는 다른 한개의 노드에서만 링크될 수 있다. 이는 데이터 구조에서 노드를 수정하거나 삭제할 때 중요하게 생각해야한다.

만약 실수로 하나만 존재하는 링크를 삭제한다면 그 노드의 데이터와 링크된 노드들은 "lost"될 수 있다. 이런 경우에 *orphaned*(분리된) 노드라고 부른다.

![orphaned](https://s3.amazonaws.com/codecademy-content/courses/learn-nodes-general/removing_nodes_3.gif)

위 그림에서 `node_c`는 `node_b`에 의해서만 연결된다. 만약 `node_b`를 지우고 `node_c`는 놔두고 싶다면 간단히 `node_a`에서 `node_b`로 연결되는 링크를 제거해주면 된다.

`node_c`를 유지하는 가장 간단한 방법은 `node_a`의 링크를 `node_b` 대신 `node_c`를 가리키도록 변경하는 것이다. 그러나 몇몇 데이터 구조는 이를 다른 방식으로 처리할 수 있다.

## Nodes Review

- Nodes:
  1. 데이터를 포함하고 다양한 형태의 데이터타입이 될 수 있다.
  2. 다른 노드에 링크되어있다. 만약 링크되어있는 노드가 없거나 `null`이라면 경로의 끝에 다다른것임을 의미한다.
  3. 링크걸린 다른 노드가 없다면 분리될 수 있다.