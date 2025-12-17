from collections import deque
from typing import Any


class Stack:
    """Структура данных стек (LIFO) на базе list."""
    
    def __init__(self) -> None:
        """Инициализирует пустой стек."""
        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:
        """Добавляет элемент на вершину стека.
        
        Args:
            item: Элемент для добавления в стек.
        """
        self._data.append(item)
    
    def pop(self) -> Any:
        """Удаляет и возвращает верхний элемент стека.
        
        Returns:
            Верхний элемент стека.
            
        Raises:
            IndexError: Если стек пуст.
        """
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустого стека")
        return self._data.pop()
    
    def peek(self) -> Any | None:
        """Возвращает верхний элемент стека без удаления.
        
        Returns:
            Верхний элемент стека или None, если стек пуст.
        """
        return self._data[-1] if not self.is_empty() else None
    
    def is_empty(self) -> bool:
        """Проверяет, пуст ли стек.
        
        Returns:
            True, если стек пуст, иначе False.
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """Возвращает количество элементов в стеке.
        
        Returns:
            Количество элементов в стеке.
        """
        return len(self._data)
    
    def __str__(self) -> str:
        """Строковое представление стека.
        
        Returns:
            Строковое представление стека.
        """
        return f"Stack({self._data})"
    
    def __repr__(self) -> str:
        """Официальное строковое представление стека.
        
        Returns:
            Официальное строковое представление стека.
        """
        return f"Stack({self._data})"


class Queue:
    """Структура данных очередь (FIFO) на базе deque."""
    
    def __init__(self) -> None:
        """Инициализирует пустую очередь."""
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        """Добавляет элемент в конец очереди.
        
        Args:
            item: Элемент для добавления в очередь.
        """
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """Удаляет и возвращает элемент из начала очереди.
        
        Returns:
            Элемент из начала очереди.
            
        Raises:
            IndexError: Если очередь пуста.
        """
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустой очереди")
        return self._data.popleft()
    
    def peek(self) -> Any | None:
        """Возвращает элемент из начала очереди без удаления.
        
        Returns:
            Элемент из начала очереди или None, если очередь пуста.
        """
        return self._data[0] if not self.is_empty() else None
    
    def is_empty(self) -> bool:
        """Проверяет, пуста ли очередь.
        
        Returns:
            True, если очередь пуста, иначе False.
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """Возвращает количество элементов в очереди.
        
        Returns:
            Количество элементов в очереди.
        """
        return len(self._data)
    
    def __str__(self) -> str:
        """Строковое представление очереди.
        
        Returns:
            Строковое представление очереди.
        """
        return f"Queue({list(self._data)})"
    
    def __repr__(self) -> str:
        """Официальное строковое представление очереди.
        
        Returns:
            Официальное строковое представление очереди.
        """
        return f"Queue({list(self._data)})"