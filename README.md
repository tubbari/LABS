��#   L A B S 


Цей репозиторій містить збірку навчальних робіт з програмування.

## Структура репозиторію

.
├── README.md     // Цей файл з описом репозиторію
├── lab3         // лабораторна роботи №3
├── lab1         // лабораторна роботи №1
├── navprac         // Папка зі сторонніми файлами
├──Untitled2       //лабараторна робота №6
├──blocks         // CSV файл з вхідними даними для лабораторної №1
├──chain         // CSV файл з вхідними даними для лабораторної №1
├──votes         //CSV файл з вивідними даними для лабораторної №1
└──hupert/          //лабораторна роботи №4



* `README.md`: Містить загальний опис репозиторію та його структуру.
* `lab1/`: Містить файли, пов'язані з лабораторною роботою №1.
* `blocks/`: Містить файли, пов'язані з лабораторною роботою №1.
* `chain/`: Містить файли, пов'язані з лабораторною роботою №1.
* `votes/`: Містить файли, пов'язані з лабораторною роботою №1.
* `lab3/`: Містить файли, пов'язані з лабораторною роботою №3.
* `hupert/`: Містить файли, пов'язані з лабораторною роботою №4.
* `Untitled2/`: Містить файли, пов'язані з лабораторною роботою №6.
## Лабораторна робота №3 Python Regular Expressions

## Лабораторна робота №4 Git Merges + BlockProcessor extension

Ця лабораторна робота присвячена реалізації бінарного дерева пошуку на основі даних, отриманих в процесі виконання роботи №1. Програма зчитує дані з файлу `votes.csv` та визначається тип дерева та виконуються основні алгоритми обходу з виведенням результатів на консоль.

### Файли, що використовуються (hupert/)

* `votes.csv`: Файл, який містить ланцюжок блоків. Значення зі стовпця `'view'` цього файлу використовуються для побудови бінарного дерева пошуку.

### Файли, що можуть бути присутні (hupert/)

* `blocks.csv`: Файл з даними про блоки (може використовуватися для генерації `chain.csv`).
* `votes.csv`: Файл з даними про голоси за блоки (може використовуватися для генерації `chain.csv`).
* `chain.csv`: Файл з даними про ланцюг.

### Запуск (hupert/)

1.  Переконайтеся, що у папці `hupert/` знаходиться основний Python-скрипт та файл `votes.csv` (якщо він не генерується скриптом).
2.  Запустіть основний Python-скрипт з папки `hupert/`.
3.  Результати (тип дерева та результати обходів) будуть виведені на консоль.
