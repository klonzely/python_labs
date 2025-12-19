from typing import Any, Optional, Iterator


class Node:
    """Узел односвязного списка"""
    
    def __init__(self, value: Any, next_node: Optional['Node'] = None):
        self.value = value
        self.next = next_node
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    """Односвязный список"""
    
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка за O(1)"""
        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        """Добавить элемент в начало списка за O(1)"""
        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        """Вставить элемент по индексу idx"""
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")
        
        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            new_node = Node(value, current.next)
            current.next = new_node
            self._size += 1
    
    def remove_at(self, idx: int) -> None:
        """Удалить элемент по индексу idx"""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size})")
        
        if idx == 0:  # Удаление из начала
            self.head = self.head.next
            if self.head is None:  # Если список стал пустым
                self.tail = None
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            # current теперь указывает на узел перед удаляемым
            current.next = current.next.next
            
            # Если удалили последний элемент
            if current.next is None:
                self.tail = current
        
        self._size -= 1
    
    def remove(self, value: Any) -> None:
        """Удалить первое вхождение значения value"""
        if self.is_empty():
            return
        
        # Если удаляем из начала
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return
        
        # Ищем узел перед тем, который нужно удалить
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        
        # Если нашли значение
        if current.next and current.next.value == value:
            current.next = current.next.next
            self._size -= 1
            
            # Если удалили последний элемент
            if current.next is None:
                self.tail = current
    
    def is_empty(self) -> bool:
        """Проверка, пуст ли список"""
        return self.head is None
    
    def __iter__(self) -> Iterator[Any]:
        """Итератор по значениям списка"""
        current = self.head
        while current:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        """Количество элементов в списке"""
        return self._size
    
    def __repr__(self) -> str:
        """Строковое представление списка"""
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def __getitem__(self, idx: int) -> Any:
        """Получить значение по индексу (дополнительный метод)"""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size})")
        
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value