# Linked List

Linked List 또한 컴퓨터 과학에 사용되는 기본 데이터 구조 중 하나이다. Linked List는 많은 직접적인 응용프로그램을 가지고있고 복잡한 데이터 구조의 기초로 사용된다.

![ll](https://s3.amazonaws.com/codecademy-content/courses/learn-linked-lists-general/Linked+List.svg)

List는 위 그림과 같이 노드의 집합으로 이루어져 있다. head node는 list의 처음으로 오는 노드를 말한다. 각 노드는 데이터와 list의 다음 노드에대한 링크(혹은 포인터)로 이루어져있다. list는 노드의 링크가 null일 때 종료된다. 그리고 이러한 노드를 tail node라고 한다.

비행기 편도여행을 생각해보자. 이 여행은 여행 경로 구간(링크)으로 연결된 여러개의 공항(노드)을 포함한다. 이 예제에서 출발하는 공항이 head node, 마지막에 도착하는 공항을 tail node라고 부른다.

노드는 링크를 사용하여 다음 노드를 나타내므로 노드는 메모리에 순서대로 위치 할 필요가 없다. 이러한 링크들은 노드의 빠른 삽입과 삭제를 하게해준다.

- Linked List의 일반적인 연산은 다음과같다.
  1. 노드 추가
  2. 노드 삭제
  3. 노드 찾기
  4. Linked List 돌아다니기

Linked list는 일반적으로 단방향 링크만 존재한다. (다음 노드) 하지만 몇몇 구현은 양방향 링크를 사용할 수 있게 해준다. (이전, 다음 노드)

## Adding and Removing Nodes

Linked list에서 노드들은 다른 하나의 노드에서만 링크되어있기 때문에 좋든싫든 약간의 작업없이 노드를 추가하거나 제거할 수 없다.

### Adding a new node

List의 시작부분에 새 노드를 추가하려면 새로운 노드를 현재 헤드 노드에 연결해야한다. 이렇게하면 list에서 다음 노드와의 연결을 유지할 수 있다.

### Removing a node

실수로 노드에 대한 단일 링크를 제거하게되면 해당 노드의 데이터와 다음 노드가 손실되어 orphaned 노드가 남겨질 수 있다.

링크된 list의 중간에서 노드를 제거할 때 순서를 유지하려면 이전 노드에서 다음 노드를 가리키도록 링크를 조정해야한다.

언어에따라 참조되지 않은 노드는 자동으로 제거된다. 노드를 "제거"하는 것은 노드에대한 모든 참조를 제거하는 것과 같다.

![s](https://s3.amazonaws.com/codecademy-content/courses/learn-nodes-general/removing_nodes_gif_preview_v2.png)

## Review

Linked List?

1. 노드로 구성되어있다.
2. 노드에는 다음 노드에 대한 링크(및 양방향 링크된 list의 이전 노드)가 포함된다.
3. 단방향 혹은 양방향이 될 수 있다.
4. 기초 데이터 구조이며 다른 데이터 구조들의 기반이된다.
5. 한개의 헤드노드를 가지고있고 이 헤드노드는 list에서 첫번째 노드로 사용된다.
6. 노드를 추가하거나 제거할 때 약간의 유지관리가 필요하다.
