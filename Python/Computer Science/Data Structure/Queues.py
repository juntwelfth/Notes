from Node import Node


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        # 현재 queue에 공간이 있다면
        if self.has_space():
            # 새로운 Node 생성
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            # 현재 queue에 공간이 있고, 빈 queue라면
            if self.is_empty():
                # 현재 queue의 head와 tail을 방금 생성한 Node로 설정
                self.head = item_to_add
                self.tail = item_to_add
            # 빈 queue가 아니라면
            else:
                # 방금 생성한 Node를 현재 tail의 다음 순서로 설정
                self.tail.set_next_node(item_to_add)
                # tail을 방금 추가한 Node로 변경 (head는 유지)
                self.tail = item_to_add
                # size + 1
                self.size += 1
        # 현재 queue에 공간이 없다면
        else:
            print("Sorry, no more room!")

    def dequeue(self):
        # 현재 queue가 비어있지 않다면
        if not self.is_empty():
            item_to_remove = self.head
            print("Removing " + str(item_to_remove.get_value()) + " from the queue!")

            # 현재 queue의 크기가 딱 1이라면
            if self.size == 1:
                # head와 tail을 삭제
                self.head = None
                self.tail = None
            # 현재 queue의 크기가 1보다 크다면
            else:
                # head를 head의 다음 node로 설정
                self.head = self.head.get_next_node()
            # queue의 size - 1
            self.size -= 1
            # 방금 지운 node의 value 반환
            return item_to_remove.get_value()
        else:
            print("This queue is totally empty!")

    def peek(self):
        if self.get_size() == 0:
            print("Nothing to see here!")
        else:
            return self.head.get_value()

    def get_size(self):
        return self.size

    def has_space(self):
        # max_size가 truthy면 공간이 있다는 뜻이므로 True 반환
        if not self.max_size:
            return True
        # 현재 size가 max_size보다 작은지 (여유공간이 있는지)
        return self.max_size > self.get_size()

    def is_empty(self):
        return self.get_size() == 0
