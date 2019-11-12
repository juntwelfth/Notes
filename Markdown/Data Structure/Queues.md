# Queues

Queue는 순서가있는 데이터를 포함하고있는 데이터 구조다.

Stack과 마찬가지로 세가지의 메소드를 제공한다.

1. Enqueue - Queue의 맨뒤에 데이터를 추가한다.
2. Dequeue - Queue의 맨앞에 데이터를 제거하고 반환한다.
3. Peek - Queue의 맨앞 데이터를 반환한다.

![queue](https://s3.amazonaws.com/codecademy-content/courses/learn-queues-general/movie_line.gif)

Queue의 처음으로 추가된 데이터가 첫번째로 반환된다. First In, First Out (FIFO)

## Queues Implementation

Queue는 linked list를 사용하여 구현할 수 있다. Queue의 맨앞에 있는 데이터는 linked list의 head node고 맨 뒤에있는 데이터는 tail node 와 같다.

Queue의 메소드가 맨 앞과 맨 뒤의 데이터만 영향을 끼칠 수 있기 때문에 Linked List 내부의 데이터 노드들을 여행하는것은 불가능하다. 큐의 양쪽 끝에 모두 접근이 가능해야하므로 head node와 tail node가 존재해야만 한다.

Queue의 제약조건으로는 길이이다. 큐에 넣을 수 있는 데이터의 양에 제한이있는 경우 큐는 *bounded queue*로 간주된다.

스택과 마찬가지로 이미 가득 찬 queue에 데이터를 추가시키려고 하면 *queue overflow*가 발생한다. 빈 queue에서 데이터를 빼려고하면 *queue underflow*가 발생한다.

![queue2](https://s3.amazonaws.com/codecademy-content/courses/learn-queues-general/queue_linked_list.svg)

## Review

Queue는

1. 데이터 노드를 포함한다.
2. 세개의 메소드를 지원한다.
    - 데이터를 추가할 땐 queue의 마지막에 추가된다.
    - 데이터를 제거하고 반환할 땐 첫번째 데이터가 선택된다.
    - 첫번째 데이터를 반환할 수 있다.
3. Linked List 혹은 배열로 구현할 수 있다.
4. Bounded queues(제한된 큐)는 사이즈(크기)가 제한되어있다.
5. Stack과 마찬가지로 overflow, underflow가 존재한다.
6. First In, First Out (FIFO)을 따른다.