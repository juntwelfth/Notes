# 파이썬으로 노드 구현
class Node:
    # link_node는 optional
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    # value값을 불러오는 메소드
    def get_value(self):
        return self.value

    # link 정보를 불러오는 메소드
    def get_link_node(self):
        return self.link_node

    # link_node를 설정해주는 메소드
    def set_link_node(self, link_node):
        self.link_node = link_node
        #: 한번 설정된 value는 수정할 수 없지만 link는 수정이 가능하다.


# 각 변수에 instance 생성
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

# 링크 걸어주기
yacko.set_link_node(dot)
dot.set_link_node(wacko)

# 링크를 통해 value 불러오기
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()
