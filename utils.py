#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
utils.py - Утилиты для работы с заметками
"""

from datetime import datetime


def create_note(text):
    """
    Создать новую заметку
    
    Args:
        text (str): Текст заметки
        
    Returns:
        dict: Словарь с данными заметки
    """
    note = {
        'text': text,
        'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return note


def add_note(database, text):
    """
    Добавить заметку в базу данных
    
    Args:
        database: Объект базы данных
        text (str): Текст заметки
        
    Returns:
        bool: True если добавление успешно
    """
    if not text or not text.strip():
        print("\n✗ Текст заметки не может быть пустым!")
        return False
    
    note = create_note(text)
    database.add_note(note)
    notes_count = database.get_notes_count()
    print(f"\n✓ Заметка #{notes_count} успешно добавлена!")
    return True


def show_all_notes(database):
    """
    Показать все заметки
    
    Args:
        database: Объект базы данных
    """
    notes = database.get_all_notes()
    
    if not notes:
        print("\n📝 Список заметок пуст.")
        return
    
    print("\n" + "=" * 60)
    print("📝 СПИСОК ЗАМЕТОК")
    print("=" * 60)
    
    for index, note in enumerate(notes, start=1):
        print(f"\n[{index}] {note['created']}")
        print(f"    {note['text']}")
    
    print("\n" + "=" * 60)
    print(f"Всего заметок: {len(notes)}")


def delete_note(database, note_number):
    """
    Удалить заметку по номеру
    
    Args:
        database: Объект базы данных
        note_number (int): Номер заметки (начиная с 1)
        
    Returns:
        bool: True если удаление успешно
    """
    # Преобразуем номер в индекс (нумерация с 1, индексы с 0)
    index = note_number - 1
    
    if database.remove_note(index):
        print(f"\n✓ Заметка #{note_number} успешно удалена!")
        return True
    else:
        print(f"\n✗ Заметка #{note_number} не найдена!")
        return False


def format_note(note, index):
    """
    Форматировать заметку для отображения
    
    Args:
        note (dict): Словарь с данными заметки
        index (int): Номер заметки
        
    Returns:
        str: Отформатированная строка
    """
    return f"[{index}] {note['created']} - {note['text']}"


def search_notes(database, keyword):
    """
    Поиск заметок по ключевому слову
    
    Args:
        database: Объект базы данных
        keyword (str): Ключевое слово для поиска
        
    Returns:
        list: Список найденных заметок с их индексами
    """
    notes = database.get_all_notes()
    results = []
    
    keyword_lower = keyword.lower()
    for index, note in enumerate(notes, start=1):
        if keyword_lower in note['text'].lower():
            results.append((index, note))
    
    return results


def display_search_results(results):
    """
    Отобразить результаты поиска
    
    Args:
        results (list): Список кортежей (индекс, заметка)
    """
    if not results:
        print("\n📝 Ничего не найдено.")
        return
    
    print("\n" + "=" * 60)
    print(f"🔍 РЕЗУЛЬТАТЫ ПОИСКА (найдено: {len(results)})")
    print("=" * 60)
    
    for index, note in results:
        print(f"\n[{index}] {note['created']}")
        print(f"    {note['text']}")
    
    print("\n" + "=" * 60)

