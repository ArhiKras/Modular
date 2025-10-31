#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py - Точка входа в приложение менеджера заметок
"""

import sys
from database import Database
from utils import add_note, show_all_notes, delete_note, search_notes, display_search_results


def print_menu():
    """Вывести главное меню"""
    print("\n" + "=" * 60)
    print("📒 МЕНЕДЖЕР ЗАМЕТОК")
    print("=" * 60)
    print("1. Добавить заметку")
    print("2. Показать все заметки")
    print("3. Удалить заметку")
    print("4. Поиск заметок")
    print("0. Выход")
    print("=" * 60)


def handle_add_note(db):
    """
    Обработка добавления заметки
    
    Args:
        db: Объект базы данных
    """
    print("\n--- Добавление заметки ---")
    text = input("Введите текст заметки: ").strip()
    add_note(db, text)


def handle_show_notes(db):
    """
    Обработка показа всех заметок
    
    Args:
        db: Объект базы данных
    """
    show_all_notes(db)


def handle_delete_note(db):
    """
    Обработка удаления заметки
    
    Args:
        db: Объект базы данных
    """
    show_all_notes(db)
    
    if db.get_notes_count() == 0:
        return
    
    try:
        note_num = int(input("\nВведите номер заметки для удаления: ").strip())
        delete_note(db, note_num)
    except ValueError:
        print("\n✗ Ошибка! Введите корректный номер.")
    except KeyboardInterrupt:
        print("\n\n✗ Операция отменена.")


def handle_search_notes(db):
    """
    Обработка поиска заметок
    
    Args:
        db: Объект базы данных
    """
    print("\n--- Поиск заметок ---")
    keyword = input("Введите ключевое слово для поиска: ").strip()
    
    if not keyword:
        print("\n✗ Ключевое слово не может быть пустым!")
        return
    
    results = search_notes(db, keyword)
    display_search_results(results)


def main():
    """Главная функция программы"""
    print("\n👋 Добро пожаловать в Менеджер заметок!")
    
    # Инициализация базы данных
    db = Database('notes.json')
    db.load()
    
    print(f"📊 Загружено заметок: {db.get_notes_count()}")
    
    # Главный цикл программы
    while True:
        try:
            print_menu()
            choice = input("\nВыберите действие (0-4): ").strip()
            
            if choice == '1':
                handle_add_note(db)
            
            elif choice == '2':
                handle_show_notes(db)
            
            elif choice == '3':
                handle_delete_note(db)
            
            elif choice == '4':
                handle_search_notes(db)
            
            elif choice == '0':
                print("\n👋 До свидания!\n")
                sys.exit(0)
            
            else:
                print("\n✗ Неверный выбор! Пожалуйста, выберите от 0 до 4.")
        
        except KeyboardInterrupt:
            print("\n\n👋 До свидания!\n")
            sys.exit(0)
        
        except Exception as e:
            print(f"\n⚠️ Произошла ошибка: {e}")


if __name__ == '__main__':
    main()

