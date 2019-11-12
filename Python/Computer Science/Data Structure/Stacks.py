# Node 파일에서 Node 클래스 가져오기
from Node import Node


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.limit = limit
        self.size = 0

    def push(self, value):
        # 만약 현재 stack의 공간이 남아있다면
        if self.has_space():
            # 새로운 Node 생성
            item = Node(value)
            # 현재 top_item을 새로 만든 Node의 다음 Node로 설정
            item.set_next_node(self.top_item)
            # 새로 만든 Node를 top_item으로 설정
            self.top_item = item
            # 추가했으니깐 size +1
            self.size += 1
        else:
            print("All out of space!")

    def pop(self):
        if self.is_empty():
            # 현재 top_item을 변수에 저장
            item_to_remove = self.top_item
            # top_item을 기존 top_item의 다음 node로 변경
            self.top_item = self.top_item.get_next_node()
            # 하나 지웠으니깐 size도 -1
            self.size -= 1
            # 현재 top_item의 value 리턴
            return item_to_remove.get_value()
        else:
            print("This Stack is Totally Empty.")

    def peek(self):
        if self.is_empty():
            # top_item을 Node 메소드를 이용해 value 가져오기
            return self.top_item.get_value()
        else:
            print("There's Nothing to See Here..")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0


n_c = Node(256)
n_b = Node(8, n_c)
n_a = Node(4, n_b)
a = Stack(n_b)

print(a.peek())
