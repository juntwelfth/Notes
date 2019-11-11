# 먼저 노드를 생성해준다.
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


# LinkedList 클래스 생성
class LinkedList:
    def __init__(self, value=None):
        # head node를 Node 클래스를 이용하여 생성해준다.
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    # 새로운 node를 생성하는 메소드
    def insert_beginning(self, new_value):
        # new_value를 이용해 새로운 node 인스턴스를 만들어준다.
        new_node = Node(new_value)

        # 새로 만든 node를 현재 head_node에 연결해준다.
        new_node.set_next_node(self.head_node)

        # 방금만든 node를 head node로 설정해준다.
        self.head_node = new_node

    # string print전용 메소드
    def stringify_list(self):
        result = ""
        # 현재 head node가 존재할 때
        while self.head_node:
            # 만약 head node의 value가 None이 아니라면
            if self.head_node.get_value() != None:
                result += str(self.head_node.get_value()) + '\n'
            # head node를 head node의 다음 node로 설정
            self.head_node = self.head_node.get_next_node()
        return result

    # node를 삭제하는 메소드
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        # 만약 현재 head node를 삭제하려고 한다면
        if current_node.get_value() == value_to_remove:
            # head node를 head node 다음 노드로 변경
            self.head_node = current_node.get_next_node()

        # 현재 head node가 아니라면
        else:
            while current_node:
                next_node = current_node.get_next_node()
                # 만약 현재 head node의 다음 node 즉 2번째 노드라면
                if next_node.get_value() == value_to_remove:
                    # 현재 head node의 다음 node를 건너뛰고 그 다음 node로 설정 즉 2번째 노드를 버리고 3번째 노드로 설정
                    current_node.set_next_node(next_node.get_next_node())

                    # 현재 head node를 None으로 설정
                    current_node = None

                # 현재 head node의 다음 node가 아니라면 그 다음 node를 체크
                else:
                    current_node = next_node
