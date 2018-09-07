# Jupyter notebook

_И это теперь обучение? Запустить все ячейки и посмотреть, что произошло._

[Jupyter notebook](http://jupyter.org) -- это интерактивная среда для вычислений, про которую можно погулить. Если коротко, то есть "тетрадки" (notebooks), в которых есть ячейки (cells), в них может быть гипертекст/markdown или код.

Удобная среда для интерактивной работы: ты нажал на ячейку, выполнил её и посмотрел на результат, а не запускаешь каждый раз абсолютно все вычисления по-новой.

Пока это звучит сумбурно, но потом все станет понятно.

## Откуда взять?

Есть несколько вариантов работы с ноутбуками:
1. Поставить Anaconda
2. Поставить Python и накатывать все руками
3. Ничего не ставить и запускать все в интернете (Благо есть куча бесплатных и платных вариантов)

### Anaconda

Большой пакет со всеми батарейками, библиотеками и прочим хламом, который нам понадобится.

Взять можно по [ссылке](https://conda.io/docs/user-guide/install/windows.html)

Это рекомендуемый путь для любителей __винды__ или тех, кому хочется работать локально, но не хочется заморачиваться с пакетами (но мы вас не судим).

### Для смелых

1. Ставите python3 одним из способов:
  1. Ubuntu
    1. `$sudo apt-get update`
    2. `$sudo apt-get install python3.6`
  2. MacOS
    1. [Вот нормальный туториал](https://docs.python-guide.org/starting/install3/osx/) (Да и вообще книжка ничего)
    1. Сначала надо заварить пивас
      - Устанавливаем Command Line Tools установив XCode или [Command Line Tools](https://developer.apple.com/downloads/) (Чуть полегче, потому что нет всякой всячины для разработки приложений)
      - `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
        - Это [менеджер пакетов для macOS](https://brew.sh/index_ru), если у вас еще нет
    2. `brew install python3`
  3. Под виндой -- [Anaconda](https://conda.io/docs/user-guide/install/windows.html)
2. Если не установлен pip, то [ставим](https://pip.pypa.io/en/stable/installing/)
3. `$pip3 install virtualenv` в папке с курсом
4. `$virtualenv -p python3 venv`
5. `$source venv/bin/activate`
6. `$pip3 install -r requirements.txt`

### Я не хочу засорять свой ноут ради этого курса

В интернете есть куча вариантов, платных и бесплатных, для запуска ноутбуков. Ниже те, которые я смог вспомнить:

- [Google colab](https://colab.research.google.com/)
  - Вроде бы даже gpu бесплатно дают
- [Kaggle](https://www.kaggle.com)
  - Делать из своих ноутбуков kernels (Хз, насколько валидный путь)
- [Да нафиг мне ваш сахар, я сам себе все библиотеки напишу](https://repl.it)

## Запускаем Jupyter notebook:
В папке курса:

`$jupyter notebook`

И вас должно выкинуть в браузер

# Куда дальше?

Можно открыть `python_example.ipynb` в папке `introduction`
