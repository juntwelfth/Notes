# Stacks

Stack은 순서대로 정렬된 데이터셋을 담고있는 데이터 구조이다.

스택은 상호작용을 위한 세가지 메소드를 제공한다.

1. Push - 데이터를 스택의 맨 위에 추가시킨다.
2. Pop - 데이터를 스택의 맨 위에서 삭제시키고 그 삭제시킨 데이터를 반환한다.
3. Peek - 스택의 맨 위 데이터를 반환한다.

Stack에 push를 할 수록 점점 쌓이게되며 삭제할 수 있는 데이터는 오로지 제일 위에있는 (마지막으로 추가한)데이터 뿐이다. 마지막으로 추가한 데이터는 첫번째 데이터가되며 접근할 수 있는 데이터가된다. 이것을 Last In, First Out | LIFO 구조라고 한다. 또한 First In, Last Out | FILO라고 불리기도 한다.

![stack](https://s3.amazonaws.com/codecademy-content/courses/learn-stacks-general/weight_Stacking.gif)

## Stacks Implementation

스택은 list 혹은 배열보다 효율적이므로 Linked List를 기본 데이터 구조로 사용하여 구현할 수 있다.

구현함에 따라, 스택의 가장 위에있는 데이터는 linked list의 head node이고 가장 아래있는 데이터는 linked list의 tail node가된다.

스택에는 크기의 제한이있다. 가득 차면 데이터 구조가 차지하는 자원을 제한한다.

이미 가득 찬 스택으로 데이터를 push하려고 하면 stack overflow가 발생한다. 마찬가지로 빈 스택에서 데이터를 pop하려고 하면 stack underflow가 발생한다.

![stack2](https://s3.amazonaws.com/codecademy-content/courses/learn-stacks-general/stack_linked_list.svg)

## Review

Stack이란

1. 데이터노드를 포함한다.
2. 세가지 연산을 제공한다.
   - Push - 데이터 추가시키기
   - Pop - 데이터 제거하기
   - Peek - 데이터 불러오기
3. Linked List 혹은 배열을 포함한다.
4. 크기가 제한이걸린다.
   - 공간이 없는 스택에 데이터를 push하면 stack overflow가 발생한다.
5. Last In, First Out (LIFO) 프로세싱을 따른다.
