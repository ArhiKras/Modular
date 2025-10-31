#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
database.py - Модуль для работы с хранилищем заметок
"""

import json
import os


class Database:
    """Класс для работы с базой данных заметок (JSON файл)"""
    
    def __init__(self, filename='notes.json'):
        """
        Инициализация базы данных
        
        Args:
            filename (str): Имя файла для хранения заметок
        """
        self.filename = filename
        self.notes = []
    
    def load(self):
        """
        Загрузить заметки из файла
        
        Returns:
            list: Список заметок
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.notes = json.load(f)
                    return self.notes
            except (json.JSONDecodeError, IOError) as e:
                print(f"⚠️ Ошибка при загрузке данных: {e}")
                self.notes = []
                return self.notes
        else:
            self.notes = []
            return self.notes
    
    def save(self):
        """
        Сохранить заметки в файл
        
        Returns:
            bool: True если сохранение успешно, False в случае ошибки
        """
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.notes, f, ensure_ascii=False, indent=2)
            return True
        except IOError as e:
            print(f"⚠️ Ошибка при сохранении данных: {e}")
            return False
    
    def get_all_notes(self):
        """
        Получить все заметки
        
        Returns:
            list: Список всех заметок
        """
        return self.notes
    
    def add_note(self, note):
        """
        Добавить заметку в базу
        
        Args:
            note (dict): Словарь с данными заметки
        """
        self.notes.append(note)
        self.save()
    
    def remove_note(self, index):
        """
        Удалить заметку по индексу
        
        Args:
            index (int): Индекс заметки в списке
            
        Returns:
            bool: True если удаление успешно, False если индекс неверный
        """
        if 0 <= index < len(self.notes):
            self.notes.pop(index)
            self.save()
            return True
        return False
    
    def clear_all(self):
        """Очистить все заметки"""
        self.notes = []
        self.save()
    
    def get_notes_count(self):
        """
        Получить количество заметок
        
        Returns:
            int: Количество заметок
        """
        return len(self.notes)

