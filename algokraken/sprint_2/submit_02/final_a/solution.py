'''
Успешная посылка: 
140879860
140826719 (предыдущий сабмит)
https://contest.yandex.ru/contest/22781/run-report/140826719/

Задача: https://contest.yandex.ru/contest/22781/problems/A/

==Изменения==
1. Добавил классы ошибок DequeEmptyError и DequeFullError
2. В выводе в файл используется 'error', сообщение самой ошибки не выводится,
т к показалось некорректным заменять в классах ошибок содержательноый текст на 
абстрактный 'error' только чтобы использовать в скрипте переменную e. 

Тестирование у меня производится с помощью pytest, здесь не прикладываю, т к 
не требуется в задаче. 


==ПРИНЦИП РАБОТЫ==
Дек реализован на кольцевом буфере, согласно условию задачи.
Руководствовался примером из теории урока по Очередям и Деку.
В частности, приемом изменения индекса головы и хвоста с помощью вычисления
остатка от деления по модулю. 

Алгоритмы вставки/удаления в начало и в конец работают как два револьверных 
барабана, вращающихся (почти) независимо друг от друга, 
в которых патроны заполняют пустые гнезда.

Индекс головы указывает на первое крайнее слева заполненое место в деке.
Индекс хвоста - на пустое место, следующее вправо за последним заполненным.


==ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ==

При добавлении элемента в голову индекс головы сдвигается на 1 влево, 
а в то место, откуда был сдвинут индекс, кладется добавляемый элемент. 
При добавлении элемента в хвост элемент кладется по индексу хвоста, 
всегда пустому, индекс хвоста увеличивается на 1.
Условие выполнения обоих вставок: размер не должен быть равен 
максимально возможному, указанному при инициализации дека. Это гарантирует, 
что индексы головы и хвоста не будут пересекаться и добавление в голову (или
хвост) не заменит находящийся в деке элемент.

Дек реализует требования к очереди и стеку, т.е. позволяет добавлять и удалять
элементы как с начала, так и с конца списка. 
Таким образом, дек может работать по принципу стека (LIFO — последний пришёл, 
первый ушёл) и по принципу очереди (FIFO — первый пришёл, первый ушёл.


==ВРЕМЕННАЯ СЛОЖНОСТЬ==

Добавление выполняется за O(1) ("сложность О от 1"), т.к. вставка 
производится сразу, без поиска следующего свободного места в деке. 
Таким образом, сложность не зависит от размера деки (количества элементов в нем)
Всего выполняется 3 действия: помещение элемента в стек, изменение индекса, 
изменение размера. Не включая операцию проверки размера дека.

Извлечение выполняется за O(1), т.к. индекс извлекаемого элемента известен до
извлечения. Работая с Деком, можно извлекать элементы только из головы или 
хвоста, но не по произвольному индексу. Сложность также не зависит от кол-ва
элементов в деке. 


==ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ==

Размер дека определяется аргументом максимального количества элементов при 
создании дека.
В деке используется только один контейнер - поэтому сложность не превышает n.
В реализации на Python при иниц-ции None всего дека, размер дека при добавлении
или удалении элемента, размер не меняется, т.к. происходит замена None на 
значение. В примере это int. 

'''
class DequeEmptyError(Exception):
	def __init__(self):
		super().__init__("Deque is empty")

class DequeFullError(Exception):
	def __init__(self):
		super().__init__("Deque is full")

class Deque:
	def __init__(self, max_size):
		self.max_size = max_size
		self.deque = [None] * max_size
		self.size = 0
		self.head = 0
		self.tail = 0
		
	def push_back(self, value):
		if self.size == self.max_size:
			raise DequeFullError()
		self.deque[self.tail] = value
		self.tail = (self.tail + 1) % self.max_size
		self.size += 1

	def pop_back(self):
		if self.size == 0:
			raise DequeEmptyError()
		self.tail = (self.tail - 1) % self.max_size
		item = self.deque[self.tail]
		self.deque[self.tail] = None
		self.size -= 1
		return item

	def push_front(self, value):
		if self.size == self.max_size:
			raise DequeFullError()
		self.head = (self.head - 1) % self.max_size
		self.deque[self.head] = value
		self.size += 1

	def pop_front(self):
		if self.size == 0:
			raise DequeEmptyError()
		item = self.deque[self.head]
		self.deque[self.head] = None
		self.head = (self.head + 1) % self.max_size
		self.size -= 1
		return item

	def is_empty(self):
		return self.size == 0


def main(input_file='input.txt', output_file='output.txt'):
	with open(input_file, 'r') as f:
		n = int(f.readline().rstrip())
		max_size = int(f.readline().rstrip())
		deque = Deque(max_size)
		with open(output_file, 'w') as f_out:
			for _ in range(n):
				commands = f.readline().rstrip().split(' ')

				if commands[0] == 'push_front':
					try:
						deque.push_front(int(commands[1]))
					except DequeFullError:
						f_out.write('error\n')

				elif commands[0] == 'pop_front':
					try:
						res = deque.pop_front()
						f_out.write(f'{str(res)}\n')
					except DequeEmptyError:
						f_out.write('error\n')

				elif commands[0] == 'push_back':
					try:
						deque.push_back(int(commands[1]))
					except DequeFullError:
						f_out.write('error\n')

				elif commands[0] == 'pop_back':
					try:
						res = deque.pop_back()
						f_out.write(f'{str(res)}\n')
					except DequeEmptyError:
						f_out.write('error\n')


if __name__ == '__main__':
	fixtures =[
        ['input.txt', 'output.txt'],
        # ['input_2.txt', 'output_2.txt'],
        # ['input_3.txt', 'output_3.txt'],
    ]
	for fixture in fixtures:
		main(fixture[0], fixture[1])
