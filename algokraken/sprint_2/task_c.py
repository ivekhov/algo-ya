# https://contest.yandex.ru/contest/22779/problems/C/
# Напишите функцию solution, которая принимает на вход голову списка и 
# номер удаляемого дела и возвращает голову обновлённого списка.


import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
	class Node:
		def __init__(self, value, next_item=None):
			self.value = value
			self.next_item = next_item

def print_linked_list(node):
	while node:
		print(node.value, end=" -> ")
		node = node.next_item
	print("None")


def get_node_by_index(head, index):
	curr_node = head
	cnt = 0
	for i in range(cnt, index + 1):
		if cnt == index:
			return curr_node
		else:
			cnt += 1
			curr_node = curr_node.next_item


def solution(node, idx):
	if idx == 0:
		replacement = node.next_item
		return replacement
	
	curr_node = node
	curr_idx = 0
	while curr_node:
		if curr_idx == idx:
			previous_node = get_node_by_index(node, curr_idx - 1)
			replacement = curr_node.next_item
			previous_node.next_item = replacement
			head = get_node_by_index(node, 0)
			return head
		curr_idx += 1
		curr_node = curr_node.next_item


def test():
	node3 = Node("node3", None)
	node2 = Node("node2", node3)
	node1 = Node("node1", node2)
	node0 = Node("node0", node1)

# 	print_linked_list(node0)

	new_head = solution(node0, 1)

# 	print_linked_list(new_head)

	assert new_head is node0
	assert new_head.next_item is node2
	assert new_head.next_item.next_item is node3
	assert new_head.next_item.next_item.next_item is None

#	result is node0 -> node2 -> node3


if __name__ == '__main__':
	test()
